from bot import main
class insta(main):
    pass

while True:
    login=input("AlreadyLogin y : or n :? =")
    msg=input("msg=")
    num_usr= []
    a=int(input("number of user"))
    limit= int(input("limit= "))
    if a==1 and a>0:
        user=input("user=")
    else:
        print("enter user 1 by 1")
        for i in range(a):
            username=input("user=: ")
            num_usr.append(username)
    match login:
        case 'n':
            break
        case 'y':
            break
    if login!='y' or login!='n':
        print("try again")

x = insta(login,"_ansh_bajpai_","ansh@999","",4)
x.open()
mul=x.multiuser
x.chat(num_usr,limit,msg,mul)
x.close()