import calcData

def getStocks(base):
    stocks = []
    pref = input("Enter a name of a stock you want to see analysis for (q to exit): ")
    if (pref != 'q') and (pref not in base):
        stocks.append(pref)
    while (pref.lower() != "q"):
        pref = input("Enter a name of a stock you want to see analysis for (q to exit): ")
        if (pref != 'q') and (pref not in base):
            stocks.append(pref)
    return stocks



