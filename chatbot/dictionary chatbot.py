from nltk.corpus import wordnet
print("I am dictionary chatbot used to find the synonms or antonyms of the word")
def dic():
    while True:
        word=input("Give the word :")
        user=wordnet.synsets(word)
        msg=["end","quit","bye","tata","see you"]
        if word in msg:
            break  
        print("To get the meaning or synonms of the word press = 1\nTo get the opposite or antonyms of the word press =2\nTo get the examples of the word press = 3\n")
        user_need=int(input())
         
        if user_need==1:
                print("Synonms:",user[1].definition())
        if user_need==2:
            if(user[0].lemmas()[0].antonyms()):
                print("Antonyms :",user[0].lemmas()[0].antonyms()[0].name())
            else:
                print("No Antonyms")
        if user_need==3:
            print("Examples: ",user[0].examples())
        
                        
dic()







