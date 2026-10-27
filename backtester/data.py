import yfinance as yf
import pandas as pd

def load_prices(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)
    df.columns = df.columns.get_level_values(0)
    return df[["Close"]].dropna()

if __name__ == "__main__":
    print(load_prices("AAPL", "2018-01-01", "2025-12-31").tail())
