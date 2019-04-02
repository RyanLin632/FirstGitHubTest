import io
import requests
import datetime
import pandas as pd
import time
import matplotlib.pyplot as plt


def allStock():
    url = "https://finance.yahoo.com/world-indices/"
    response = requests.get(url)
    f = io.StringIO(response.text)
    dfs = pd.read_html(f)
    index = dfs[0]
    return index


def crawl_price(stock_id):
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + \
        "?period1=0&period2=" + \
        str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"

    response = requests.post(url)

    f = io.StringIO(response.text)
    df = pd.read_csv(f, index_col='Date', parse_dates=['Date'])

    return df


def showPlot():
    world_index = allStock()
    world_index_history = {}
    for symbol, name in zip(world_index['Symbol'], world_index['Name']):
        world_index_history[name] = crawl_price(symbol)

    plt.rcParams['figure.figsize'] = (16, 9)
    plt.style.use('ggplot')
    for name, history in world_index_history.items():
        history.Close.plot()


showPlot()
