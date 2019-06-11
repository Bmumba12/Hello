
#for name in range(1,21,2):
    # print(name)

prices= [5, 10, 15, 20, 25]
total= 0
for price in prices:
    total = total + price
print(f'Total= {total}')

# Nested loops

for x in range(5):
    for y in range(5):
        print(f'({x}, {y})')


# A challenge
Number = [5, 2, 5, 2, 2]
for x_count in Number:
    print('x' * x_count)

# The other way
Number = [5, 2, 5, 2, 2]
for L_count in Number:
    output = ""
    for count in range(L_count):
        output+= 'L'
    print(output)

# Printing the maximum number in a list
numbers = [2, 4, 6, 7, 8, 9, 11, 1, 23, 3, 50]
max = numbers[0]
for x in numbers:
    if x > max:
        max = x
print(max)






















