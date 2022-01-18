# Instructions

Complete the tasks below in **main.py**. All work must be done individually.

**NOTE:** Remember to test your code before submitting!

There are unit tests to run for each homework. To make it automated, each unit test looks for the exact output expected for each task. Makes sure all unit tests pass before submitting your homework.

**Important:** You will be graded for completing the tasks as instructed. Not only do the test cases have to pass, but we will check over the code to see that you followed directions.

**Note 2** Don't use more `input()` functions than you have to---only what is asked for in the tasks below.

#

## Your Tasks

### Task 1: Smallest Number

**Instructions:**
Take two numbers as **input from the user** (use the `input()` function), and print the smallest one. 

**Example 1**
##### Input:

    What is your first number?: 30
    What is your second number?: 20

##### Output:

    20

**Example 2**
##### Input:

    What is your first number?: 5
    What is your second number?: 8

##### Output:

    5

# 

### Task 2: Date Validator

**Instructions:**
Take three ints as **input from the user** (use `input()` function for each), a year, a month, and a day. Then, verify that the date is valid. Conditions for a valid date:

* The year is between 1900 and 2020
* The month is between 1 and 12
* The day is between 1 and 31

If the year is invalid, print "Invalid Year". Otherwise, print "Valid Year"

If the month is invalid, print "Invalid Month". Otherwise, print "Valid Month"

If the day is invalid, print "Invalid Day". Otherwise, print "Valid Day"

**Example 1**
##### Input:

    What is the year?: 1999
    What is the month?: 18
    What is the day?: 4
    
##### Output:

    Valid Year
    Invalid Month
    Valid Day
    

**Example 2**
##### Input:

    What is the year?: 300
    What is the month?: 8
    What is the day?: 32
    
##### Output:

    Invalid Year
    Valid Month
    Invalid Day
    
# 

## Task 3: String Comparer

**Instructions:**
Read in two strings from **user input** (use the `input()` function) and assign them to variables called `string1` and `string2`. If the two strings are equal, print the following:

    You said the same thing both times.

Otherwise, print the following (replacing what's in angle brackets below with the actual variables):

    You said <string1> and then <string2>.

**Example Run 1:**

    What is your first string?: Hello, my friend
    What is your second string?: Hello, my friend
    You said the same thing both times.

**Example Run 2:**

    What is your first string?: Here you go
    What is your second string?: Here's another
    You said Here you go and then Here's another.

# 

### Task 4: Water State Determiner

**Instructions:**
Read in **input from the user** (use `input()` function) asking for the water temperature, and print out whether it is ice (temperature below 32), water (temperature between 32 and 212), or steam (temperature above 212), in the following format:

    Water at that temperature is [state]


**Example Run 1:**

    What is the temperature of your water?: 250
    Water at that temperature is steam

**Example Run 2:**

    What is the temperature of your water?: 45
    Water at that temperature is water

#

### Task 5: Print True

**Instructions:**
There is existing code in main.py (and below). Modify the value of the boolean variables such that the conditional expression resolves to True, and the program prints:

    Boolean expression is True!

**Note:** Do not modify the expression, only the value of the variables.

    A = False
    B = False
    C = False
    D = False

    if (A or B) and (C or D) and not (A and not D):
        print("Boolean expression is True!")
    else:
        print("Boolean expression is False.")

# 

## Task 6: Print Shorter String

**Instructions:**
Read in two strings from **user input** (use `input()` function for each) and assign them to variables called `first_string` and `second_string`. If `first_string` is a shorter **length** than  `second_string`, print the following:

    <first_string> is shorter

If the second string has a shorter length than the first string, print:

    <second_string> is shorter

If the two strings are of equal length, print:
    
    Both strings are the same length!

**Example Run 1:**

    What is your first string?: this is short
    What is your second string?: this is loooooonger
    this is short is shorter

**Example Run 2:**

    What is your first string?: I love this class!
    What is your second string?: definitely 
    definitely is shorter

**Example Run 3:**

    What is your first string?: my random string
    What is your second string?: the other string
    Both strings are the same length!