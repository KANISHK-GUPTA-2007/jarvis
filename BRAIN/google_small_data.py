import requests
from bs4 import BeautifulSoup
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

from jarvis_speak.speak import speak_safe

# --- Summarize text ---
def summarize_text(text, sentence_count=2):
    if not text or len(text.split()) < 40:
        return text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary_sentences = summarizer(parser.document, sentence_count)
    return " ".join(str(s) for s in summary_sentences)

# --- Extract article text from a page ---
def extract_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")

        # remove junk
        for s in soup(["script", "style", "header", "footer", "nav", "aside"]):
            s.decompose()

        article_tag = soup.find("article")
        if article_tag:
            text = article_tag.get_text(separator=" ")
        else:
            ps = [p.get_text() for p in soup.find_all("p")]
            text = " ".join(p for p in ps if len(p.strip()) > 50)

        text = re.sub(r"\s+", " ", text).strip()
        return text
    except Exception:
        return ""

# --- Search DuckDuckGo HTML endpoint (no JS) ---
def get_top_result_link(query):
    search_url = "https://html.duckduckgo.com/html/"
    params = {"q": query}
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.post(search_url, data=params, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")

    # Find first real link
    for a in soup.select("a.result__a"):
        href = a.get("href")
        if href and href.startswith("http") and "duckduckgo.com" not in href:
            return href
    return None

# --- Main function ---
def get_brief_summary(query):
    speak_safe(f"Searching for: {query}")
    top_link = get_top_result_link(query)

    if not top_link:
        speak_safe(" No result found.")
        return None

    
    text = extract_text(top_link)

    if not text:
        speak_safe("Could not extract text.")
        return None

    summary = summarize_text(text, sentence_count=2)
    speak_safe(summary)
    
    


