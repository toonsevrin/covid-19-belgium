import requests
import matplotlib.pyplot as plt
import numpy as np
import datetime

country_code = "BE"
host = "https://coronavirus-tracker-api.herokuapp.com"
start_date = datetime.datetime(2020, 3, 1)

def get_confirmed(data, country_code):
    for loc in data["confirmed"]["locations"]:
        if loc['country_code'] == country_code:
            return loc
    return None
    
def sorted_dates(history_dates):
    dates = []
    for date in history_dates:
        s = date.split("/")
        dt = datetime.datetime(2020, int(s[0]), int(s[1]))
        if dt >= start_date:
            dates.append(dt)
    dates.sort()
    date_strings = []
    for date in dates:
        date_strings.append(str(date.month) + "/" + str(date.day) + "/20")
    return date_strings

# Fetch the date from the api and generate plot
r = requests.get(host + "/all")
data = r.json()
loc = get_confirmed(data, country_code)

keys = []
values = []

history_dates = list(loc["history"].keys())
sorted_dates = sorted_dates(history_dates)
for date in sorted_dates:
    keys.append(date)
    values.append(loc["history"][date])

plt.plot(keys, values, marker=".")
plt.show()
