from flask import Flask, jsonify, render_template, request
import json
import os

app = Flask(__name__)
DATA_FILE = "market_data.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/currencies', methods=['GET'])
def get_currencies():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(list(data.keys()))
    return jsonify([])

@app.route('/api/cot-data', methods=['GET'])
def get_cot_data():
    currency = request.args.get('currency', 'USD').upper()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        rows = data.get(currency, [])
        return jsonify({
            "status": "success",
            "currency": currency,
            "data": rows
        })
    return jsonify({"status": "error", "message": "market_data.json not found", "data": []}), 404

if __name__ == '__main__':
    app.run(debug=True, port=7000)