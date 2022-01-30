from hashlib import new
import numpy as np
import scipy.stats as stats
import users
import requests

def CleanData(data):
    news = []
    for i in range(len(data)):
        if data[i] is not None:
            news.append(data[i])
    return news

def CalcAvg(data):
    total = 0
    sum = 0
    for i in range(len(data)):
        if data[i] is not None:
            sum += data[i]
            total += 1
    return sum/total

def Deviation(data):
    new_data = []
    for i in range(len(data)):
        if data[i] is not None:
            new_data.append(data[i])
    return np.std(new_data)

def PrintData(data):
    for i in range(len(data)):
        print(data[i])
    return
    
def Zscores(data):
    new_data = []
    for i in range(len(data)):
        if data[i] is not None:
            new_data.append(data[i])
    return stats.zscore(new_data)

def Probability(data,percent):
    dev = Deviation(data)
    avg = CalcAvg(data)
    z = (percent - avg/dev)
    return stats.norm(0,1).cdf(z) * 100

def ProbRange(data, percent1, percent2):
    while percent1 >= percent2:
        print("The second percentage should be greater than the first. \n")
        percent1 = float(input("Enter the first(lower) percentage: "))
        percent2 = float(input("\nEnter the second(higher) percentage: \n"))
    dev = Deviation(data)
    avg = CalcAvg(data)
    z1 = (percent1 - avg)/dev
    z2 = (percent2 - avg)/dev
    res = stats.norm(0,1).cdf(z2) - stats.norm(0,1).cdf(z1)
    return float("{:.2f}".format(res))

def Change(data):
    gain = []
    loss = []
    for i in range(len(data)):
        if i == 0:
            continue
        else:
            change = (data[i]/data[i-1])
            if change >= 1:
                gain.append(change)
            else:
                loss.append(change)
    return CalcAvg(loss), CalcAvg(gain)

def RSI(data):
    loss, gain = Change(data)
    return 100 - (100/(1+(gain/loss)))

def GenerateSortedData(data):
    vals = {}
    for stock in data:
        symbol = stock
        url = "https://yh-finance.p.rapidapi.com/stock/v3/get-historical-data"

        querystring = {"symbol":symbol,"region":"US"}

        headers = {
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': "50de179b3dmshba15e5d0e44e4d3p169d7djsn21ed347daa51"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        strings = response.json()
        j = 0
        close_prices = []
        for i in range(len(strings["prices"])):
            try:
                if strings["prices"][i]['close'] is not None:
                    close_prices.append(strings["prices"][i]['close'])
            except:
                continue
        close_prices = CleanData(close_prices)
        vals[stock] = close_prices
    return vals
    RSI_list = {}
    for key in vals:
        RSI_list[key] = RSI(vals[key])

    return RSI_list

