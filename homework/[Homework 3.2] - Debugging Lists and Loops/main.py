# Homework 3.2 - Debugging Lists and Loops

# Task 1 - First Things First
todo_list = ["water plants", "clean bathroom", "eat ice cream"]
print("The first thing to get done is: " + todo_list[0])


# Task 2 - Print Grades
grades = [95, 67, 73, 88, 99, 91, 68, 75, 89]
for i in range(8):
  print(grades[i])
print(grades[len(grades) - 1])

# Task 3 - Enter Names
num_people = int(input("How many people? "))
names = []
for i in range(num_people):
  names.append(input("Enter name: "))

for name in names:
  print(name)


# Task 4 - Multiply List
num_items = int(input("How many numbers? "))

result = 0
for i in range(num_items):
  number = int(input("Enter Number: "))
  if result == 0 and i == 0:
    result = number
  else:
    result *= number

if num_items == 0:
    result = 0

print("Total Multiplication: " + str(int(result)))