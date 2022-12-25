from bot import main
class insta(main):
    pass

while True:
    login=input("AlreadyLogin y : or n :? =")
    limit= int(input("No. of post= "))
    time= int(input("time to watch every post= ")) 
    match login:
        case 'n':
            break
        case 'y':
            break
    if login!='y' or login!='n':
        print("try again")

        
x = insta(login,6)  
x.open()
x.surf(limit,time)  
x.close()
    

