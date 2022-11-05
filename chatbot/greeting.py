from random import randint
def greet_random():
    greeting=["hey","haii","hello","vanakkam","namashte","welcome","banjour"]
    n=0
    n=randint(0,(len(greeting)-1))
    return greeting[n]

print("vanakkam,I am chatbot repeats whatever you say")
greet_ing=greet_random()

    