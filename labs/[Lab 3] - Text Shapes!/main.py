# Lab 3 - Text Shapes!

# Task 1: Draw Square
square = int(input('Enter square size: '))
for index in range(square):
  print('X' * square)

# Task 2: Draw Right Triangle
triangle = int(input('Enter triangle size: '))
for index in range(triangle):
  if index == 0:
    print('X')
  else:
    print('X' * (index * 2))

# Task 3: Draw Hollow Square
hollow_square = int(input('Enter square size: '))
for index in range(hollow_square):
  if index == 0:
    print('X' * (hollow_square))
  elif index == (hollow_square - 1):
    print('X' * hollow_square)
  else:
    print('X' + (' ' * (hollow_square - 2) + 'X'))

# Task 4: Draw Diamond
diamond = int(input('Enter diamond size: '))
if diamond % 2 == 0:
  for index in range(diamond):
    if index / diamond < 0.5:
      print((' ' * ((diamond - index) - 5)) + ('X' * ((index * 2) + 1)))
    else:
      print((' ' * (index - 3)) + ('X' * (((diamond - index) * 2) - 3)))
else:
  for index in range(diamond):
    if index / diamond < 0.5:
      print((' ' * ((diamond - index) - 5)) + ('X' * ((index * 2) + 1)))
    else:
      print((' ' * (index - 4)) + ('X' * (((diamond - index) * 2) - 1)))