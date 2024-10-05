# feature_engineer.py
import pandas as pd

def calculate_moving_average(data, window=5):
    """Calculate simple moving average for given stock data."""
    return data['Close'].rolling(window=window).mean()

def calculate_bollinger_bands(data, window=20):
    """Calculate Bollinger Bands for stock data."""
    ma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    upper_band = ma + (std * 2)
    lower_band = ma - (std * 2)
    return ma, upper_band, lower_band

# Add more features as needed
