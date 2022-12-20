from bot import main
class insta(main):
    pass

while True:
    user=input("user or hashtag you want to like =")
    login=input("AlreadyLogin y : or n :? =")
    scroll= int(input("scroll= "))
    limit= int(input("limit= "))
    msglist = []
    a = int(input("no of comments to save"))
    print("enter comment 1 by 1")
    for i in range(a):
        msg=input("comment= ")
        msglist.append(msg)
    match login:
        case 'n':
            break
        case 'y':
            break
    if login!='y' or login!='n':
        print("try again")

x = insta(login,"_ansh_bajpai_","ansh@999",user)
x.open()
x.likeComment(limit,scroll,msglist)
x.close()