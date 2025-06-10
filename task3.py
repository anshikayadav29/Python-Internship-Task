import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string.strip()

with open("webpage_title.txt", "w", encoding="utf-8") as file:
    file.write(f"Title of {url}:\n{title}")