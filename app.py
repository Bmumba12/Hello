#name1 = input('What is your name?   ')
#ycolor = input('what is your favorite?  ')
#print(name1 + ' likes ' + ycolor)

#birth_year = input('Birth Year:  ')
#age = 2019 - int(birth_year)
#print(age)

# "Another function to convert respondents weight in pound to kg"
#weight_lb = input('What is your weight in pound? ')
#weigh_kg = int(weight_lb) * 0.454
#print(weigh_kg)

#Strings

# emal = '''
# Hello Mumba,

# I have been waiting to hear from you today.
# Please return as soon as you receive this message.

# Thanks

# '''
# print(emal)

course = 'This is my python first course'
# print(len(course))
# print(course.upper())
# print(course)
# print(course.replace("my python first course", "python course absolutely for beginners"))
# print('my python' in course)

# is_hot = False
# is_cold = False
# if is_hot:
    # print("It's a hot day")
    # print(" Drink a lot of water")
# elif is_cold:
    # print("It's a cold day")
    # print("Wear warm cloths")
# else:
    # print("It's a lovely day")
# print("Enjoy your day")

# Suppose the price of a house is $1M. If the buyer has good credit, they need to put down 10% of
# of the price of the house. Otherwise, they need to put down 20%. Write a program with these rules and print
# print down the down payment of the buyer with good credit.

price = 1000000
good_buyer = True
if good_buyer:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down_payment: ${down_payment}")

# If the applicant has high income and good credit, then they are elligible for loan.
has_high_income =True
has_good_credit =False
if has_high_income and has_good_credit:
    print("Elligible for loan")
else:
    print("None")

# At least given one condition is true
has_high_income =True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Elligible for loan")
else:
    print("None")

# Comparision operators
# If temperature is greater than 30, its a hot day. Otherwise, it is less than 30, its a cold day.
# Otherwise, its neither hot nor cold.

temp= 40
if temp > 30:
    print("It's a hot day")
else:
    print("It's a cold day")

name = "John Mumba"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must at least be maximum of 50 characters")
else:
    print("Name looks good")











