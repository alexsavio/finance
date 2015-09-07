#------------------------------------------------------------------------------
#Authors:
# Alexandre Manhaes Savio <alexsavio@gmail.com>
#
# BSD 3-Clause License
#
# 2015, Alexandre Manhaes Savio
# Use this at your own risk!
#------------------------------------------------------------------------------

import pandas                 as pd
import pandas_datareader.data as web


def get_yahoo_stocks_data(ticker, start_day, end_day, voi='Close'):
    """ Return the Yahoo Finance data for the ticker from `start_day` and `end_day`.

    Include:
       - the Simple Moving Average (SMA) for 30, 100 and 300 days for `voi` field,
       - the SMA for 30 and 300 days for Volume field and
       - the ticker of the stock in the `name` attribute of the DataFrame.
    
    Parameters
    ----------
    ticker: str
        The stock ticker
    
    start_day: str
        The date in format: yyyy-mm-dd

    end_day: str
        The date in format: yyyy-mm-dd

    Returns
    -------
    stock_values: pandas.DataFrame
    """
    stock_values = web.DataReader(ticker, 'yahoo', start_day, end_day)
    #stock_values = wb.get_data_yahoo(ticker, start_day, end_day)

    # percent change
    #stock_pc = stock_values.pct_change(periods=1, fill_method='pad', limit=None, freq=None)

    # stock_smas
    stock_values['SMA 30' ] = pd.stats.moments.rolling_mean(stock_values[voi],  30)
    stock_values['SMA 100'] = pd.stats.moments.rolling_mean(stock_values[voi], 100)
    stock_values['SMA 300'] = pd.stats.moments.rolling_mean(stock_values[voi], 300)

    # average volume
    stock_values['Volume 30' ] = pd.stats.moments.rolling_mean(stock_values['Volume'],   30)
    stock_values['Volume 300'] = pd.stats.moments.rolling_mean(stock_values['Volume'],  300)

    stock_values.name = ticker
    
    return stock_values