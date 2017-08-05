from pandas_datareader import data
import datetime
from datetime import date, timedelta
import pandas as pd

tickers = ["MMM", "AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "KO", "DIS", "DD",
"XOM", "GE", "GS", "HD", "IBM", "INTC", "JNJ", "JPM", "MCD", "MRK", "MSFT", "NKE",
"PFE", "PG", "TRV", "UTX", "UNH", "VZ", "V", "WMT"
]

selected = ["^DJI"]
source = 'yahoo'

start_date = 0
end_date  = 1

print("------------------------------------------------------------------")
print("Stock Quote Appication")
print("------------------------------------------------------------------")
print("Welome!")
print("Choose your tickers, receive quotes and returns, and download to a csv file!")
print("")
print("You will be prompted for your desired Dow Jones stock tickers.")
print("When your are finished type 'DONE'.")
print("You will then be asked to choose a specific date or range of dates.")
print("")
print("Your data and returns will be displayed and shown with the Dow Jones.")
print("Your information request will be written to as csv file for your convenience.")
print("------------------------------------------------------------------")

for x in tickers:
    user_input = "Please choose some Dow Jones tickers (e.g., KO, GE, PG, V): "
    user_op = input(user_input).upper()
    if user_op in tickers:
        selected.append(user_op)
        print("Input accepted!")
    elif user_op == 'DONE':
        user_date = "Are you using a date range? (Y/N): "
        date_put = input(user_date).upper()
        range_answer = date_put
        break
    else:
        print("Invalid input. Please try again.")
