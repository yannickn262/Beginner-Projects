import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))
userWord = input("Enter a word to be defined: ")

def findWord(word):
    #creates case insensitivity
    word = word.lower()
    if word in data:
        return data[word]
    elif len 
        #prints the word that closest matches the invalid user input
        closeMatches = get_close_matches(word, data.keys())[0]
        if(closeMatches != "")
            print("Did you mean " + str(closeMatches) + "?")
    else:
        print("Not a valid word, try again! ")

print(findWord(userWord))
