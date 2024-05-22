import json

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()
# 必要に応じてデータの整形を行う
