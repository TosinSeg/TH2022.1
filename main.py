from zipapp import create_archive
import requests
import numpy
import calcData
import users
from flask import Flask, render_template
import operator

base_stocks = ['aapl', 'tsla', 'googl', 'doge-usd']
stocks = users.getStocks(base_stocks)
vals = calcData.GenerateSortedData(stocks)
vals2 = calcData.GenerateSortedData(base_stocks)
vals2.update(vals)
for key in vals2:
    vals2[key] = calcData.Probability(vals2[key], 1.1)
vals2 = (sorted(vals2.items(), key =
             lambda kv:(kv[1], kv[0])))  
vals2 = reversed(vals2)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data = vals2)

if __name__ == '__main__':
    app.run(debug=True)



