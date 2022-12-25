"""               
REQUIREMENTS FOR THIS CODE TO WORK :
1. A BROWSER 
2. CODE EDITOR , YOU CAN ALSO TYPE python whatsapp_chat.py
3. YOU HAVE TO ALREADY LOGIN YOUR WHATSAPP FOR ONE TIME THAN YOU CAN CLOSE YOUR BROWSER /BUT REMEMBER DONT CLOSE THE
   LINK FROM YOUR PHONE

WHY IS THIS CODE? :
1. YOU CAN USE OTHER LIBRARIES BUT I WANT TO DO IT WITH THE HELP OF PYAUTOGUI(USED FOR AUTOMATION)

LIBRARY TO INSTALL :
1. PYAUTOGUI :
            FOR INSTALLING OPEN TERMNAL AND TYPE pip install pyautogui

REMEBER :
1. YOU CAN USE PYEX.PY FILE TO FIND THE COORDINATE OF YOUR MOUSE AND FILL IT WHERE IT REQUIRED IN THE CODE
2. IMPORTANT :
             CHECK THE START() CODE AND CHANGE TYPE YOUR BROWSER AFTER START 
3. FIRST RUN THE CODE TO CHECK WHERE IT ID IS REQUIRED TO CHANGE BY OBSERVING THE PROGRAM .

******************** WELL FEEL HAPPY IF YOU ABLE TO RUN THE CODE ***********************
"""
import pyautogui as pg
from time import sleep

# You can change the coordinate of leftClick() by using pyex.py file 

def start():
    sleep(1)
    pg.press("win")
    sleep(1)
    pg.typewrite("cmd")
    sleep(1)
    pg.press("enter")
    sleep(2)
    pg.typewrite("start brave https://web.whatsapp.com/" ) #you need to type your browser name which is installed in your pc
    sleep(1)
    pg.press("enter")
    sleep(20)

def search():
    #The line below will click at whatsapp user search box
    pg.leftClick(328,228)
    sleep(1)
    #The line below will type the user name of the reciever
    pg.typewrite(user)
    sleep(2)
    #The line below will click on message box.
    pg.leftClick(339,432)
    sleep(1)

def emo():
    #The line below will open emojies
    pg.leftClick(720,963)
    sleep(0.2) 
    for i in range(1):
        #The line below will click on recent emoji
        pg.leftClick(724,668)
        sleep(0.2)    
    #The line below will close the emojies    
    pg.leftClick(720,963)    
    sleep(0.2)

def msg():
    for i in range(limit):
        #The line below will Type the message given by the sender.
        pg.typewrite(message)
        #This condition will not call emoji function if the user gives the n as input for emoji.
        if emoji != 'n':
            emo()
        #The code below will again touch the message box    
        pg.leftClick(1497,954)    
        sleep(0.5)
        #The code below will send the message
        pg.press("enter")

def close():
    sleep(2)
    #reopening teminal to close # for that you need the coordinate of terminal on Taskbar after only your 
    #vs code is open on and not other tasks
    # note: that this will only open terminal if there is only one terminal instance open on taskbar.
    pg.leftClick(1295,1055,1,1)
    sleep(1)
    #This will type the msg on terminal to close the browser
    pg.typewrite("taskkill /f /im brave.exe")
    sleep(1)
    pg.press("enter")
    sleep(1)
    #Ignore the code below written in comments 
    # pg.typewrite("taskkill /f /im screenrec.exe")
    # sleep(1)
    # pg.press("enter")
    # sleep(1)
    pg.typewrite("exit")  
    sleep(1)
    pg.press("enter")
    

#******************************CODE START FROM HERE****************************************
a = int(pg.prompt("how many times you want to run this program=:"))
while True:
    user = pg.prompt("Type user name you want to send message=:")
    message = pg.prompt("Type the message you want to send=:")
    emoji = pg.prompt("Want emoji after your message if yes type y or else n:=")
    limit = int(pg.prompt("How many times you want the message to be delivered =:"))
    #The code below will execute for the first time
    start()
    search()
    msg()
    #The code below will execute after the first time
    if a>1:
        a-=1
        for i in range(a):
            sleep(3)
            user = pg.prompt("Type user name you want to send message=:")
            message = pg.prompt("Type the message you want to send=:")
            emoji = pg.prompt("Want emoji after your message if yes type y or else n:=")
            limit = int(pg.prompt("How many times you want the message to be delivered =:"))
            search()
            msg()
            
    break    
sleep(1)            
close()    


print("success")
