import warnings
warnings.filterwarnings("ignore")

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QGraphicsDropShadowEffect, QTextEdit
)
from PyQt5.QtCore import Qt, QUrl, QPropertyAnimation, QEasingCurve, QTimer, pyqtProperty, QProcess
from PyQt5.QtGui import QColor, QPainter, QRadialGradient, QPen
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


# ---------- Pulsing Halo ----------
class Halo(QWidget):
    def __init__(self, parent=None, color=QColor(0, 255, 255)):
        super().__init__(parent)
        self._scale = 1.0
        self.color = color
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(220, 220)

    def setScale(self, value: float):
        self._scale = value
        self.update()

    def getScale(self) -> float:
        return self._scale

    scale = pyqtProperty(float, fget=getScale, fset=setScale)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(self._scale, self._scale)

        radius = 90
        grad = QRadialGradient(0, 0, radius * 1.3)
        base = self.color
        grad.setColorAt(0.0, QColor(base.red(), base.green(), base.blue(), 100))
        grad.setColorAt(0.5, QColor(base.red(), base.green(), base.blue(), 50))
        grad.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.setBrush(grad)
        pen = QPen(QColor(base.red(), base.green(), base.blue(), 100))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawEllipse(-radius, -radius, 2 * radius, 2 * radius)


# ---------- Main UI ----------
class JarvisUI(QWidget):
    def __init__(self, main_py_path, webm_path, click_sound_path=None):
        super().__init__()
        self.main_py_path = main_py_path
        self.webm_path = webm_path
        self.click_sound_path = click_sound_path
        self.player = QMediaPlayer()
        self.is_listening = False
        self.halo_anim = None
        self.process = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("JARVIS Interface")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # --- Background video ---
        self.web_view = QWebEngineView(self)
        html = f"""
        <html><body style="margin:0; background:black; overflow:hidden;">
        <video autoplay loop muted playsinline width="100%" height="100%">
            <source src="file:///{self.webm_path.replace(os.sep, '/')}" type="video/webm">
        </video></body></html>
        """
        tmp_html = os.path.join(os.path.dirname(self.webm_path), "temp_ui.html")
        with open(tmp_html, "w", encoding="utf-8") as f:
            f.write(html)
        self.web_view.load(QUrl.fromLocalFile(tmp_html))
        self.web_view.setGeometry(0, 0, 1920, 1080)

        # --- Mic core ---
        self.core = QLabel(self)
        self.core_size = 160
        self.set_mic_style()
        self.center_mic()

        # --- Halo ---
        self.halo = Halo(self)
        self.halo.move(self.core.x() - 30, self.core.y() - 30)
        self.halo.resize(self.core_size + 60, self.core_size + 60)

        # --- Input box (user voice + listening text) ---
        self.input_box = QTextEdit(self)
        self.input_box.setGeometry(80, 575, 600, 350 )
        self.style_box(self.input_box, "cyan")
        self.input_box.setReadOnly(True)
        self.input_box.setPlaceholderText("Listening here...")

        # --- Output box (Jarvis replies) ---
        self.output_box = QTextEdit(self)
        self.output_box.setGeometry(1200, 100, 600, 400)
        self.style_box(self.output_box, "#00ffcc")
        self.output_box.setReadOnly(True)
        self.output_box.setPlaceholderText("Jarvis responses appear here...")

        # --- Glow effect ---
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(80)
        glow.setColor(QColor(0, 255, 255))
        glow.setOffset(0, 0)
        self.core.setGraphicsEffect(glow)

        self.core.mousePressEvent = self.activate_jarvis

    def style_box(self, box, color):
        box.setStyleSheet(f"""
            QTextEdit {{
                background-color: rgba(0, 20, 40, 130);
                border: 2px solid {color};
                border-radius: 15px;
                color: white;
                font-family: Consolas;
                font-size: 16px;
                padding: 10px;
            }}
        """)

    def center_mic(self):
        x = self.width() // 2 - self.core_size // 2
        y = self.height() - 300
        self.core.setGeometry(x, y, self.core_size, self.core_size)

    def set_mic_style(self, active=False):
        if active:
            self.core.setStyleSheet("""
                QLabel {
                    background-color: qradialgradient(
                        cx:0.5, cy:0.5, radius:0.8,
                        stop:0 #00ffff, stop:1 #0044ff);
                    border-radius: 80px;
                    border: 3px solid rgba(0,255,255,0.9);
                }
            """)
        else:
            self.core.setStyleSheet("""
                QLabel {
                    background-color: qradialgradient(
                        cx:0.5, cy:0.5, radius:0.9,
                        stop:0 #001a26, stop:1 #000000);
                    border-radius: 80px;
                    border: 2px solid rgba(0,255,255,0.3);
                }
            """)

    def activate_jarvis(self, event):
        if self.is_listening:
            return
        self.play_click_sound()
        self.set_mic_style(True)
        self.start_pulse()
        self.is_listening = True
        self.input_box.clear()
        self.output_box.clear()
        self.run_main_file()

    def play_click_sound(self):
        if self.click_sound_path and os.path.exists(self.click_sound_path):
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.click_sound_path)))
            self.player.play()

    def start_pulse(self):
        if self.halo_anim:
            self.halo_anim.stop()
        self.halo_anim = QPropertyAnimation(self.halo, b"scale")
        self.halo_anim.setDuration(1500)
        self.halo_anim.setStartValue(1.0)
        self.halo_anim.setEndValue(1.7)
        self.halo_anim.setEasingCurve(QEasingCurve.InOutSine)
        self.halo_anim.setLoopCount(-1)
        self.halo_anim.start()

    def stop_pulse(self):
        if self.halo_anim:
            self.halo_anim.stop()
            self.halo_anim = None
        self.set_mic_style(False)
        self.is_listening = False
        self.halo.update()

    def run_main_file(self):
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.finished.connect(lambda: QTimer.singleShot(200, self.stop_pulse))
        self.process.start(sys.executable, [self.main_py_path])

    def handle_output(self):
        data = self.process.readAllStandardOutput().data().decode("utf-8", errors="ignore").strip()
        if not data:
            return

        # Send recognized listening text to input box, others to output box
        lower_data = data.lower()
        if any(word in lower_data for word in ["listening", "hearing", "you said", "recognizing", "user :"]):
            self.input_box.append(data)
        else:
            self.output_box.append(data)


if __name__ == "__main__":
    main_py = r"C:\Users\hp\Desktop\JARVIS project\main.py"
    webm = r"C:\Users\hp\Desktop\JARVIS project\JARVIS_UI\50504.webm"
    click_sound = r"C:\Users\hp\Desktop\JARVIS project\JARVIS_UI\sound.mp3"

    app = QApplication(sys.argv)
    jarvis = JarvisUI(main_py, webm, click_sound)
    jarvis.showMaximized()
    sys.exit(app.exec_())
