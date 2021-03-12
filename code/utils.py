import time
import pandas as pd
from pykrx import stock


def make_csv(df, name):
    path = './data/'
    now = time.strftime('%Y_%m_%d', time.localtime(time.time()))
    df.to_csv(path + name + now + '.csv', encoding='euc-kr', index=False)


def get_index():
    kospi_index = stock.get_index_ticker_list(market='KOSPI')
    kosdaq_index = stock.get_index_ticker_list(market='KOSDAQ')
    time.sleep(1)
    return kospi_index, kosdaq_index


def get_name(index):
    name = []
    for idx in index:
        name.append(stock.get_index_ticker_name(idx))
        time.sleep(1)
    return name