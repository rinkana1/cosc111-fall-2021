# Lab 7 - Refactor Palidromes

# Function to get input
def GetInput():
  print()
  print("Please enter a palindrome string consisting only of letters (no spaces, numbers, or punctuation).")

  text = input("Enter: ").lower()

  while not text.isalpha():
    print(text + " must only contain letters! Try Again!\n")
    text = input("Enter: ").lower()
  
  return text

# Function to check if text is a palindrome
def IsPalindrome(text):
  is_palindrome = True
  s = 0
  e = len(text) - 1

  while s < e:
    if text[s] != text[e]:
        is_palindrome = False

    s += 1
    e -= 1

  if is_palindrome:
    return text

  else:
    print(text + " is not a palindrome. Try again!")
    return IsPalindrome(GetInput())

# Program Start

print("Hello! Welcome to the Palindrome Checker!")

palindrome1 = IsPalindrome(GetInput())
palindrome2 = IsPalindrome(GetInput())

if palindrome1 == palindrome2:
    print("You entered the same palendrome twice!")
else:
    print("You entered:")
    print(palindrome1)
    print("Then:")
    print(palindrome2)

# Program End