import pyautogui as pg
from time import sleep

def start():
    sleep(1)
    pg.press("win")
    sleep(1)
    pg.typewrite("cmd")
    sleep(1)
    pg.press("enter")
    sleep(1)
    pg.typewrite("start brave https://web.whatsapp.com/" )
    sleep(1)
    pg.press("enter")
    sleep(20)

def search():
    pg.leftClick(328,228)
    sleep(1)
    pg.typewrite(user)
    sleep(2)
    pg.leftClick(339,432)
    sleep(1)

def emo():
    sleep(1)
    pg.leftClick(720,963)
    for i in range(1):
        pg.leftClick(724,668)
        sleep(0.2)
    sleep(1)    
    pg.leftClick(720,963)    

def msg():
    for i in range(limit):
        pg.typewrite(message)
        sleep(1)
        emo()
        sleep(1)
        pg.leftClick(1497,954)
        sleep(1)
        pg.press("enter")
        sleep(1)

def close():
    sleep(2)
    #reopening teminal to close
    pg.leftClick(1295,1055,1,1)
    sleep(1)
    pg.typewrite("taskkill /f /im brave.exe")
    sleep(1)
    pg.press("enter")
    sleep(1)
    pg.typewrite("exit")  
    sleep(1)
    pg.press("enter")

#******************************CODE START FROM HERE****************************************
i=0
j = int(input("give j value="))
for i in range(0,1,1):
    sleep(3)
    user = input("username=:")
    message = input("message=:")
    limit = int(input("limit=:"))
    start()
    search()
    msg()
    for j in range(0,j,1):
        sleep(3)
        user=input("username=:")
        message=input("message=:")
        limit=int(input("limit=:"))
        search()
        msg()
            
    


print("success")
