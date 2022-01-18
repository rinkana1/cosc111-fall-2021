
# Homework 4.1 - Functions
def ExampleFunction():
    message = "I'm awesome!"
    return message


# Function 1 - Dice Roll
import random
def DiceRoll():
  return random.randint(1, 6)

# Function 2 - Double Dice DiceRoll
def DoubleDiceRoll():
  return DiceRoll() + DiceRoll()

# Function 3 - Odd Integers
def GetOddIntegersTo100():
  integers = []
  for i in range(0, 100):
    if i % 2 != 0:
      integers.append(i)
  
  return integers