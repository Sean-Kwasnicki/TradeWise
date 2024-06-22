# finnhub_client.py

import os
from datetime import datetime, timedelta
import finnhub
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY')
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

def get_stock_price(symbol):
    try:
        stock_quote = finnhub_client.quote(symbol)
        stock_profile = finnhub_client.company_profile2(symbol=symbol)
        print(f"Fetched data for {symbol}: {stock_quote}")  # Debug print statement
        return {
            'symbol': symbol,
            'price': stock_quote['c'],  # Current price
            'name': stock_profile.get('name', symbol),  # Fetches the full name of the stock
            'market_cap': stock_profile.get('marketCapitalization', 0),
            'pe_ratio': stock_profile.get('peTTM', 0),
            'dividend_yield': stock_profile.get('dividendYield', 0)
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")  # Error handling
        return None

def get_historical_prices(symbol):
    try:
        now = datetime.utcnow()
        start_date = now - timedelta(days=5)
        end_timestamp = int(now.timestamp())
        start_timestamp = int(start_date.timestamp())
        
        historical_data = finnhub_client.stock_candles(symbol, 'D', start_timestamp, end_timestamp)
        
        if historical_data['s'] != 'ok':
            print(f"Error fetching historical data for {symbol}: {historical_data['s']}")
            return None

        formatted_data = {}
        for i in range(len(historical_data['t'])):
            date = datetime.utcfromtimestamp(historical_data['t'][i]).strftime('%Y-%m-%d')
            formatted_data[date] = {
                '1. open': historical_data['o'][i],
                '4. close': historical_data['c'][i],
                '2. high': historical_data['h'][i],
                '3. low': historical_data['l'][i],
                '5. volume': historical_data['v'][i]
            }

        return formatted_data
    except Exception as e:
        print(f"Error fetching historical prices for {symbol}: {e}")
        return None

# Test the functions
if __name__ == "__main__":
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    for symbol in symbols:
        print(get_stock_price(symbol))
        print(get_historical_prices(symbol))
