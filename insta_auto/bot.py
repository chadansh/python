import pyautogui as pg
import time as t
import random


    
#**********************************************************open function*******************************************************
class main:
   
    def __init__(self,alreadyLogin,task,admin,password,user):
        self.alreadyLogin=alreadyLogin
        self.task=task
        self.admin=admin
        self.password=password
        self.user=user
    def open(self):
        #opening cmd
        pg.press("win")
        t.sleep(1)
        pg.typewrite("cmd")
        t.sleep(1)
        pg.press("enter")
        t.sleep(3)
        #opening brave in cmd
        
        if self.alreadyLogin=='y':
            if self.task==4:
                pg.typewrite("start brave https://www.instagram.com/direct/new/")
                t.sleep(1)
                pg.press("enter")    
                t.sleep(10)
            elif self.task==6:
                pg.typewrite("start brave https://www.instagram.com/explore/")    
                t.sleep(1)
                pg.press("enter")
                t.sleep(5)
            else:
                pg.typewrite("start brave https://www.instagram.com/")
                t.sleep(1)
                pg.press("enter")
                t.sleep(10)
        else:
            pg.typewrite("start brave https://www.instagram.com/")
            t.sleep(1)
            pg.press("enter")
            t.sleep(10)
            #filling details
            pg.leftClick(1141,407)
            t.sleep(1)
            pg.typewrite(self.admin)
            t.sleep(1)
            pg.leftClick(1109,465)
            t.sleep(1)
            pg.typewrite(self.password)
            t.sleep(1)
            pg.press("enter")
            t.sleep(10)
    def close(self):
        #closing the program
        pg.click(1303,1043)
        t.sleep(1)
        pg.typewrite("taskkill /f /im brave.exe")
        t.sleep(1)
        pg.press("enter")
        t.sleep(1)
        pg.typewrite("exit")
        t.sleep(1)
        pg.press("enter")
    #**********************************************************like function**************************************************
    def like(self,scroll,likeLimit):
        self.scroll=scroll
        self.likeLimit=likeLimit
        #open search box
        pg.leftClick(863,138)
        t.sleep(1)
        #searching user
        pg.typewrite(self.user)
        t.sleep(1)
        pg.press("enter")
        t.sleep(1)
        pg.press("enter")
        t.sleep(5)
        pg.scroll(scroll)
        #open a recent post
        pg.leftClick(424,383,1,1)
        t.sleep(1)
        #like post
        for i in range(likeLimit):
            pg.doubleClick(561,506)
            t.sleep(3)
            pg.leftClick(1847,546,1,1)
            t.sleep(3)
    #*******************************************************comment function**************************************************
    def comment(self,limit,scroll,msglist):
        self.scroll=scroll
        self.limit=limit
        self.msglist=msglist
        #open search box
        pg.leftClick(863,138)
        t.sleep(1)
        #searching user
        pg.typewrite(self.user)
        t.sleep(1)
        pg.press("enter")
        t.sleep(1)
        pg.press("enter")
        t.sleep(5)
        pg.scroll(scroll)
        #open a recent post
        pg.leftClick(424,383,1,1)
        t.sleep(1)
        #comment post
        for i in range(limit):
            pg.doubleClick(561,506)
            t.sleep(1)
            msg=random.choice(msglist)
            pg.typewrite(msg)
            t.sleep(1)
            pg.press("enter")
            t.sleep(1)
            pg.leftClick(1847,546,1,1)
            t.sleep(3)
    #************************************like and comment function*****************************************   
    def likeComment(self,scroll,msglist,limit):
        self.limit=limit
        self.scroll=scroll
        self.msglist=msglist
        #open search box
        pg.leftClick(863,138)
        t.sleep(1)
        #searching user
        pg.typewrite(self.user)
        t.sleep(1)
        pg.press("enter")
        t.sleep(3)
        pg.press("enter")
        t.sleep(5)
        pg.scroll(scroll)
        #open a recent post
        pg.leftClick(424,383,1,1)
        t.sleep(1)
        for i in range(limit):
            #like a post
            pg.doubleClick(561,506)
            t.sleep(3)
            #comment on post
            pg.leftClick(1448,933,1,1)
            t.sleep
            msg=random.choice(msglist)
            pg.typewrite(msg)
            t.sleep(1)
            pg.press("enter")
            t.sleep(1)
            pg.leftClick(1847,546,1,1)
            t.sleep(2)
    #************************************chat functions*************************************************
    def multiuser(self,num_usr,limit,msg):
        i=0
        pg.leftClick(819,372)
        t.sleep(1)
        #searching user
        for j in num_usr:
            pg.typewrite(num_usr[i])
            i+=1
            t.sleep(3)
            pg.leftClick(884,453)
            t.sleep(3)
        #next
        pg.leftClick(1195,290,1,1)
        t.sleep(10)
        #inside chat
        pg.leftClick(1045,911)
        t.sleep(1)
        for i in range(limit):
            pg.typewrite(msg)
            t.sleep(1)
            pg.press("enter")
            t.sleep(1)       
    def chat(self,num_usr,limit,msg):
        self.num_usr=num_usr
        self.limit=limit
        self.msg=msg
        if self.alreadyLogin=='y':
            if num_usr==1:
                pg.leftClick(819,372)
                t.sleep(1)
                pg.typewrite(self.user)
                t.sleep(3)
                pg.leftClick(884,453)
                t.sleep(3)
                #next
                pg.leftClick(1195,290,1,1)
                t.sleep(10)
                #inside chat
                pg.leftClick(1045,911)
                t.sleep(1)
                for i in range(limit):
                    pg.typewrite(msg)
                    t.sleep(0.5)
                    pg.press("enter")
                    t.sleep(0.5)
            else:
                multiuser(num_usr,limit,msg)
        else:
            pg.leftClick(1349,142,1,2)      
            t.sleep(2)
            pg.leftClick(1218,732,1,2)
            t.sleep(2)
            multiuser(num_usr,limit,msg)
    #*************************storyWatch Function***********************************************
    def storyWatch(self,time):
        self.time=time
        pg.leftClick(1278,152,1,2)
        t.sleep(1)
        pg.leftClick(403,292,1,2)
        t.sleep(1)
        pg.leftClick(1088,198,1,2)
        t.sleep(self.time)
    
    def surf(self,limit,time):
        self.limit=limit
        self.time=time
        if self.alreadyLogin=='y':
            pg.leftClick(483,441,1,1)
            for i in range(limit):
                t.sleep(time)
                pg.leftClick(1847,546,1,1)
        else:
            pg.leftClick(1486,142,1,1)
            t.sleep(2)
            pg.leftClick(483,441,1,1)
            for i in range(limit):
                t.sleep(time)
                pg.leftClick(1847,546,1,1)
