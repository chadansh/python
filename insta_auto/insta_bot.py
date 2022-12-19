import pyautogui as pg
from time import sleep
import random
import keyboard as key    


    
#**********************************************************open function*******************************************************
def open():
    #opening cmd
    pg.press("win")
    sleep(1)
    pg.typewrite("cmd")
    sleep(1)
    pg.press("enter")
    sleep(3)
    #opening brave in cmd
    if alreadyLogin=='y':
        if task==4:
            pg.typewrite("start brave https://www.instagram.com/direct/new/")
            sleep(1)
            pg.press("enter")    
            sleep(10)
        elif task==6:
            pg.typewrite("start brave https://www.instagram.com/explore/")    
            sleep(1)
        else:   
            pg.typewrite("start brave https://www.instagram.com/")
        sleep(1)
        pg.press("enter")
        sleep(10)
    else:
        pg.typewrite("start brave https://www.instagram.com/")
        sleep(1)
        pg.press("enter")
        sleep(10)
        #filling details

        pg.leftClick(1141,407)
        sleep(1)
        pg.typewrite(admin)
        sleep(1)
        pg.leftClick(1109,465)
        sleep(1)
        pg.typewrite(password)
        sleep(1)
        pg.press("enter")
        sleep(10)

   
  
        

#**************************************************************close function**************************************************
def close():
    #closing the program
    pg.click(1303,1043)
    sleep(1)
    pg.typewrite("taskkill /f /im brave.exe")
    sleep(1)
    pg.press("enter")
    sleep(1)
    pg.typewrite("exit")
    sleep(1)
    pg.press("enter")

#**********************************************************like function**************************************************
def like():
    #open search box
    pg.leftClick(863,138)
    sleep(1)
    #searching user
    pg.typewrite(user)
    sleep(1)
    pg.press("enter")
    sleep(1)
    pg.press("enter")
    sleep(5)
    pg.scroll(scroll)
    #open a recent post
    pg.leftClick(424,383,1,1)
    sleep(1)
    #like post
    
    for i in range(likeLimit):
        pg.doubleClick(561,506)
        sleep(3)
        pg.leftClick(1847,546,1,1)
        sleep(3)
        

#*******************************************************comment function**************************************************
def comment():
    #open search box
    pg.leftClick(863,138)
    sleep(1)
    #searching user
    pg.typewrite(user)
    sleep(1)
    pg.press("enter")
    sleep(1)
    pg.press("enter")
    sleep(5)
    pg.scroll(scroll)
    #open a recent post
    pg.leftClick(424,383,1,1)
    sleep(1)
    #comment post

    for i in range(likeLimit):
        pg.doubleClick(561,506)
        sleep(1)
        msg=random.choice(list)
        pg.typewrite(msg)
        sleep(1)
        pg.press("enter")
        sleep(1)
        pg.leftClick(1847,546,1,1)
        sleep(3)
        


#************************************like and comment function*****************************************   
def likeComment():
    #open search box
    pg.leftClick(863,138)
    sleep(1)
    #searching user
    pg.typewrite(user)
    sleep(1)
    pg.press("enter")
    sleep(3)
    pg.press("enter")
    sleep(5)
    pg.scroll(scroll)
    #open a recent post
    pg.leftClick(424,383,1,1)
    sleep(1)
    

    for i in range(limit):
        #like a post
        pg.doubleClick(561,506)
        sleep(3)
        #comment on post
        pg.leftClick(1448,933,1,1)
        sleep
        msg=random.choice(list)
        pg.typewrite(msg)
        sleep(1)
        pg.press("enter")
        sleep(1)
        pg.leftClick(1847,546,1,1)
        sleep(2)
    
#************************************chat functions*************************************************
def multiuser():
    i=0
    pg.leftClick(819,372)
    sleep(1)
    #searching user
    for j in range(num_usr):
        pg.typewrite(user1[i])
        i+=1
        sleep(3)
        pg.leftClick(884,453)
        sleep(3)
    #next
    pg.leftClick(1195,290,1,1)
    sleep(10)
    #inside chat
    pg.leftClick(1045,911)
    sleep(1)
    for i in range(limit):
        pg.typewrite(msg)
        sleep(1)
        pg.press("enter")
        sleep(1)

def chat():
    
    if alreadyLogin=='y':
        if num_usr==1:
            pg.leftClick(819,372)
            sleep(1)
            pg.typewrite(user)
            sleep(3)
            pg.leftClick(884,453)
            sleep(3)
            #next
            pg.leftClick(1195,290,1,1)
            sleep(10)
            #inside chat
            pg.leftClick(1045,911)
            sleep(1)
            for i in range(limit):
                pg.typewrite(msg)
                sleep(0.5)
                pg.press("enter")
                sleep(0.5)
        else:
            multiuser()
    else:
        pg.leftClick(1349,142,1,2)      
        sleep(2)
        pg.leftClick(1218,732,1,2)
        sleep(2)
        multiuser()
      

#*************************storyWatch Function***********************************************
def storyWatch():
    pg.leftClick(1278,152,1,2)
    sleep(1)
    pg.leftClick(403,292,1,2)
    sleep(1)
    pg.leftClick(1088,198,1,2)
    sleep(30)

def surf():
    if alreadyLogin=='y':
        pg.leftClick(483,441,1,1)
        for i in range(limit):
            sleep(15)
            pg.leftClick(1847,546,1,1)
    else:
        pg.leftClick(1486,142,1,1)
        sleep(2)
        pg.leftClick(483,441,1,1)
        for i in range(limit):
            sleep(15)
            pg.leftClick(1847,546,1,1)

        




#*****************************************************************code start from here**************************************************
alreadyLogin=input("already login? y or n=")
if alreadyLogin=='n':
    admin=input("admin=")
    password=input("password=")
print("Press 1.LikePost\nPress 2.Comment\nPress 3.Like_and_Comment\nPress 4.Chat \nPress 5.Watch insta story\nPress 6.surfing")
task=int(input("your option="))
print("Note for hashtag  user will work as hashtag" )
user=input("username=")

if task==1:
    likeLimit=int(input("how many photo you want to like="))
    scroll=int(input("scroll="))
    open()
    like()
    close()

elif task==2:
    commentLimit=int(input("how many comment you want to write"))
    scroll=int(input("scroll="))
    # print("tell me your 5 comments 1 by 1")
    list=["mast","nice","shandar","bhadiya","awesome","amazing"]
    # for i in range(5):
    #     a=input("")
    #     list.append(a)

    open()
    comment()
    close()    

elif task==3:
    limit=int(input("how many like and comment you want?="))
    scroll=int(input("scroll="))
    # print("tell me your 5 comments 1 by 1")
    list=["mast","nice","shandar","bhadiya","awesome","amazing"]
    # for i in range(5):
    #     a=input("")
    #     list.append(a)

    open()
    likeComment()
    close()    

elif task==4:
    limit=int(input("how many msg you want to send="))
    num_usr=int(input("number of user to send msg="))
    msg=input("your message=")
    if num_usr >1:
        user1=[]
        print("type the users on by one:")
        for i in range(num_usr):
            a=input("users=")
            user1.append(a)
    open()    
    chat()
    close()

elif task==5:
    open()
    storyWatch()
    close()

elif task==6:
    limit = int(input("number of post to explore="))
    open()
    surf()           
    close()

else:
    print("you typed wrong")



sleep(5)
print("everything works fine")




