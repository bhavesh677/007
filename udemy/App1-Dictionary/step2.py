import json

data=json.load(open("data.json"))

def find(w):
    if w in data.keys():
        return data[w]
    else:
        return "not found"

word=input("Enter a word: ")
print(find(word))

