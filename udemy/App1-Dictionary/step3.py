import json

data=json.load(open("data.json"))

def find(w):
    w = w.lower()
    
    if w in data.keys():
        return data[w]
    else:
        return "The word doesn't exist. Please try again"

word=input("Enter a word: ")

print(find(word))


