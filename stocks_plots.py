#------------------------------------------------------------------------------
#Authors:
# Alexandre Manhaes Savio <alexsavio@gmail.com>
#
# BSD 3-Clause License
#
# 2015, Alexandre Manhaes Savio
# Use this at your own risk!
#------------------------------------------------------------------------------

import numpy as np

from   bokeh.plotting import figure #show, output_file, vplot, hplot
from   bokeh.models   import HoverTool, PrintfTickFormatter


line_style = {'line_width': 2,
              'line_join':'round',
              'line_cap': 'round'}


def stock_value_history(stock_values, value_name='Close'):
    """ Create a Bokeh plot for a historic analysis of the values of the stock.

    Parameters
    ----------
    stock_values: pandas.DataFrame
        Stock historic data from pandas_datareader
    
    Returns
    -------
    p: Bokeh.figure
    """
    ticker = stock_values.name
    dates  = stock_values.index
    
    # hover tool
    phover = HoverTool(tooltips=[("price", "$y"),])

    # plot
    p = figure(x_axis_type = "datetime", tools=["pan,wheel_zoom,box_zoom,reset,resize", phover])

    p.title = "{} Closing Prices".format(ticker)
    p.title_text_font_size = '12'
    p.title_text_font_style = 'bold'

    # x axis
    p.xaxis.axis_label = 'Date'
    p.xaxis.axis_label_text_font_size = '9'

    # y axis
    p.yaxis.axis_label = 'Price (US$)'
    p.yaxis.axis_label_text_font_size = '9'

    line1_name = value_name
    p.line(np.array(dates, 'M64'), stock_values[value_name], legend=value_name,
            color='#182b8b', **line_style)

    line1_name = 'SMA 30'
    p.line(np.array(stock_values.index, 'M64'), stock_values[line1_name], legend=line1_name,
            color='#5477a0', **line_style)

    line2_name = 'SMA 100'
    p.line(np.array(stock_values.index, 'M64'), stock_values[line2_name], legend=line2_name,
            color='#dfbd4d', **line_style)

    line3_name = 'SMA 300'
    p.line(np.array(stock_values.index, 'M64'), stock_values[line3_name], legend=line3_name,
            color='#df1b06', **line_style)

    # set plot style
    p.plot_width  = 800
    p.plot_height = 300
    p.grid.grid_line_alpha=0.3

    # set grid
    # change just some things about the x-grid
    p.xgrid.grid_line_color = None

    # change just some things about the y-grid
    p.ygrid.grid_line_alpha = 0.5
    p.ygrid.grid_line_dash = [6, 4]

    # legend
    p.legend.orientation = "bottom_left"
    p.legend.label_text_font_size = '3'
    
    return p


def stock_volume_history(stock_values):
    """ Create a Bokeh plot for a historic analysis of the transactions volume of the stock.

    Parameters
    ----------
    stock_values: pandas.DataFrame
        Stock historic data from pandas_datareader
    
    Returns
    -------
    p: Bokeh.figure
    """
    ticker = stock_values.name
    dates  = stock_values.index
    
    # stock volume plot   
    p2hover = HoverTool(tooltips=[("volume", "$y"),])

    p = figure(x_axis_type = "datetime")

    p.title = "{} Daily Volume".format(ticker)
    p.title_text_font_size = '12'
    p.title_text_font_style = 'bold'

    # x axis
    p.xaxis.axis_label = 'Date'
    p.xaxis.axis_label_text_font_size = '9'

    # y axis
    p.yaxis.axis_label = 'Kilo Transactions'
    p.yaxis.axis_label_text_font_size = '9'
    p.yaxis[0].formatter = PrintfTickFormatter(format="%3d")

    p.quad(top=stock_values['Volume'], bottom=0, left=dates, right=dates,
            fill_color="#036564", line_color="#033649")

    p.line(np.array(dates, 'M64'), stock_values['Volume 30'],
            color='#dfbd4d', **line_style)

    p.line(np.array(dates, 'M64'), stock_values['Volume 300'],
            color='#df1b06', **line_style)

    # set plot style
    p.plot_width  = 800
    p.plot_height = 200
    p.grid.grid_line_alpha=0.3

    # set grid
    # change just some things about the x-grid
    p.xgrid.grid_line_color = None

    # change just some things about the y-grid
    p.ygrid.grid_line_alpha = 0.5
    p.ygrid.grid_line_dash = [6, 4]

    return p