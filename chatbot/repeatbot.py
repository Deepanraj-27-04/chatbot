from greeting import *
get=greet_random()


def quit():
    msg=["end","quit","bye","tata","see you"]
    while True:   
        user=input() 
        if user in msg:
            break
        else:
            print(user)
quit()  

    
              