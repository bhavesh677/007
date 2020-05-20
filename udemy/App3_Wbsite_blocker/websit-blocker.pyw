import time
from datetime import datetime as dt

temp_path = r"C:\Users\praz1\007\udemy\App3_Wbsite_blocker\hosts"
host_path = "C:\WINDOWS\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","web.whatsapp.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours...")
        with open(host_path,"+r") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else :
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun hours...")
        with open(host_path,"+r") as file:
            content = file.readlines() #each line will read as item of list each item is str
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
    


