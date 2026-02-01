import nltk
import re
from nltk.corpus import stopwords

nltk.download("stopwords")

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", text)

    stop_words = set(stopwords.words("portuguese"))
    words = text.split()

    filtered = [w for w in words if w not in stop_words]

    return " ".join(filtered)
