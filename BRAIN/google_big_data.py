

import re
import time
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from jarvis_speak.speak import speak_safe

# from jarvis_speak.speak import speak_safe

# ---------------- CONFIG ----------------
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36"
)

TOP_N_RESULTS = 3          # number of search results to fetch
MAX_COMBINED_WORDS = 1000  # limit text length before summarizing
DETAILED_SENTENCES = 6


# ---------------- HELPERS ----------------
def duckduckgo_search(query, num_results=TOP_N_RESULTS):
    """Perform DuckDuckGo search (HTML endpoint) and return top result URLs."""
    search_url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": USER_AGENT}
    data = {"q": query}
    res = requests.post(search_url, data=data, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "lxml")

    links = []
    for a in soup.select("a.result__a")[:num_results]:
        href = a.get("href")
        if href and href.startswith("http") and "duckduckgo.com" not in href:
            links.append(href)
    return links


def fetch_page_text(url):
    """Fetch a web page and extract readable text."""
    try:
        headers = {"User-Agent": USER_AGENT}
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
    except Exception:
        return ""

    soup = BeautifulSoup(res.text, "lxml")

    # Remove non-text elements
    for s in soup(["script", "style", "header", "footer", "nav", "aside"]):
        s.decompose()

    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
    long_paragraphs = [p for p in paragraphs if len(p.split()) > 40]

    text = " ".join(long_paragraphs)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def summarize_text(text, sentence_count):
    """Use Sumy LSA summarizer to summarize long text."""
    if not text or len(text.split()) < 40:
        return text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(s) for s in summary)


def combine_texts(texts, word_limit=MAX_COMBINED_WORDS):
    combined = " ".join(t for t in texts if t)
    words = combined.split()
    if len(words) <= word_limit:
        return combined
    return " ".join(words[:word_limit])


# ---------------- MAIN CHATBOT ----------------
def answer_query(query):
    
    urls = duckduckgo_search(query)
    if not urls:
        return "Sorry, I couldn't find anything."

    all_texts = []
    for url in urls:
        
        text = fetch_page_text(url)
        if text:
            all_texts.append(text)
        time.sleep(0.5)

    combined = combine_texts(all_texts)
    if not combined:
        return "Couldn't extract readable content."

    detailed = summarize_text(combined, DETAILED_SENTENCES)
    return detailed


# ---------------- INTERACTIVE LOOP ----------------
def run_chat(text):
    q = text.strip()
    if not q:
        return "(no query provided)"
    

    detailed = answer_query(q)
    speak_safe(detailed or "(no detail available)")
    return detailed




