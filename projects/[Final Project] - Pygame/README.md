# Final Project - Pygame

**Congratulations!** This is the final project! You're almost there!

**We will build a Graphics-based Program/Game!**

Don't worry, most of the code will be provided for you. You will simply need to get the code running, and then add something new to it!

You may work in teams of one or two! The larger your team, the more is expected of you however. Make sure to read ALL the instructions!

Write the names of EACH team member at the top of EACH project file.

**NOTE** EACH person must contribute in some way! An individual's grade will be adjusted according to how the other person rated them. I will be sending out a survey to ask each group member privately to rate each other.

---
## **Part 1: Pygame Tutorial (50% of grade)**
---
Make sure to download the PDF for the tutorial. It is linked here, but can also be found on Canvas-->Modules. This tutorial will walk you step by step through THREE small programs, in THREE chapters! The code and explanations are all provided in the tutorial, you simply need to read through it and get the code up and running here in repl.it.

Note No need to worry about "installing pygame". Repl.it already has it installed. You just need to import it at the top of the python file:

```py
import pygame
```
### **No main.py**

If you notice on the left, there is NO main.py. Instead there are several Python files, an image, and a folder with an example (for extra credit).

Each of the three main programs in each chapter of the tutorial should be implemented in one of these three files:

```
(Chapter 8) SmileyBounce --> smiley_bounce.py
(Chapter 9) DragDots --> drag_dot.py
(Chapter 10) SmileyPong --> smiley_pong.py
```

It should automatically run the program in show_dot.py and you should see something like this load in Repl.it:

You may have to move the UI panel around to make room for it!

### **Part 1 Requirements**

* **Implement the three programs as described in the tutorial.** The tutorial gives you all the code and walks you through each line, step by step! Part 1 is to just get the programs working!

* **Your program should NOT crash with any syntax or runtime errors!** You program should not crash. Syntax errors will receive zero points, and runtime errors will cause a significant loss in your grade. Make sure to test your program with MANY different inputs!

---
## **Part 2: Add Something of Your Own (50% of grade)**
---
After completing part 1, you should have three working programs!

* A bouncing animation (`smiley_bounce.py`)
* A drawing program (`drag_dots.py`)
* A pong game (`smiley_pong.py`)

**For each person in your group**, choose one of these programs and add modifications of your own! Change it in some way. Add more capabilities, add new features, change the behavior. **Include the use of a list AND a dictionary!.** Describe your changes at the top of each file you added new features to!

### **Change one program For EACH person in your group!**

If there is only one of you, only one program needs to be modified by you. If there are two people in your group, then you need to modify two programs.

### **Examples**

What are some examples of ways you could change the program?

* `smiley_bounce.py`
    * Use a dictionary to group the smiley's attributes into a single data structure. For example, to group a smiley's picx,picy, speedx, and speedy data together (and reference the dictionary throughout the code instead):

    `smiley = { "picx": 0, "picy": 0, "speedx": 5, "speedy": 5 }`

    * Use a `list` to keep track of multiple bouncing faces, not just one!
    * Upload your own image for the smiley!
    * Add keyboard input to change the speed on the smiley (see below for keyboard input)

* `drag_dots.py`
    * Allow the user to choose different colors (see keyboard input below)
    * Use a list to keep track of available colors
    * Allow the user to draw different sized dots (bigger or smaller)
    * Enable the user to clear the screen if they press a certain key.
    * Let the user save the image to a file! For example, you could execute this line of code if the user presses a certain key:

    `pygame.image.save(screen, "screenshot.jpeg")`

* `smiley_pong.py`
    * Use a different image for the face.
    * You could make things progressively harder by speeding up the smimely, or you could shrink the paddle bit by bit.
    * Add more than one smiley!
    * Use a dictionary to keep track of smiley's attributes/variables.
    * Use a dictionary to keep track of the paddle's attributes/variables too.
    * Use different colors.
    * Use multipe images for the smiley that alternate to create facial animations.

The above are just ideas, feel free to do something on your own! There is no hard and fast rule here, but I do need to see that you somehow made these programs your own in some way. And you must use a LIST and DICTIONARY in some way.

---
### **Keyboard Input**

The tutorial explains mouse inputs pretty well. For keyboard inputs, you could exectute this line of code inside the game (while) loop:

```py
keys = pygame.key.get_pressed()
```
Keys now holds a list of booleans, one for each key on a keyboard. While a key is pressed, it's correspondng boolean value in the list is `True`. In the game loop, you can check if a particular key is `True` and do something. For example:

```py
keys = pygame.key.get_pressed()

if keys[pygame.K_r]: # they key 'r' was pressed
    # Do something
  
if keys[pygame.K_LEFT]: # Left arrow was pressed
    # Do something
```
---
### **Part 2 Requirements**

* For EACH person in your group, modify one of the programs from part 1. How you modify it is up to your group.
* Your modifications should make use of a list and a dictionary somehow. I want to see you use both a list and a dictionary.
* Describe your changes/additions at the top of each file. There is a comments section at the top, please describe what you changed so I don't have to look for it.
* Have fun with it! Seriously, this should be a fun project. Celebrate what you've learned by creating something cool!

---
## **Part 3: Optional Extra Credit (8+% of total class grade)**
---

Create you OWN game! You can certainly start with any of the three programs as a base, then modify it heavily enough that it becomes it's own game! This part is purely up to you! Use the principles we've learned in class, and resources online with Pygame to make your own creation!

To get the extra credit, you must get your idea APPROVED ahead of time with me.

Then later PASS OFF the game with me!

It must be your own game. No direct copy paste of an entire game from the internet. Though, you may look for several examples on the internet as a starting point, or to figure out how to do certain things.

The scope of the game is not high, look at my example game to see what I would expect to get extra credit.

## **Python Coding Style**
---

As mentioned, the project must be implemented in a way that uses good programming style and best practices as discussed in class, and in the reading on Python Style Guide. When you pass off the project, we'll particularly look for:

* Did you use functions to help organize your code, avoid code duplication, and improve code readability?
* Are your variable and function names useful and informative?
* Did you make good use of whitespace to organize your code and make it more readable?