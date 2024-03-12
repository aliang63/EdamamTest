import requests
import os

#calling edamam api and saving the search results into "data.txt"
app_key = '0e985ceeeb7bcc4f7d5963fe118bf7e7'
app_id = 'b67d3b8c'

def initializeAPI(id,key):
    url = ('https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}').format(app_id = id,app_key = key)
    return url

#parameters [uri, label, image, images, source, url, shareAs, yield, dietLabels, healthlabels, cautions, ingredientLines, ingredients, calories, glycemicIndex, inflammatoryIndex, totalCO2EmissionsClass, totalWeight, totalTime, cuisineType, mealType, dishType, totalNutrients, totalDaily, digest, externalId]
def requestRecipe(search, parameters = [], apiURL = ''):
    
    # writes the results of the search into data.txt to avoid calling api over and over again
    def writeResults(results, file = 'data.txt'):
        with open(file, 'w') as f: #opens the file with write functionality
            f.write(results)
        f.close()
    
    #initializing and requesting query
    query = {"q":search, "field":parameters}
    queryResults = requests.request("GET", apiURL, params=query).text

    #calls write function to finalize results
    writeResults(queryResults)

    

url = initializeAPI(app_id,app_key) # initializes the url using id and key
#requestRecipe('chicken', ['ingredientLines'], url) #searches for chicken recipies, with the list of ingredients as one of the parameters


#opens the saved data file with read function
file = open('data.txt', 'rt')

file = file.read()
fileOutput = file.split(',')
webOutput = []

#finds all results with https in the string, and adds to list of outputs
for i in fileOutput:
    if "https" in i:
        webOutput.append(i)

#prints outputs
for i in webOutput:
    print("\n"+i)