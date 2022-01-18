# Instructions

Each task will require you to define a function. Complete the tasks below in **main.py**. All work must be done individually. 

Now that we are now writing functions, and the tests will be checking each function's output individually, which means that your function names are important. If you don't **name your functions exactly as indicated below**, the tests will not pass.

**NOTE:** Remember to test your code before submitting!

#

## Your Tasks

### Function 1: Dice Roll

**Instructions:**
Define a function called **DiceRoll()** that **returns** a random number from 1 to 6.

**HINT 1:** You'll have to add an import statement to the top of main.py.

**HINT 2:** Your function should not need to **print** anything, it should just **return** the result!

# 

### Function 2: Double Dice Roll

**Instructions:**
Define a function called **DoubleDiceRoll()** that uses the **DiceRoll() function from Task 1** to roll two dice, then returns the result of adding those dice rolls together.

For example, if the first DiceRoll() returns 3 and the second DiceRoll() returns 4, this function should return 7.

#

### Function 3: Odd Integers

**Instructions:**
Define a function called **GetOddIntegersTo100()** that returns a list containing only odd numbers within the range from 0 to 100. E.g., a list containing:

    [1, 3, 5, ..., 97, 99]

**Hint:** Use a for loop to append numbers to the list one by one, and then simply return the list. Use the range() function that starts at 1, ends at 100, and increments by 2.