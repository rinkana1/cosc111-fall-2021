#

# Lab 3 - Text Shapes!

## Instructions
You and your group will complete 4 different tasks, where each task requires you to print characters in a way that "draws" a shape.

You must ask the user, as `input`, for the size of each shape to draw.

### Hints
* For drawing each row, consider using *string \* int* to repeat the string/character multiple times.
* Think about what we've learned about For Loops! Can we use them to *print()* multiple rows a certain number of times?
* Use a consistent character as your "pen". In the examples below, we'll use *"XX"*.
* For the more complicated shapes, you may have to adjust the amount of characters printed in each row depending on what iteration you are in the Loop.

#

### Task 1 - Draw Square

Get the size of the square as input, then print a square in the terminal. Example output:

    What size square? 10
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

#

### Task 2 - Draw Right Triangle

Get the size of the triangle as input, then print a right triangle in the terminal. Example output:

    What size triangle? 10
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

#

### Task 3 - Draw Hollow Square

Get the size of the square as input, then print a hollow square in the terminal. Example output:

    What size square? 10
    XXXXXXXXXXXXXXXXXXXX
    XX                XX
    XX                XX
    XX                XX
    XX                XX
    XX                XX
    XX                XX
    XX                XX
    XX                XX
    XXXXXXXXXXXXXXXXXXXX

#

### Task 4 - Draw A Diamond

Get the size of the diamond as input, then print a diamond in the terminal. Example output:

    What size diamond? 10
                    
            XXXX        
          XXXXXXXX      
        XXXXXXXXXXXX    
      XXXXXXXXXXXXXXXX  
    XXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXX  
        XXXXXXXXXXXX    
          XXXXXXXX      
            XXXX  