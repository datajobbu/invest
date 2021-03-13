import time
import pandas as pd
from pykrx import stock
from utils import make_csv


def get_fundamental_data():
    now = time.strftime('%Y%m%d', time.localtime(time.time()))
    kospi = stock.get_market_fundamental_by_ticker(now, market="KOSPI")
    kosdaq = stock.get_market_fundamental_by_ticker(now, market="KOSDAQ")
    
    df = pd.concat([kospi, kosdaq])
    df['ticker'] = df.index
    df = df[['ticker', 'EPS', 'PER', 'BPS', 'PBR', 'DPS', 'DIV']]
    make_csv(df, 'fundament_')


if __name__ == "__main__":
    get_fundamental_data()