# Homework 3.1 - Loops and Lists

# Task 1: Sum List
all_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

number_sum = 0

for number in all_numbers:
  number_sum += number

print('Total sum is: ' + str(number_sum))  

# Task 2: RSVP Names
attendance = int(input('How many people in your party? '))

names = []

if not(attendance):
  pass
else:
  print('List the names below:')
  for x in range(attendance):
    names.append(input())

if not(names):
  print('No one is registered.')
else:
  print('The following are registered to attend:')
  for name in names:
    print(name)

# Task 3: Print If Greater Than 100
amount = int(input('How many numbers? '))

numbers = []

numbers_printed = 0

for x in range(amount):
  numbers.append(int(input('Enter a number: ')))

for number in numbers:
  if number > 100:
    print(number)
    numbers_printed += 1

if numbers_printed == 0:
  print('All numbers are less than 100!')

# Task 4: How Many Handshakes?
people = int(input('How many people in the room? '))

handshakes = int((people * (people - 1)) / 2)

print(str(handshakes) + ' total handshakes.')

# Task 5: Find All The 'E's!

elist = []

sentence = input('Enter a sentence of phrase: ')

for index in range(len(sentence)):
  if sentence[index] == 'e' or sentence[index] == 'E':
    elist.append(index)

print('Found \'e\' ' + str(len(elist)) + ' times!')
print('Indexes are: ' + str(elist))