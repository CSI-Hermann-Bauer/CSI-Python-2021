from email import charset
import json, ssl
from tkinter import E
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
    name = current_beer.name.split()

    return name[0]

def printWord(word):
  x=0
  letters = list(string.ascii_lowercase)
  lettersInWord = list(word)
  lettersGuessed = []
  temp:str= ("_" * len(word))
  print(temp)
  #for letter in word:
  while True:
    letter = input("Input Guess: ")
    if letter not in letters:
      print("Please input letter.")
    elif letter in lettersInWord:
      for i in range(len(lettersInWord)):
        if letter == lettersInWord[i]:
          lettersGuessed.append(letter)
          temp = temp[:i] + lettersInWord[i] + temp[i + 1:]
          
          if temp==word:
            return("Game won!")
          else:
            print(temp)
            print("Letter in word")
            print(lettersGuessed)

      print(temp)

    elif letter in lettersGuessed:
      print("Already guessed that")
    else:
      print("Letter not in word")
      print(steps[x])
      x+=1
      lettersGuessed.append(letter)
      print(temp)
      print(lettersGuessed)
    if x>6:
      return 'Game Lost'
        



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

while True:
  word = getWord().lower()
  print(word)
  print(printWord(word))


