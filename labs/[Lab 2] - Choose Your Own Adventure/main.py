# Lab 2 - Choose your own adventure.
# Write the names of the members of your breakout group here:
#   1. (myself)
#   2.
#   3.
#   4.

print("Welcome to choose your own adventure game!")

print("An evil monster has attacked the kingdom! Do you run away from the monster (1) or fight the monster (2)")

decision1 = input("Decide here: ")

if decision1 == "1":
  print("You ran away from the monster. He took the princess to his evil lair!")

  print("Do you want to chase after the monster (1) or stay behind (2)")
  decision2 = input("Decide here: ")

  if decision2 == "1":
    print("You chased the monster and saved the princess! She didn\'t fall in love with you because you\'re a coward, but the kingdom still lived happily ever after.")
  elif decision2 == "2":
    print("You\'re a terrible person -_-")
  else:
    print("This isn\'t a valid choice.")
elif decision1 == "2":
  print("You were injured in battle and the monster took the princess to his evil lair.")

  print("You are injured. Do you want to chase after the monster (1) or stay back and heal (2)?")
  decision2 = input("Decide here: ")

  if decision2 == "1":
    print("You died from blood loss. You should\'ve went to the doctor :(")
  elif decision2 == "2":
    print("You healed and then chased the monster and saved the princess! She fell in love with you and the kingdom lived happily ever after.")
  else:
    print("This isn\'t a valid choice.")
else:
  print("This isn\'t a valid choice.")