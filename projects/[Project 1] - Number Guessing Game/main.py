'''
Name: Mackinley Hill

Project Title: Number Guessing Game

Description: After inputting a maximum value, the computer picks a 
random number between 0 and that maximum value. Then, the user 
guesses an integer. After each guess, the program tells the user 
whether their guess it too high, or too low. When the user guesses 
the correct number, the program prints the total number of guesses.

Due Date: 11/11/2021

Note: Instead of using while loops, I utilized recursion in this 
project. If you'd rather me use while loops, I can rewrite my code,
but this was the easiest and quickest solution I could think of.
'''

###### Imports ######
from random import *

###### Functions ######

# Function to get maximum value as input from the user
def GetMaximumValue():
  maximum = input('Enter the maximum value: ')
  print()

  if (not maximum.isnumeric()) or (int(maximum) < 0):
    print('Maximum number must be a positive integer')
    return GetMaximumValue()
  
  return int(maximum)

# Function to generate a random number to act as the answer
def GenerateRandomNumber(maximum):
  print('OK! I\'ve thought of a number. Try to guess what it is!')
  return randint(0, maximum)
# MH

# Function to get the user's guess
def GetGuess():
  guess = input('Enter guess: ')
  
  if (not guess.isnumeric()) or (int(guess) < 0):
    print('Your guess must be a positive integer!')
    return GetGuess()
  
  return guess

# Function to check if the value is correct
def CheckValue(guess, value, counter):
  counter += 1
  guess = int(guess)

  if guess == value:
    return counter
  
  # If the value is too high or too low, the program will call the function again and return the result
  if guess > value:
    print('Too High!')
    print()
    return CheckValue(GetGuess(), value, counter)
  
  if guess < value:
    print('Too Low!')
    print()
    return CheckValue(GetGuess(), value, counter)

# Function to print results after the game is complete
def PrintResults(answer, guesses):
  print()
  print('Hey! You got it! The number was: ' + str(answer))
  print()
  if guesses == 1:
    print('Took you ' + str(guesses) + ' guess.')
  else:
    print('Took you ' + str(guesses) + ' guesses.')
# MH

# Function to implement appropriate functions into gameplay
def PlayGame():
  print('Welcome to the Number Guessing Game!')
  print()

  # Variables
  maximum = GetMaximumValue()
  answer = GenerateRandomNumber(maximum)
  guess_counter = 0

  PrintResults(answer, CheckValue(GetGuess(), answer, guess_counter))
  print()

  PlayAgain()

# After each game, the program will ask the user if they want to play again, and restart the Play Game function with a new maximum, answer, and restarted guess counter
def PlayAgain():
  playagain = input('Would you like to play again? (Yes/Y or No/N) ').lower()
  print()

  if playagain == 'yes' or playagain == 'y':
    PlayGame()
  if playagain == 'no' or playagain == 'n':
    print('Thanks for playing !')

###### PROGRAM START ######

PlayGame()

## MH