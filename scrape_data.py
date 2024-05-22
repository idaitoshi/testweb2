import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

# スクレイピング対象のURL
urls = [
    "https://www.fresh-club.net/akb/",
    # 他のURL
]

def scrape_data():
    data = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # 例: タイトルと本文を抽出
            title = soup.find("h1").get_text()
            body = soup.find("div", class_="content").get_text()
            data.append({"url": url, "title": title, "body": body})
    return data

def save_data(data):
    # JSONファイルに保存
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 実行
data = scrape_data()
save_data(data)
