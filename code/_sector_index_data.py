'''
make index - name relation table
only for kospi, kosdaq
'''
import time
import pandas as pd
from utils import make_csv, get_index, get_name


def main():
    kospi, kosdaq = get_index()
    
    kospi_df = pd.DataFrame({
            'index': kospi,
            'name': get_name(kospi)
        })

    kosdaq_df = pd.DataFrame({
            'index': kosdaq,
            'name': get_name(kosdaq)
        })

    df = pd.concat([kospi_df, kosdaq_df])
    make_csv(df, 'sector_index_')


if __name__ == "__main__":
    main()




