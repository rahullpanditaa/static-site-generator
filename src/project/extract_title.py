import re

def extract_title(md: str):
    if matches := re.search(r"^# (.+)", md, re.MULTILINE):
        return matches.group(1).strip()
    raise ValueError("Error: No h1 header in markdown")
