import yfinance as yf
from yahooquery import Ticker

# return marketcap of a company


def get_marketcap(Ticker):
    return yf.Ticker(Ticker).info['marketCap'] / 1000000

# example
# print(get_marketcap("ADMS"))
# print(yf.Ticker('ADMS').info)


def get_EV(Ticker):
    return yf.Ticker(Ticker).info['enterpriseValue'] / 1000000

# print(yf.Ticker('ADMS').financials)


# get reported amount of cash of the company
def get_cash(ticker):
    return [Ticker(ticker).balance_sheet('q')['asOfDate'].iloc[-1], Ticker(ticker).balance_sheet('q')['CashCashEquivalentsAndShortTermInvestments'].iloc[-1] / 1000000]


# print(Ticker('ADMS').balance_sheet('q').iloc[-1])
