from email import charset
import json, ssl
import urllib.request
from Beer import Beer
import json
import os
from pathlib import Path
import string

def getWord():
    # This is discouraged but it will avoid certificate validation (prevents error)
    # This is the URL from which we will request the data
    beerURL = "https://random-data-api.com/api/beer/random_beer"
 
    # Loop over JSON items and Deserialize them into python objects
    req = urllib.request.Request(beerURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    # Deserialize 
    current_beer:Beer = Beer(**requestData)
    current_beer.name
    return current_beer.name
steps = ["""
  -----
|  |   
|      
|      
|      
|      
=========
""", """
  -----
|  |   
|  😢   
|      
|      
|      
=========
""", """
  -----
|  |   
|  😢   
|  |   
|      
|      
=========
""", """
  -----
|  |  
|  😢   
| /|   
|      
|      
=========
""", """
  -----
|  |   
|  😢   
| /|\  
|      
|      
=========
""", """
  -----
|  |   
|  😢   
| /|\  
| /    
|      
=========
""", """
  -----
|  |   
|  😢   
| /|\  
| / \  
|      
=========
"""]


word = getWord()
letters = list(string.ascii_lowercase)
lettersInWord = list(word)
lettersNotInWord = []

for r in letters:
    if r not in lettersInWord:
        lettersInWord.append(r)

print(steps[0])
guess = []
for i in range(len(word)):
    if i != " ":
        guess.append("_")
    else:
        guess.append("   ")

#print("_ "*len(word))

print(len(word)*" _")
print(word)