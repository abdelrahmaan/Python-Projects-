import random
def guessing():
    randNum = random.randint(1 , 100)
    isrunning = 1
    number_guessing = 0
    while isrunning:
        number_guessing += 1
        print("Hi human guess a number 1-100! \nYour Trial is " + str(number_guessing))
        guess = input()
        guess = int(guess)
        
        if guess > randNum:
            print("your guess is high")
    
        if guess < randNum:
            print("your guess is  low")
    
        if guess == randNum:
            print("awsome you're a genius ^_^\nyou complete guessing in " + str(number_guessing) + " guesses\n")
            isrunning = 0
for i in range(100):
    guessing()
