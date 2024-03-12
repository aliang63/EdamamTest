import requests
import os

#calling edamam api and saving the search results into "data.txt"
app_key = '0e985ceeeb7bcc4f7d5963fe118bf7e7'
app_id = 'b67d3b8c'

def initializeAPI(id,key):
    url = ('https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}').format(app_id = id,app_key = key)
    return url

def requestRecipe(search, parameters = [], apiURL = ''):
    def writeResults(results, file = 'data.txt'):
        with open(file, 'w') as f:
            f.write(results)
        f.close()
    
    query = {"q":search, "field":parameters}
    queryResults = requests.request("GET", apiURL, params=query).text

    writeResults(queryResults)

    

url = initializeAPI(app_id,app_key)
file = requestRecipe('chicken', ['ingredientLines'], url)


file = open('data.txt', 'rt')

file = file.read()
fileOutput = file.split(',')
webOutput = []
for i in fileOutput:
    if "https" in i:
        webOutput.append(i)

for i in webOutput:
    print("\n"+i)