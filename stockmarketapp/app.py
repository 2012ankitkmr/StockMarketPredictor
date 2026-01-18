from flask import Flask, jsonify, render_template
from .services.api_service import get_stock_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stocks')
def get_stocks():
    stocks_data = get_stock_data()
    return jsonify(stocks_data)

