"""Guess the word"""

import random #This imports the random module

Lives = (5,4,3,2,1,0)

Dead = len(Lives) - 1


WORDS = ("adduct", "absurd" , "acquit", "adjust" , "badger", "bangle", "catkin", "dancer",
"earwig", "fabric", "garlic")

lives = 5
word = random.choice(WORDS) 
so_far = "-" * len(word) 
wrong = 0 
used = [] 

#main part of the code


start_game = input("Would you like to play a game? type 'yes' or 'no' ")
if start_game == 'yes':
    print("Welcome to 'Guess the word' ")
    while wrong < Dead and so_far != word:
        print("You have used these letters: \n", used,)
        print("You have", wrong, "lives left")
        print("So far, the word is", so_far)
        guess = input("\nEnter your guess:  ")
        guess = guess.lower()

        while guess in used:
            print("You have used that letter" , guess)
            guess = input("Enter your guess: ")
            guess = guess.lower()

        used.append(guess)
        
        if guess in word:
            print("That letter is in the word")
        
            new = "" # NOTE: This creates a new so_far
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        
        else:
            print("The letter" ,guess, "is not in the word")
            wrong += 1
            lives -= 1
            print("You have", lives, "left")
            

    if wrong == Dead:
        print("You have no lives left.")
        print("The word was", word)
else:
    print("Ok then ")
    input("Press the enter key to exit")