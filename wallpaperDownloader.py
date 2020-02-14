import os
import urllib.request
import requests
from bs4 import BeautifulSoup

opener = urllib.request.URLopener()
opener.addheader("User-Agent", "whatever")

for i in range(101, 150):
    soup = BeautifulSoup(
        requests.get(f"https://hdqwalls.com/latest-wallpapers/page/{i + 1}").text,
        features="html.parser",
    )
    for wall_resp in soup.find_all("div", class_="wall-resp"):
        web_parser = BeautifulSoup(
            requests.get(
                "https://hdqwalls.com/"
                + "wallpaper/720x1280"
                + "-".join(wall_resp.a["href"].split("-")[:-1])
            ).text,
            features="html.parser",
        )
        img_url = web_parser.find("span", {"id": "c_download_btn"}).span.a["href"]
        opener.retrieve(
            img_url, f"./images/{wall_resp.a['href'][1:]}.jpg",
        )
        print(f"Downloaded {wall_resp.a['href'][1:]}")


# Optional to convert images to webp
os.chdir("./images/")
demo = os.listdir(path=".")

for file in demo:
    file_name_old = file.split(".").pop(0)
    file_name = " ".join(file_name_old.split("-")[:-1])
    os.system(f'cwebp {file} -o "{file_name.title()}".webp')
    print(f"Removing file {file}")
    os.remove(file)

