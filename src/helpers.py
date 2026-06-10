import re

def extract_title(markdown: str) -> str:
    result = re.match(r'^# (.+)$', markdown, re.MULTILINE)
    if result is None:
        raise Exception("No title")

    return result.group(1).strip()
