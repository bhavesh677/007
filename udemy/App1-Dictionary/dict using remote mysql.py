import mysql.connector
import difflib
from difflib import get_close_matches


con=mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

def find(w):
    w = w.lower()
    
    
    query = cursor.execute("SELECT Expression FROM Dictionary")
    
    out = cursor.fetchall()
    
    results=[]
    for j in out:
        results.append(j[0])
    
    
    if w in results:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" %w)
        return cursor.fetchall()
    
    elif w.title() in results:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" %w.title())
        return cursor.fetchall()
    
    elif w.upper() in results:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" %w.upper())
        return cursor.fetchall()
    
    elif len(get_close_matches(w,results)) > 0:
        
        a=get_close_matches(w,results)[0]
        
        t = input("Did you mean %s ? Enter Y if yes or N if no: "%a)
        if t == "y" or t == "Y":
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" %a)
            return cursor.fetchall()
        elif t == "n" or t == "N":
            return "please try again"
        else:
            return "Invalid entry"
    else:
        return "The word doesn't exist. Please try again"




word=input("Enter the word: ")
result=find(word)



if isinstance(result,list):
    for i in result:
        print(i[0])
else:
    print(result)


