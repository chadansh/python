import pyautogui as pg
from time import sleep

def open():
    pg.press("win")
    sleep(1)
    pg.typewrite("cmd")
    sleep(1)
    pg.press("enter")
    sleep(2)
    #opening brave
    pg.typewrite("start brave")
    sleep(1)
    pg.press("enter")
    sleep(3)
    #opening incognito
    pg.leftClick(1295,1055,1,1)
    sleep(1)
    pg.typewrite("start brave /incognito https://motherless.com/")
    sleep(1)
    pg.press("enter")
    sleep(10)
#********************STORY WATCH*******************************
def storyWatch():
    pg.leftClick(498,492)
    sleep(3)
    #opening vs code
    pg.leftClick(1244,1038)
    sleep(1)
    for i in range(10):
        a=input("skip ?=: y or n =")
        if a=='y':
            sleep(2)
            pg.leftClick(1270,560,1,1)
            sleep(1)
            pg.leftClick(1244,1038)
        elif a=="close":
            close()    
        
    refweb()        
          
#*****************REFRESES THE BROWSER*****************************
def refweb():
    sleep(3)
    pg.leftClick(120,64,1,1)
    sleep(5)
    storyWatch()

#*****************FUNCTION TO CLOSE**********************************        
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

#************************CODE STARTS FROM HERE*************************
sleep(3)
open()
storyWatch()