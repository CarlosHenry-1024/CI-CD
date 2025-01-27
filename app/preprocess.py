import re

def clean_text(text):
    # 简单的文本清理逻辑
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower().strip()