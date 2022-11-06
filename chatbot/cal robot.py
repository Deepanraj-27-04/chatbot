print(",I am calbot used to calculate the basic operations")
def cal_robot():
    
    user_split=user.split()
    if "add" in user:
        return float(user_split[1])+float(user_split[2])
    elif "sub" in user:
        return float(user_split[1])-float(user_split[2])
    elif " mul" in user:
        return float(user_split[1])*float(user_split[2])
    elif "div" in user:
        return float(user_split[1])/float(user_split[2])
    elif "square" in user:
        return float(user_split[1])**2
    
while True:
     user=input() 
     msg=["end","quit","bye","tata","see you"]
     if user in msg:
         break
     else:
        print(cal_robot(user))
    
    
    
  