'''
TODO: Describe algorithm here:

Choose word from list of words
Create two empty lists for the correct and incorrect answers

While the word isn't completed:
  Display the monster

  If the user has guessed incorrectly more than 5 times:
    End the game 
  
  Display the word:
    For every letter in the word:
      If the letter is in the list of correct letters:
        Display the letter
      Otherwise:
        Display an underscore (_)
    
    Display the list of incorrect answers

  Get a guess from the user and check it:
    For every letter in the word:
      If the guess matches the letter:
        Add the guess to the list of correct letters:
    
    If guess is not in the word:
      Add the guess to the list of incorrect letters
  
  Check if word is correctly answered:
    For every letter in word:
      If letter is not in the list of correct letters, return False
    
    Otherwise, return true

When while loop ends, go through winning sequence
'''

# Imports
from random import *

# Prints the monster using Text Art!
# It prints the monster progressively
# as the number of wrong guesses 
# increases (to 6 or greater).
def PrintMonster(num_wrong):
    print()
    print("-" * 40)
    print()
    print(r" ---------------- ")
    print(r"|                |")
    if num_wrong == 1:
        print(r"|                |")
        print(r"|                |")
        print(r"|       /\       |")
        print(r"|      /  \      |")
        print(r"|     /-  -\     |")
        print(r"|~~~~~~~~~~~~~~~~|")
    elif num_wrong == 2:
        print(r"|       /\       |")
        print(r"|      /  \      |")
        print(r"|     /-  -\     |")
        print(r"|     \    /     |")
        print(r"|      \--/      |")
        print(r"|~~~~~~~~~~~~~~~~|")
    elif num_wrong == 3:
        print(r"|                |")
        print(r"|                |")
        print(r"|       /\       |")
        print(r"|      /  \      |")
        print(r"|     /-  -\     |")
        print(r"|     \    /     |")
        print(r"|      \--/      |")
        print(r"|       \ \      |")
        print(r"|        ) )     |")
        print(r"|~~~~~~~~~~~~~~~~|")
    elif num_wrong == 4:
        print(r"|       /\       |")
        print(r"|      /  \      |")
        print(r"|     /-  -\     |")
        print(r"|     \    /     |")
        print(r"|      \--/      |")
        print(r"|       \ \      |")
        print(r"|        ) )     |")
        print(r"|       / /      |")
        print(r"|      ( (       |")
        print(r"|~~~~~~~~~~~~~~~~|")
    elif num_wrong == 5:
        print(r"|                |")
        print(r"|                |")
        print(r"|       /\       |")
        print(r"|      /  \      |")
        print(r"|     /-  -\     |")
        print(r"|     \    /     |")
        print(r"|      \--/      |")
        print(r"|       \ \      |")
        print(r"|        ) )     |")
        print(r"|       / /      |")
        print(r"|______( (_______|")
        print(r"|\_____    _____/|")
        print(r"|     / /\ \     |")
        print(r"|    / /  \ \    |")
        print(r"|   / /    \ \   |")
        print(r"|~~~~~~~~~~~~~~~~|")
    elif num_wrong == 6:
        print(r"|       /\       |")
        print(r"|      /  \      |")
        print(r"|     /0  0\     |")
        print(r"|     \    /     |")
        print(r"|      \VV/      |")
        print(r"|       \ \      |")
        print(r"|        ) )     |")
        print(r"|       / /      |")
        print(r"|      ( (       |")
        print(r"|______( (_______|")
        print(r"|\_____    _____/|")
        print(r"|     / /\ \     |")
        print(r"|    / /  \ \    |")
        print(r"|   / /    \ \   |")
        print(r"|  (__)    (__)  |")
        print(r"|~~~~~~~~~~~~~~~~|")


    print(r"|                |")
    print(r" ---------------- ")


# Loads many possible words from a file 
# and returns them as a list
# word_list = LoadWords()
def LoadWords(filename='words.txt', min_length=5):
    words = []
    with open(filename) as f:
        for word in f:
            if len(word) > min_length:
                words.append(word.rstrip())
    return words

def ChooseWord(words):
  # Using random.choice to pick a random word from the list
  return choice(words)

def GetUserInput():
  letter = input('Guess a letter: ')
  '''
  if len(letter) > 1:
    print('You can only guess 1 letter!')
    print()
    return GetUserInput()
  
  if not letter.isalpha():
    print('You can only guess a letter, not a number or symbol!')
    print()
    return GetUserInput()
  '''
  while((len(letter) > 1) or (not letter.isalpha())):
    print('You can only choose 1 letter!')
    print()
    letter = input('Guess a letter: ')

  return letter

def CheckGuess(guess, word, correct, wrong):
  '''
  for letter in word:
    if guess.lower() == letter.lower():
      if guess.lower() in correct:
        continue
      correct.add(guess.lower())

  if guess.lower() not in correct:
    wrong.add(guess.lower())
  '''
  for letter in word:
    if guess.lower() == letter.lower():
      if guess.lower() in correct:
        continue
      correct.append(guess.lower())
  
  if guess.lower() not in correct:
    if guess.lower() not in wrong:
      wrong.append(guess.lower())
    
  return correct, wrong

def DisplayWord(word, correct, wrong):
  display = ''
  display_wrong = ''

  for letter in word:
    if letter in correct:
      display += letter
    else:
      display += '_'
  
  for value in wrong:
    if display_wrong == '':
      display_wrong += value
    else:
      display_wrong += ', ' + value

  print('Word: ' + display + ' | Wrong: [' + display_wrong + ']')

def CheckCorrect(word, correct):
  for letter in word:
    if letter not in correct:
      return False
  
  
  return True

def Main():
  # Starting Sequence
  print('Welcome to the WORD MONSTER game!')
  print()
  print()
  print('A terrible monster is coming! It will only go away if we can guess all the letters in the the word it is thinking of!')
  print('Every letter we get wrong brings the moster closer and closer...')

  word = ChooseWord(LoadWords())
  is_complete = False
  correct_list = set()
  wrong_list = set()
  correct_list = []
  wrong_list = []
  num_wrong = 0

  while is_complete == False:
    PrintMonster(num_wrong)
    print()

    # Checks if game is over
    if num_wrong > 5:
      print('-' * 40)
      print()
      print('NOOO!! The monster is attacking, we are doomed!')
      print()
      print('The word was: ' + word)
      return

    DisplayWord(word, correct_list, wrong_list)
    print()

    CheckGuess(GetUserInput(), word, correct_list, wrong_list)
    num_wrong = len(wrong_list)

    is_complete = CheckCorrect(word, correct_list)
  
  # Winning Sequence
  print()
  print('-' * 40)
  print()
  print('Congratulations! The monster has been pleased :)')
  print()
  print('The word was: ' + word)

############ PROGRAM START ################
Main()