# Native
import re


with open("./data/links.txt.example", "w") as example_file:
    with open("./data/links.txt", "r") as links:
        for line in links:
            line = re.sub(r'(?<=@).+?(?=/)', "username", line)
            line = re.sub(r'(?<=/video/).+(?=\?)', "videoID", line)
            example_file.write(line)
    