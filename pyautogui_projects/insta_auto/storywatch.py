from bot import main
class insta(main):
    pass

while True:
    login=input("AlreadyLogin y : or n :? =")
    time= int(input("total time= "))
    match login:
        case 'n':
            break
        case 'y':
            break
    if login!='y' or login!='n':
        print("try again")


x = insta(login,5)
x.open()
x.storyWatch(time)
x.close()    