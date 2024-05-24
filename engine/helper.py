import re


def extract_yt_term(command):
    # Regex to find song name 
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    # if match found return song name
    return match.group(1) if match else None