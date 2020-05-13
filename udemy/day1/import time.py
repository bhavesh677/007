'''import time
while True:
    with open("file/original.txt") as file:
        print(file.read())
        time.sleep(5)
'''

import time
import os

#print(os.path.exists("file/original.txt"))

if os.path.exists("file/original.txt"):
    with open("file/original.txt") as file:
        print(file.read())
else:
    print("file not found")



        



