import requests
import os

#calling edamam api and saving the search results into "data.txt"
'''
url = "https://api.edamam.com/api/recipes/v2?type=public&app_id=b67d3b8c&app_key=0e985ceeeb7bcc4f7d5963fe118bf7e7"
querystring = {"q":"chicken","random":"false", "field":["ingredients"],"count":1.0}

response = requests.request("GET", url, params=querystring)
#print(response.text)

with open('data.txt', 'w') as file:
    file.write(response.text)
file.close()
'''

#opening "data.txt" refine outputs into usable dictionaries
#'''
file = open('data.txt', 'rt')

file = file.read()
fileOutput = file.split(',')
webOutput = []
for i in fileOutput:
    if "https" in i:
        webOutput.append(i)

for i in webOutput:
    print("\n"+i)
#'''