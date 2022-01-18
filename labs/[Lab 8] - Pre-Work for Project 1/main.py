'''
Algorithm:

  Asks the user for the maximum_value (must be positive integer)

  Generate random_value between 0 and maximum_value

  While guess doesn't equal random_value (false):
    Ask user for guess between 0 and maximum_value

    If guess equals random_value, return True 

    If guess is greater than random value:
      Print "That's too high"

    Otherwise:
      Print "That's too low"
  
    Add 1 to guess_count
  
  After user guesses the correct value, print guess_count

Functions:

  A function to get user input for maximum_value
  A function to get random_value
  A function to check if value is correct
  A function to print the guess count
'''