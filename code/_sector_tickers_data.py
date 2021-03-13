'''
make sector - tickers dict
'''
import time
import pandas as pd
from pykrx import stock
from utils import make_csv, get_index


def get_sector_tickers_data():
    kospi, kosdaq = get_index()
    markets = kospi + kosdaq
    stocks = []
    
    for idx in markets:
        stocks.append(stock.get_index_portfolio_deposit_file(idx))
        time.sleep(0.5)

    df = pd.DataFrame({
        'index': markets,
        'stocks': stocks
    })
    
    make_csv(df, 'sector_tickers_')


if __name__ == "__main__":
    get_sector_tickers_data()
