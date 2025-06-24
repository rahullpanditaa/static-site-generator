import re

def extract_title(markdown):
    if matches := re.search(r"# (.+)", markdown):
        return matches.group(1).strip()
    else:
        raise BaseException("No title found")