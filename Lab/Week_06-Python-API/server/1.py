from xlwt import *
import requests
import json

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

# ### 1a
# output to console
# print(data)

# ### 1b
# output to console
# for car in data["cars"]:
# print(car)

# ### 1c
# save this to a file
filename = 'cars.json'
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ### 1d
# write to excel file
w = Workbook()
ws = w.add_sheet('cars')

row = 0  # note semicolon here!
ws.write(row, 0, "reg")
ws.write(row, 1, "make")
ws.write(row, 2, "model")
ws.write(row, 3, "price")
row += 1

for car in data["cars"]:
    ws.write(row, 0, car["reg"])
    ws.write(row, 1, car["make"])
    ws.write(row, 2, car["model"])
    ws.write(row, 3, car["price"])
    row += 1

w.save('cars.xls')
