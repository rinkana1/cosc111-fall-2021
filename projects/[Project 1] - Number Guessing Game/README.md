# **Project 1 - Number Guessing Game**

Understand the problem below and design and implement the solution in main.py.

**All work must be done individually.**

There will be NO tests for the projects. Part of the project will be to understand the problem well enough to design a complete solution. **That means understanding when your code fullfills all the requirements!**

To this end, in order to receive credit on projects, your project MUST be complete and run WITHOUT ERRORS. I highly recommend **visiting with a TA or the Instructor to turn in the project!** This means coming to either TA or instructor office hours and do so either in person, or virtually. We'll grade it on the spot!

The TA or the Instructor will verify that your program meets the requirements and also look over your code for any major style issues. If your project fails to meet the criteria, you can keep working on the project until you can successfully pass it off. Late projects will be docked %15.

**NOTE:** Remember to test your code yourself before submitting/passing it off.

---
## **Number Guessing Game**
---
In this project, we'll be implementing a number guessing game!

### **How The Game Works**

* The program asks the user for the maximum value a number could be (postive integer).
* The program randomly chooses an integer between 0 and the maximum number.
* The user then has to guess what the number is.
* The user enters a guess.
* After each guess, the program tells the user whether their guess is too high, or too low.
* The user keeps guessing until they get the correct number.
* The program outputs the total number of guesses it took.

Here is an example run of what the program output and interaction could be:

**Example 1:**
```
Welcome to the Number Guessing Game!

Enter the maximum value: 10

OK! I've thought of a number, try to guess what it is!
Enter guess: 5

Too High!
Enter guess: 3

Too High!
Enter guess: 2

Too High!
Enter guess: 1

Hey! You got it! The number was: 1

Took you 4 guesses.
Welcome to the Number Guessing Game!

Enter the maximum value: 10

OK! I've thought of a number, try to guess what it is!
Enter guess: 5

Too High!
Enter guess: 3

Too High!
Enter guess: 2

Too High!
Enter guess: 1

Hey! You got it! The number was: 1

Took you 4 guesses.
```

**Example 2:**
```
Welcome to the Number Guessing Game!

Enter the maximum value: dfd

It must be a positive number!
Enter the maximum value: 100

OK! I've thought of a number, try to guess what it is!
Enter guess: 50

Too High!
Enter guess: 25

Too Low!
Enter guess: 35

Too Low!
Enter guess: 45

Too High!
Enter guess: 40

Too Low!
Enter guess: 42

Hey! You got it! The number was: 42

Took you 6 guesses.
Welcome to the Number Guessing Game!

Enter the maximum value: dfd

It must be a positive number!
Enter the maximum value: 100

OK! I've thought of a number, try to guess what it is!
Enter guess: 50

Too High!
Enter guess: 25

Too Low!
Enter guess: 35

Too Low!
Enter guess: 45

Too High!
Enter guess: 40

Too Low!
Enter guess: 42

Hey! You got it! The number was: 42

Took you 6 guesses.
```
---
## **Project Requirements**

* Implement the game as described above. You should more or less follow similar flows as the example outputs above.

* The exact text to use in printing the output is up to you. Feel free to have fun with the wording, spacing, etc.

* You must ask the user for the maximum number. This should be a postitive integer. The program should NOT just crash if the user enters in non-number characters. Instead, the program should ask the user to enter the number again until they enter in a valid number (postive integer).

* The computer must choose a random number from 0 to the maximum number.. Don't print this number to user, the user must guess what this number is.

* Each user guess should be an integer. If the user enters in a non-number, the program should NOT just crash, but should ask the user to enter in their guess again.

* The program repeatedly asks the user for a guess until they guess the correct number. If a particular guess is less than the randomly chosen number, then tell the user it's "too low". If the the guess is greater, then tell the user "too high".

* Print the number of guesses it took the user. Tell the user how many guesses it took.

* You must use good programing best practices. This primarily comes down to good use of functions and variable naming! There is no hard and fast rule here. However, you won't receive full credit if there are NO functions, or if the variable names don't make any sense at all.

* Your program should NOT crash with any syntax or runtime errors! You program should not crash. Syntax errors will receive zero points, and runtime errors will cause a significant loss in your grade. Make sure to test your program with MANY different inputs!

Optional Requirements

* Ask the user if they want to play again. When the game is over (after the user has guessed the correct number), instead of ending the program, ask the user if they want to play again. If so, start the game over again. This should all happen without exiting the program.

### **Python Coding Style**

As mentioned, the project must be implemented in a way that uses good programming style and best practices as discussed in class, and in the reading on Python Style Guide. When you pass off the project, we'll particularly look for:

* Did you use functions to help organize your code, avoid code duplication, and improve code readability?
* Are your variable and function names useful and informative?
* Did you make good use of whitespace to organize your code and make it more readable?

**Hints**

* START EARLY! It will be very hard to finish this just the day it is due. Programming ALWAYS takes longer than you think.
* Pass off the project with a TA or the instructor. They will grade it on the spot for you! Or provide helpful advice and feedback!
* Remember, projects are about making use of multiple concepts we've learned so far in class.
* Consider concepts like while loops, random, conditionals, functions, etc.
* Develop a PLAN first. Write out in English the steps your program will need to take. If you're struggling with this, think about how you would explain the rules of this game to another person.
* Break up parts of the program into functions. For example, you might have a function whose purpose is to get a postive integer from the user---without crashing on non-numerical input. This function could then be used in multiple places, like getting the user's guess and also for getting the max number from the user.