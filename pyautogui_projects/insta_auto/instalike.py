from bot import main
class insta(main):
    pass

while True:
    user=input("user or hashtag you want to like =")
    login=input("AlreadyLogin y : or n :? =")
    scroll= int(input("scroll= "))
    likeLimit=int(input("like limit= "))
    match login:
        case 'n':
            break
        case 'y':
            break
    if login!='y' or login!='n':
        print("try again")

x = insta(login,1)
x.open()
x.like(scroll,likeLimit,user)
x.close()
    