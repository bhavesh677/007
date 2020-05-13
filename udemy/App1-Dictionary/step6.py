import json
import difflib
from difflib import get_close_matches



data=json.load(open("data.json"))

def find(w):
    w = w.lower()
    
    if w in data.keys():
        return data[w]
    
    elif w.title() in data.keys():
        return data[w.title()]
    
    elif w.upper() in data.keys():
        return data[w.upper()]
    
    elif len(get_close_matches(w,data.keys())) > 0:
        
        a=get_close_matches(w,data.keys())[0]
        
        t = input("Did you mean %s ? Enter Y if yes or N if no: "%a)
        if t == "y" or t == "Y":
            return data[a]
        elif t == "n" or t == "N":
            return "please try again"
        else:
            return "Invalid entry"
    else:
        return "The word doesn't exist. Please try again"

word=input("Enter word: ")
output=find(word)

if isinstance(output,list):
    for i in output:
        print(i)
else:
    print(output)


