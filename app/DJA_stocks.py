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

while range_answer == "Y":
    start = "Pick a start date (yyyy/mm/dd): "
    start_date = input(start)
    end = "Pick an end date (yyyy/mm/dd): "
    end_date = input(end)
    if end_date < start_date:
        print("Invalid input. Please try again.")
    else:
        break

# user_range = data.DataReader(selected, source, start_date, end_date)
# daily_closing_range = user_range.ix["Close"].round(2)



# if range_answer == "Y":
#     start = "Pick a start date (yyyy/mm/dd): "
#     end = "Pick an end date (yyyy/mm/dd): "
#     start_date = input(start)
#     end_date = input(end)
#     user_range = data.DataReader(selected, source, start_date, end_date)
#     daily_closing_range = user_range.ix["Close"].round(2)

if range_answer == "N":
    start = "Pick a date (yyyy/mm/dd): "
    start_date = input(start)
    end_date = start_date
    user_range = data.DataReader(selected, source, start_date, end_date)
    daily_closing_range = user_range.ix["Close"].round(2)
else:
    print("Invalid input. Please try again.")


# elif range_answer == "N":
#     start = "Pick a date (yyyy/mm/dd): "
#     start_date = input(start)
#     end_date = start_date
#     user_range = data.DataReader(selected, source, start_date, end_date)
#     daily_closing_range = user_range.ix["Close"].round(2)
# else:
#     print("Invalid input. Please try again.")

user_range = data.DataReader(selected, source, start_date, end_date)
daily_closing_range = user_range.ix["Close"].round(2)
print(daily_closing_range)

df = pd.DataFrame(daily_closing_range)
sort_data = df.sort_index(axis=0, ascending=True)

x = sort_data.pct_change()
x.ix["Cumulative"] = ((x+1).cumprod()-1).iloc[-1]
percents = x.ix["Cumulative"].map('{:,.2%}'.format)

print("")

if end_date != start_date:
    print(pd.DataFrame(percents))
else:
    pass

filename = 'my_data.csv'
df.to_csv(filename, index=True)

if end_date != start_date:
    with open('my_data.csv', 'a') as file:
        percents.to_csv(file, header=False)
else:
    pass
