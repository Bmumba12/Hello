# This creates a simple guessing game

secret_number = 5
guess_count = 0
guess_limit = 2
while guess_count < guess_limit:
    guess= int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Sorry you have failed the game")
