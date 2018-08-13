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
        #if there is more than one close match
    elif len(get_close_matches(word, data.keys())) > 0:
        closeMatches = get_close_matches(word, data.keys())[0]
        print("Did you mean " + str(closeMatches) + "?")
        userErrorInput = input("Type Y for Yes and N for No: ")
        userErrorInput = userErrorInput.lower()
        if userErrorInput == "y":
            return data[closeMatches]
        #prints the word that closest matches the invalid user input
    else:
        print("Not a valid word!")

print(findWord(userWord))
