# stockData.py
import yfinance as yf

import os
import pickle
import hashlib
import yfinance as yf

# This is relative to the path that the ipynb notebook is called from
CACHE_DIR = os.path.join(os.path.dirname(__file__), '../data/cache')

def create_cache_key(tickers, start_date, end_date):
    key = f"{tickers}_{start_date}_{end_date}"
    return hashlib.md5(key.encode()).hexdigest()

def save_to_cache(key, data):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    filepath = os.path.join(CACHE_DIR, f"{key}.pkl")
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)

def load_from_cache(key):
    filepath = os.path.join(CACHE_DIR, f"{key}.pkl")
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    return None

def get_stock_data(tickers, start_date, end_date):
    """
    Fetch historical stock data for given tickers within a specified date range.

    Uses a cache to avoid redundant data fetching.

    Parameters:
    ----------
    tickers : list of str
        A list of stock ticker symbols to fetch data for.
    start_date : str
        The start date for fetching data in 'YYYY-MM-DD' format.
    end_date : str
        The end date for fetching data in 'YYYY-MM-DD' format.

    Returns:
    -------
    dict
        A dictionary where keys are ticker symbols and values are DataFrames
        containing the historical stock data for the respective ticker.

    Examples:
    ---------
    >>> stock_data = get_stock_data(['AAPL', 'GOOGL'], '2023-01-01', '2023-01-31')
    >>> print(stock_data['AAPL'].head())
    """
    cache_key = create_cache_key(tickers, start_date, end_date)
    
    # Try loading data from cache
    cached_data = load_from_cache(cache_key)
    if cached_data:
        print(f"Loaded data from cache for tickers: {tickers}")
        return cached_data

    # If not cached, fetch data from yfinance
    stock_data = {}
    for ticker in tickers:
        data = yf.download(ticker, start=start_date, end=end_date)
        stock_data[ticker] = data

    # Save the fetched data to cache for future use
    save_to_cache(cache_key, stock_data)
    return stock_data


