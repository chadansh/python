import pyautogui as pg
from time import sleep
def open():
    pg.press("win")
    sleep(1)
    pg.typewrite("cmd")
    sleep(1)
    pg.press("enter")
    sleep(1)
    #opening brave
    pg.typewrite("start brave")
    sleep(1)
    pg.press("enter")
    sleep(3)
    #opening incognito
    pg.leftClick(1295,1055,1,1)
    sleep(1)
    pg.typewrite("start brave /incognito www.pornhub.com")
    sleep(1)
    pg.press("enter")
    sleep(10)
    #open vs code
    pg.leftClick(1244,1038)
    sleep(1)
    a = input("age verify?= y or n =")
    if a=='y':
        ageVerify()
    else:
        sleep(1)    

def ageVerify():
    pg.leftClick(873,707)
    sleep(10)

def setFor():
    #setting for 1080
    pg.leftClick(1694, 1034)
    sleep(1)
    pg.leftClick(1757, 931)
    sleep(1)
    pg.leftClick(1805, 777)
    sleep(1)
    pg.leftClick(1694, 1034)
    sleep(1)
    pg.moveTo(563, 577)


#*******************************FUNCTION TO START ************************************
def start():
    sleep(10)
    if limit == 0:
        sleep(10)
        close()
    #selected first video
    pg.leftClick(280,861)
    sleep(10)
    #fullscreen
    pg.doubleClick(457, 488) 
    sleep(vidDur)
    #exit fullscreen
    pg.doubleClick(457,488)
    sleep(2)
    for i in range(limit-1):
        pg.scroll(-1000)
        sleep(2)
        pg.leftClick(742,404)
        sleep(20)
        #full screen
        pg.doubleClick(457, 488) 
        sleep(vidDur)
        #exit fullscreen
        pg.doubleClick(457,488)
        sleep(2)
    close()
        
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

# print(pg.position())

#**********************************PORNHUB*******************************************************

limit = int(input("how many video you want to watch="))
vidDur = int(input("video duration per video:="))
open()
start()
print("Hope!,you enjoys the show")