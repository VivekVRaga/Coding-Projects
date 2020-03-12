import random
#this program is a guessing game, Guess a number and it will tell you if the guess is correct

def gen(guessed):
    if int(guessed) > num:
        print('guess is too large')
    elif int(guessed) < num:
        print('guess is too small')
    else:
        print('correct')

        return 1

num=random.randint(1,20)
guessnum=0
guessed =  input('Guess a number between 1 and 20\n')
while 1:
    guessnum+=1
    if gen(guessed) == 1:
        print('you guessed it in ',guessnum,' tries')
        break
    guessed = input('')



