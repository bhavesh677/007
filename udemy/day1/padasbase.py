import time
import os
import pandas

while True:
    if os.path.exists("file/temps_today.csv"):
        data=pandas.read_csv("file/temps_today.csv")
        #print(data.mean())
        print(data.mean()["st1"])
    else:
        print("file doesnt exists")
    time.sleep(5)