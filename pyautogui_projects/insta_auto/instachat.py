from bot import main
import pyautogui as pg
class insta(main):
    pass

while True:
    login=pg.prompt("AlreadyLogin y : or n :? =")
    msg=pg.prompt("msg=")
    usr= []
    a=int(pg.prompt("number of user"))
    limit= int(pg.prompt("limit= "))
    if a==1 and a>0:
        usr=pg.prompt("user=")
    else:
        print("enter user 1 by 1")
        for i in range(a):
            username=pg.prompt("user=: ")
            usr.append(username)
            print(usr)
    match login:
        case 'n':
            break
        case 'y':
            break
    if login!='y' or login!='n':
        print("try again")

x = insta(login,4)
x.open()
mul=x.multiuser
x.chat(usr,limit,msg,mul,a)
x.close()