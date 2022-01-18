# Task 1
is_hungry = False
if is_hungry == True:
  print("I am really hungry!")
else:
  print("I'm not too hungry right now.")


# Task 2
wants_joke = input("Type yes if you'd like to hear a joke! ").lower()
if wants_joke == "yes":
  print("Question: What do you call bears with no ears?")
  print("Answer: b")
else:
  print("Nevermind!")


# Task 3
num_kids = int(input("How many kids showed up? "))
num_toys = int(input("How many toys do we have? "))

if num_kids == 0:
  print("No kids showed up!")
else:
  toys_per_kid = num_toys // num_kids
  print("Each kid gets " + str(toys_per_kid) + " toys.")
  

# Task 4
is_finished = False
if is_finished:
  print("I am all done!")
else:
  print("I\'m still working on it.")


# Task 5
height_in_feet = float(input("How many feet tall are you? "))
if height_in_feet >= 6:
  print("You're taller than average!")
elif height_in_feet <= 4:
  print("You're shorter than average!")
else:
  print("Your height is pretty average.")