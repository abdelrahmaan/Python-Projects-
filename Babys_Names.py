import random
import string

letter_input_1 = input('Choose a letter "v" for Vowels , "c" for Consonants , "o" for any other letter ')
letter_input_2 = input('Choose a letter "v" for Vowels , "c" for Consonants , "o" for any other letter ')
letter_input_3 = input('Choose a letter "v" for Vowels , "c" for Consonants , "o" for any other letter ')
letter_input_4 = input('Choose a letter "v" for Vowels , "c" for Consonants , "o" for any other letter ')
letter_input_5 = input('Choose a letter "v" for Vowels , "c" for Consonants , "o" for any other letter ')

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
other = string.ascii_lowercase

def generator():
    # 1st
    if (letter_input_1 == "v" or "V"):
        letter1 = random.choice(vowels)
    elif (letter_input_1 == "c" or "C"):
        letter1 = random.choice(consonants)
    elif (letter_input_1 == "o" or "O"):
        letter1 = random.choice(other)
    else:
        letter1 = letter_input_1
    # 2nd
    if (letter_input_2 == "v" or "V"):
        letter2 = random.choice(vowels)
    elif (letter_input_2 == "c" or "C"):
        letter2 = random.choice(consonants)
    elif (letter_input_2 == "o" or "O"):
        letter2 = random.choice(other)
    else:
        letter2 = letter_input_2
    # 3th
    if (letter_input_3 == "v" or "V"):
        letter3 = random.choice(vowels)
    elif (letter_input_3 == "c" or "C"):
        letter3 = random.choice(consonants)
    elif (letter_input_3 == "o" or "O"):
        letter3 = random.choice(other)
    else:
        letter3 = letter_input_3
    # 4th
    if (letter_input_4 == "v" or "V"):
        letter4 = random.choice(vowels)
    elif (letter_input_4 == "c" or "C"):
        letter4 = random.choice(consonants)
    elif (letter_input_4 == "o" or "O"):
        letter4 = random.choice(other)
    else:
        letter4 = letter_input_4
    # 5th
    if (letter_input_5 == "v" or "V"):
        letter5 = random.choice(vowels)
    elif (letter_input_5 == "c" or "C"):
        letter5 = random.choice(consonants)
    elif (letter_input_5 == "o" or "O"):
        letter5 = random.choice(other)
    else:
        letter5 = letter_input_5
    name = letter1 + letter2 + letter3 + letter4 + letter5
    return (name)

for i in range (23):
    print(generator())