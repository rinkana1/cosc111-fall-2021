# Lab 4 - Random Text Shapes
import random

# Task 1: Print Square
def DrawRandomSquare():
  square = random.randint(5, 30)
  for i in range(square):
    print('X' * square)

#DrawRandomSquare()

# Task 2: Print Triangle
def DrawRandomTriangle():
  triangle = random.randint(5, 30)
  for i in range(triangle):
    print('X' * (i * 2))

#DrawRandomTriangle()

# Task 3: Print Random Shape
def DrawRandomShape():
  decision = random.randint(0, 1)
  if decision == 0:
    DrawRandomSquare()
  else:
    DrawRandomTriangle()

#DrawRandomShape()

# Task 4: Ask For Shape
print('What would you like to print?\n0 - square\n1 - triangle\n2 - surprise')
choice = int(input('Enter choice: '))

if choice == 0:
  DrawRandomSquare()
elif choice == 1:
  DrawRandomTriangle()
elif choice == 2:
  DrawRandomShape()
else:
  print('OK, I won\'t print anything then.')