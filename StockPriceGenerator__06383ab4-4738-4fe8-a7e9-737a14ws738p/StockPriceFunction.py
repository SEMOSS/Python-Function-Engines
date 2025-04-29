

import json
import urllib.request
import requests

from gaas_gpt_model import ModelEngine




def get_stock_price(api_key, company_name, start_date, end_date , insight_id):
    # Use Polygon's API to fetch the ticker symbol dynamically
    model = ModelEngine(engine_id = "4801422a-5c62-421e-a00c-05c6a9e15de8", insight_id = insight_id)
    ticker_url = f"https://api.polygon.io/v3/reference/tickers"
    ticker_params = {
        'search': company_name,
        'active': 'true',
        'apiKey': api_key
    }
    try:
        ticker_response = requests.get(ticker_url, params=ticker_params)
    except requests.exceptions.RequestException as e:
        return "Network error"
    if ticker_response.status_code == 200:
        ticker_data = ticker_response.json()
        if 'results' in ticker_data and len(ticker_data['results']) > 0:
            ticker_symbol = ticker_data['results'][0]['ticker']
        else:
            return f"Error: Could not find ticker symbol for {company_name}"
    else:
        return f"Error: {ticker_response.status_code} - {ticker_response.text}"

    # Fetch stock price data using the ticker symbol
    stock_url = f"https://api.polygon.io/v2/aggs/ticker/{ticker_symbol}/range/1/day/{start_date}/{end_date}"
    stock_params = {'apiKey': api_key}
    stock_response = requests.get(stock_url, params=stock_params)
    if stock_response.status_code == 200:
        stock_data = stock_response.json()
        return stock_data
    else:
        return f"Error: {stock_response.status_code} - {stock_response.text}"


