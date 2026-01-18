import os
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

SOLAR_STOCKS = ["FSLR", "SPWR", "SEDG", "ENPH", "CSIQ"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stocks')
def get_stocks():
    stocks_data = []
    if not API_KEY:
        for symbol in SOLAR_STOCKS:
            stocks_data.append({'symbol': symbol, 'price': 'N/A (No API Key)'})
        return jsonify(stocks_data)

    for symbol in SOLAR_STOCKS:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            quote = data.get('Global Quote')
            if quote and '05. price' in quote:
                price = float(quote['05. price'])
                stocks_data.append({'symbol': symbol, 'price': price})
            else:
                stocks_data.append({'symbol': symbol, 'price': 'N/A'})
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {symbol}: {e}")
            stocks_data.append({'symbol': symbol, 'price': 'Error'})
            
    return jsonify(stocks_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
