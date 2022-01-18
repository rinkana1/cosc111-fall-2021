# Homework 2.1 - Conditionals

# Task 1: Smallest Number
number1 = int(input("What is your first number?: "))
number2 = int(input("What is your second number?: "))

if number1 < number2:
  print(number1)
else:
  print(number2)

# Task 2: Date Validator
year = int(input("What is the year?: "))
month = int(input("What is the month?: "))
day = int(input("What is the day?: "))

if (year >= 1900) and (year <= 2020):
  print("Valid Year")
else:
  print("Invalid Year")

if month >= 1 and month <= 12:
  print("Valid Month")
else:
  print("Invalid Month")

if day >= 1 and day <= 31:
  print("Valid Day")
else:
  print("Invalid Day")

# Task 3: String Comparer

string1 = input("What is your first string?: ")
string2 = input("What is your second string?: ")

if string1 == string2:
  print("You said the same thing both times.")
else:
  print("You said " + string1 + " and then " + string2 + ".")

# Task 4: Water State Determiner

temp = int(input("What is the temperature of your water?: "))

if temp < 32:
  print("Water at that temperature is ice")
elif temp >= 32 and temp < 212:
  print("Water at that temperature is water")
else:
  print("Water at that temperature is steam")

# Task 5: Print True
A = False
B = True
C = False
D = True

if (A or B) and (C or D) and not (A and not D):
    print("Boolean expression is True!")
else:
    print("Boolean expression is False.")


# Task 6: Print Shorter String

first_string = input("What is your first string?: ")
second_string = input("What is your second string?: ")

if len(first_string) < len(second_string):
  print(first_string + " is shorter")
elif len(second_string) < len(first_string):
  print(second_string + " is shorter")
else:
  print("Both strings are the same length!")