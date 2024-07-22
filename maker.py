import os
import re

def extract_image_links_from_markdown(markdown_text):
    pattern = r'!\[.*?\]\((.*?)\)'
    image_links = re.findall(pattern, markdown_text)
    return image_links

pths = []
names = []
for i, j, k in os.walk("posts/"):
    if not len(names):
        names = k
    for l in k:
        pths.append(os.path.join(i, l))

for i in range(0, len(pths)):
    r = ""
    names[i] = names[i].split(".md")[0].replace("~", "-").replace(" ", "")
    with open(pths[i], "r", encoding="utf-8") as f:
        r = f.read()
    for j in extract_image_links_from_markdown(r):
        r = r.replace(j, "post-images/%s" % j.replace("https://daoxi365.github.io/tech-blog//post-images/", ""))
    with open("after/%s.md" % names[i], "w", encoding="utf-8") as f:
        f.write("\n".join(r.splitlines()[9:len(r)-1]))
    print(i, names[i])
    
    
"""
x = ""
for i in names:
    j = i
    x += "- [%s](%s)\n" % (j, j)

with open("./_sidebar.md", "w", encoding="utf-8") as f:
    f.write(x)
"""
    
input()