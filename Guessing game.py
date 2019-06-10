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

# The car game
command = ""
started = False
while True:
    command =input(">").lower()
    if command=="start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")
    elif command=="stop":
        if not started:
            print("Car already stopped")
        else:
            started=False
            print("Car stopped")
    elif command == "help":
        print("""
Start = to start the car
Stop = to stop the car
quit = to quit """)
    elif command=="quit":
        break
else:
    print("Sorry I don't understand")
