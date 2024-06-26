from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/api/data')
def api_data():
    data = load_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
