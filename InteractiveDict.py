import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))
userWord = input("Enter a word to be defined: ")

def findWord(word):
    #creates case insensitivity
    word = word.lower()
    acronym = word.upper()
    properNoun = word.capitalize()
    if acronym in data:
        return data[acronym]
    if properNoun in data:
        return data[properNoun]
    if word in data:
        return data[word]
        #if there is more than one close match
    elif len(get_close_matches(word, data.keys())) > 0:
        closeMatches = get_close_matches(word, data.keys())[0]
        print("Did you mean " + str(closeMatches) + "?")
        userErrorInput = input("Type Y for Yes and N for No: ")
        userErrorInput = userErrorInput.lower()
        if userErrorInput == "y" or userErrorInput == "yes":
            return data[closeMatches]
        #prints the word that closest matches the invalid user input
    else:
        print("Not a valid word!")

output = findWord(userWord)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
