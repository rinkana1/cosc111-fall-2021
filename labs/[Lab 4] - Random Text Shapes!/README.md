#

# Lab 4 - Random Text Shapes!

## Instructions
You will complete the following tasks. Each task leads into the next, so do them in order.

#

### Task 1 - Draw Square

**Instructions:**
Write a function that draws a square of random size, between 5 and 30. This should work very similar to Lab 3.

 Example function call:

    DrawRandomSquare()

Internally, the function randomly selects the square size and outputs (say size is 10):

    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX

Or, since it's a random size, another call could output (say size is 5):
    
    XXXXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXX

#

### Task 2: Draw Right Triangle

**Instructions:**
Same as the last task, but draw a right triangle. Have the function choose a random size, between 5 and 30, for the triangle.

Example function call:

    DrawRandomTriangle()

Internally, the function randomly selects the triangle size and outputs (say size is 10):

    XX
    XXXX
    XXXXXX
    XXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXXXX
    XXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX

Or, since it's a random size, another call could output (say size is 6):
    
    XX
    XXXX
    XXXXXX
    XXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXXXX

#

### Task 3: Draw Random Shape

**Instructions:**
Write a function that will randomly choose either a square or a triangle and then draw the shape by calling your functions defined from above.

Example function call:

    DrawRandomShape()

Internally, the function randomly selects whether to draw a triangle or a square and outputs (say triangle):

    XX
    XXXX
    XXXXXX
    XXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXXXX
    XXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXX

Or, since it's a random size, another call could output (say square):
    
    XXXXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXX

#

### Task 4: Ask For Shape

**Instructions:**

Write a program that asks the user if they want a "triangle", a "square", or a "surprise".
* If the user inputs "triangle", call your triangle function to print it.
* If the user inputs "square", call your square function to print it.
* If the user inputs "surprise", call your random shape function to print either a square or triangle at random.
* If the input is neither of those options, then print:


     OK, I won't print anything then.

**Example Execution:**

    What would you like to print?
    0 - square
    1 - triangle
    2 - surprise

    Enter choice: 1

    XX
    XXXX
    XXXXXX
    XXXXXXXX
    XXXXXXXXXX
    XXXXXXXXXXXX
    XXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXX