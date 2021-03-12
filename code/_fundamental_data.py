import time
import pandas as pd
from pykrx import stock
from utils import make_csv


def main():
    now = time.strftime('%Y%m%d', time.localtime(time.time()))
    df = stock.get_market_fundamental_by_ticker(now)
    df['ticker'] = df.index
    df = df[['ticker', 'EPS', 'PER', 'BPS', 'PBR', 'DPS', 'DIV']]
    make_csv(df, 'fundament_')


if __name__ == "__main__":
    main()