# seeds/stocks.py (use the updated get_stock_price function)
# from app.models import db, Stock, environment, SCHEMA
# from sqlalchemy.sql import text
# from app.api.alpha_vantage_client import get_stock_price
# import yfinance as yf

# def seed_stocks():
#     stock_symbols = ['AAPL', 'GOOGL', 'MSFT']
#     stocks = []

#     for symbol in stock_symbols:
#         ticker = yf.Ticker(symbol)
#         stock_info = ticker.info
#         print(f"Fetching data for {symbol}: {stock_info}")  # Debug print

#         # Try multiple keys to get the current price
#         current_price = stock_info.get('regularMarketPrice', None)
#         if current_price is None:
#             current_price = stock_info.get('ask', None)
#         if current_price is None:
#             current_price = stock_info.get('bid', None)

#         if current_price is None:
#             print(f"Could not fetch current price for {symbol}, setting to 0")
#             current_price = 0  # Set a default value to avoid errors

#         stocks.append(
#             Stock(
#                 symbol=symbol,
#                 name=stock_info.get('shortName', f"{symbol} Inc."),
#                 current_price=current_price,
#                 market_cap=stock_info.get('marketCap', 0),
#                 pe_ratio=stock_info.get('trailingPE', 0),
#                 dividend_yield=stock_info.get('dividendYield', 0)
#             )
#         )

#     db.session.bulk_save_objects(stocks)
#     db.session.commit()


# def undo_stocks():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.stocks RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM stocks"))

#     db.session.commit()

# seeds/stocks.py

from app.models import db, Stock, environment, SCHEMA
from sqlalchemy.sql import text
from finnhub_client import get_stock_price, get_historical_prices

def seed_stocks():
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT']
    stocks = []

    for symbol in stock_symbols:
        stock_info = get_stock_price(symbol)
        if stock_info:
            stocks.append(
                Stock(
                    symbol=stock_info['symbol'],
                    name=stock_info['name'],
                    current_price=stock_info['price'],
                    market_cap=stock_info['market_cap'],
                    pe_ratio=stock_info['pe_ratio'],
                    dividend_yield=stock_info['dividend_yield']
                )
            )

    db.session.bulk_save_objects(stocks)
    db.session.commit()

def seed_historical_prices():
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT']
    historical_prices = []

    for symbol in stock_symbols:
        prices = get_historical_prices(symbol)
        if prices:
            for date, price_data in prices.items():
                historical_prices.append(
                    HistoricalPrice(
                        stock_symbol=symbol,
                        date=date,
                        open_price=price_data['1. open'],
                        close_price=price_data['4. close'],
                        high_price=price_data['2. high'],
                        low_price=price_data['3. low'],
                        volume=price_data['5. volume']
                    )
                )

    db.session.bulk_save_objects(historical_prices)
    db.session.commit()

def undo_stocks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.stocks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM stocks"))

    db.session.commit()

def undo_historical_prices():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.historical_prices RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM historical_prices"))

    db.session.commit()
