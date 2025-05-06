import random
import string

from words import words

def get_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word or '_' in word : 
        #get rid of words containing '-' or ' ' or '_'
        word = random.choice(words)
    return word

def hang_man():
    
    word = get_word(words)
    word_letters = set(word)   #returns the string into a set, containing unique letters in that string
    alphabets = set(string.ascii_uppercase)
    used_letters = set()#what the user is guessed

    #getting user's input
    while len(word_letters)>0:

        user_letter = input("Guess a letter: ").upper()
        if used_letters in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("you have already used that character. Please try again!")
        else:
            print("Invalid character")


# user_input = input("type something:")
# print(user_input)
hang_man()