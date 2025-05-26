import re

def clean_text(text):
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"[^A-Za-z\s]", "", text)
    return text.strip().lower()
