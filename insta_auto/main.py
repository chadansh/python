
#*****************************************************************code start from here**************************************************
while True:
    alreadyLogin = input("already login? y or n=")
    if alreadyLogin=='n':
        admin=input("admin=")
        password=input("password=")

    print("Press 1.LikePost\nPress 2.Comment\nPress 3.Like_and_Comment\nPress 4.Chat \nPress 5.Watch insta story\nPress 6.surfing")
    task=int(input("your option="))
    print("Note that for hashtag  username will work as hashtag" )
    print("Note that for watching insta story or surfing username has no use")
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
        time = int(input("total time to watch all story"))
        open()
        storyWatch()
        close()
        

    elif task==6:
        limit = int(input("number of post to explore="))
        time = int(input("time to explore 1 post="))
        open()
        surf()           
        close()


    else:
        print(f"option number {task} is not valid")
    
    
    for i in range(1):
        if task==1 or task==2 or task==3 or task==4 or task==5 or task==6:
            print("everything works fine")
            pg.leftClick(1283,1044)
            print("**********************Your task is completed*************************")
        break    
    
    
    
    a=input("Press y:another task and press any key to exit= ")
    if a!='y':
        break