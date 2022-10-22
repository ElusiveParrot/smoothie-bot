import webbrowser
import requests
import time
from bs4 import BeautifulSoup


def open_link(url):
    webbrowser.open(url, new=0, autoraise=True)


URL = "https://www.chickensmoothie.com/"

while True:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    for a in soup.find_all('a', href=True):
        link = a['href']
        if "getgiveaway" in link:
            open_link("https://www.chickensmoothie.com" + link)
            time.sleep(21 * 60)
            break
