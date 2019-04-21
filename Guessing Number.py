import random
def guessing():
    randNum = random.randint(1 , 100)
    number_guessing = 0
    isrunning = 1
    while isrunning:
        number_guessing += 1
        print("Hi human guess a number 1-100! \nYour Trial is " + str(number_guessing))
        guess = int(input())
        
        if guess > randNum:
            print("your guess is high")
    
        if guess < randNum:
            print("your guess is  low")
    
        if guess == randNum:
           print("awsome you're a genius ^_^\nyou complete guessing in {} guesses\n".format(number_guessing))
           isrunning = 0

while True:
    guessing()
    
    
  
