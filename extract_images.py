import base64
from bs4 import BeautifulSoup

# open your html file
with open("index.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

i = 1

for img in soup.find_all("img"):
    src = img.get("src")

    if src and "base64," in src:
        data = src.split("base64,")[1]
        img_data = base64.b64decode(data)

        filename = f"image{i}.jpg"

        with open(filename, "wb") as f:
            f.write(img_data)

        img["src"] = filename
        i += 1

# save new html
with open("index_new.html", "w") as f:
    f.write(str(soup))