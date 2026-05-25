import re
from pathlib import Path

for file in Path("docs").rglob("*.md"):
    text = file.read_text(encoding="utf-8")
    text = re.sub(r"~~(.*?)~~",r"<del>\1</del>",text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)",r"<a href=\2 >\1</a>",text)
    text = re.sub(r"!\[image\]\((.*?)\)",r"<img src=\1 />",text)
    file.write_text(text, encoding="utf-8")

# 
# text = re.sub(r':heavy_plus_sign:',r'&#10133;',text)