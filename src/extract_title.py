def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith('#'):
            final_title = line.lstrip('#').strip()
            if final_title:
                return final_title
    return None
