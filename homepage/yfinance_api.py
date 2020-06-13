import yfinance as yf
from yahooquery import Ticker

# return marketcap of a company


def get_marketcap(Ticker):
    return yf.Ticker(Ticker).info['marketCap'] / 1000000

# example
# print(get_marketcap("ADMS"))
# print(yf.Ticker('ADMS').info)


def get_EV(symbol):
    return Ticker(symbol).key_stats[symbol]['enterpriseValue'] / 1000000

# print(yf.Ticker('ADMS').financials)


# get reported amount of cash of the company
def get_cash(ticker):
    try:
        return Ticker(ticker).balance_sheet('q')['CashCashEquivalentsAndShortTermInvestments'].iloc[-1] / 1000000
    except:
        return None
