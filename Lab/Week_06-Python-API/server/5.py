# 4. Write a python program that deletes a car from the server using the API.

from xlwt import *
import requests
import json

url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()
# print(data) # for testing

# Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


# write to excel file
w = Workbook()
ws = w.add_sheet('githubusers')

row = 0
ws.write(row, 0, "login")
ws.write(row, 1, "id")
ws.write(row, 2, "node_id")
ws.write(row, 3, "avatar_url")
ws.write(row, 4, "url")
ws.write(row, 5, "html_url")
ws.write(row, 6, "followers_url")
ws.write(row, 7, "following_url")
ws.write(row, 8, "gists_url")
ws.write(row, 9, "starred_url")
ws.write(row, 10, "subscriptions_url")
ws.write(row, 11, "organizations_url")
ws.write(row, 12, "repos_url")
ws.write(row, 13, "events_url")
ws.write(row, 14, "received_events_url")
ws.write(row, 15, "type")
ws.write(row, 16, "site_admin")
row += 1

for user in data:
    ws.write(row, 0, user["login"])
    ws.write(row, 1, user["id"])
    ws.write(row, 2, user["node_id"])
    ws.write(row, 3, user["avatar_url"])
    ws.write(row, 4, user["url"])
    ws.write(row, 5, user["html_url"])
    ws.write(row, 6, user["followers_url"])
    ws.write(row, 7, user["following_url"])
    ws.write(row, 8, user["gists_url"])
    ws.write(row, 9, user["starred_url"])
    ws.write(row, 10, user["subscriptions_url"])
    ws.write(row, 11, user["organizations_url"])
    ws.write(row, 12, user["repos_url"])
    ws.write(row, 13, user["events_url"])
    ws.write(row, 14, user["received_events_url"])
    ws.write(row, 15, user["type"])
    ws.write(row, 16, user["site_admin"])
    row += 1

w.save('githubusers.xls')
