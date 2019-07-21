 ### guessing game....
secret_num = 10
guess_count = 0
guess_limit = 5
guess = ''
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == secret_num:
        print('You have won the game')
        break
else:
    print('Sorry try again')

######################################################
 ## car start game
user_command = ''
Car_started = False
while True:
    user_command = input(">").lower()
    if user_command == "start":
        if Car_started:
            print("Car already started")
        else:
            Car_started = True
            print("Car started")
    elif user_command == "stop":
        if not Car_started:
            print("Car already stopped")
        else:
            Car_started = False
            print("Car stopped")
    elif user_command == "help":
        print("""
start = to start the car
stop = to stop the car
quit = to quit """)
    elif user_command=="quit":
        break
    else:
        print("Sorry I dont understand you")
#######################################################################################

for x in range (1,5):
    for y in range (1,5):
        print(f'({x}, {y})')


##############################################
#Printing phone numbers in words
phone= input("Phone: ")
digits_map = {"0":'Zeor', '1':'One', '2':'Two', '3':"Three", '4':'Four', '5':'Five', '6':'Six'}
output = " "
for ch in phone:
    output += digits_map.get(ch, '!') + " "
print(output)

##################################################

message = input(">")
words = message.split(" ")
emojis = {":)":"😍", ":(":"😒"}
output_1 = ""
for word in words:
    output_1+=emojis.get(word, word) + " "
print(output_1)


###########################################################
# Emoji converter function

def emoji_converter (message):
    words = message.split(" ")
    emojis = {":)": "😍", ":(": "😒"}
    output_1 = ""
    for word in words:
        output_1 += emojis.get(word, word) + " "
    return output_1


message = input(">")
print(emoji_converter(message))


#########################################
#Classeeeeeeeeeeeeeeeeeeeeeeeeeees
# Are used ti define new types; we cna use them to define new types to model new concepts.

class Person:
    def __init__(self, name):
        self.name = name

    def talk (self):
        print(f"Hi I am, {self.name}")


brian = Person ("Brian Mumba")
brian.talk()

Mary = Person("Mary Mumba")
Mary.talk()






