# Lab 8 - Pre-Work For Project 1

## **Instructions**
---

Read the `Project 1 - Number Guessing Game` instructions carefully!

This Lab is about understanding what that project is asking for, and **writing down a plan/algorithm in English!**

You MUST read the full instructions on the project page, but here is a summary of the number guessing game:

### **How The Game Works**

* The program asks the user for the maximum value a number could be (postive integer).
* The program randomly chooses an integer between 0 and the maximum number.
* The user then has to guess what the number is.
* After each guess, the program tells the user whether their guess is too high, or too low.
* The user keeps guessing until they get the correct number.
* The program outputs the total number of guesses it took.

## **Pre-Work Task**
---

Your task for this Lab is to **outline your plan for implementing Project 1.**

In other words, develop an algorithm for implementing the project and write it down here in English/Psuedocode (write it in **main.py**).

* Describe each step you'll need to take. For example, one step could be:
    * "Get user input for the maximum number", or
    * "Repeat the following until..."
* Review the properties of a good algorithm (first two weeks of class).
* Describe each function you'll plan on defining. For example:
    * You might have a function for getting the user input and making sure it's a positive integer.

If you're having trouble, think about how you would explain this game to your sibling or parent or friend.

Don't get hung up on the details just yet, this is just an exercise to help you break down a larger problem into smaller parts. You are welcome to go into details more if you'd like, however.

You may not know all the functions you'll need just yet, but do at least try to think about how you'll break the problem down into functions. It's OK if things change later when you actualy go to implement it.

Below is an example (of a different problem) of what is expected for this lab:

---
## **Example - Rock Paper Scissors**
---

**Algorithm:**

```
Ask the user for the number of rounds
    (To play the best out of)
  
Repeat the following until the user's score OR the computer's score is greater than half the number of rounds:
  
    Play a round of rock paper scissors:
        Get the user's choice (rock, paper, or scissors)
        
        Get the computer's choice (rock, paper, or scissors)
        
        Determine who the winner is
        
        Print the results of the round
        
    Update the user's/computer's scores from the round
  
Print the final results
Ask the user for the number of rounds
    (To play the best out of)

Repeat the following until the user's score OR the computer's score is greater than half the number of rounds:

    Play a round of rock paper scissors:
        Get the user's choice (rock, paper, or scissors)

        Get the computer's choice (rock, paper, or scissors)

        Determine who the winner is

        Print the results of the round
    
    Update the user's/computer's scores from the round

Print the final results
```

**Functions:**

* A function to play a single round of rock paper scissors
* A function to get the user's choice
* A function to get the computer's choice
* A function to determine the winner
* A function to print the round results nicely
* A function to print the final results nicely
* A function to play a single round of rock paper scissors
* A function to get the user's choice
* A function to get the computer's choice
* A function to determine the winner
* A function to print the round results nicely
* A function to print the final results nicely

---
### **Computational Thinking**

* **Decomposition**
    * Break the problem into parts
* **Pattern Recognition**
    * Identify patterns and trends
* **Abstraction**
    * Generalize patterns into a rule
* **Algorithm Design**
    * Design methods to solve problems

### **Properties of a Good Algorithm**

* **Inputs and Ouputs**
    * Specify any required inputs or outputs
* **Finite**
    * The algorithm must have an end
* **Definite**
    * Each step much be precise and unambiguous
* **General**
    * It should solve a class of problems, not just a specific one.