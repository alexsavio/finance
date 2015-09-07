#------------------------------------------------------------------------------
#Authors:
# Alexandre Manhaes Savio <alexsavio@gmail.com>
#
# BSD 3-Clause License
#
# 2015, Alexandre Manhaes Savio
# Use this at your own risk!
#------------------------------------------------------------------------------

from   collections import OrderedDict

import pandas    as pd
import numpy     as np

from   ipy_table import make_table, apply_theme


def stock_summary(stock_values, value_name='Close'):
    month_avg   = stock_values['SMA 30'][-1]
    last_value  = stock_values[value_name][-1]
    last_date   = pd.to_datetime(str(np.array(stock_values.index)[-1])).strftime('%d/%m/%Y')
    last_10msma = stock_values['SMA 300'][-1]
    action      = 'buy' if month_avg > last_10msma else 'sell'

    twod = lambda x: '{:.2f}'.format(x)

    stock_data = OrderedDict([('Action', action),
                              ('Monthly average price', twod(month_avg)),
                              ('Last close value', twod(last_value)),
                              ('Last close date', last_date),
                              ('Last 10m-SMA', twod(last_10msma)),])

    return stock_data


def vertical_table(adict):
    """ Use ipy_table to create a table for the ipynb.
    The `adict` keys are headers on top and the values are vertical content.
    """
    tab_data = [list(adict.keys())]
    tab_data.append(list(adict.values()))

    tab = make_table(tab_data)
    tab.apply_theme('basic')
    return tab
    