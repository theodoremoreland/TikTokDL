# Native
import re

def sanitizeLinks():
    links = []
    with open("./data/links.txt") as txt:
        for line in txt.readlines():
            try:
                line = re.search(r'(?<=").+(?=")', line).group()
            except:
                continue
            links.append(line)
    return links