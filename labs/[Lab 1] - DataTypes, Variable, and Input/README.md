# Labs on Replit

## Instructions

Solve all of the following Type Conversion and Error tasks in their respective places in the **main.py** file.

**NOTE:** You should not be doing any arithmetic in your head or on a calculator (except to check your work). Python should be doing all of the computations for you.

**NOTE:** Remember to test your code before submitting!

# 

## Data Types

### Type Conversion Task 1: Float Conversion

**Instructions:**
Can the following string be converted into a float? If so, write the code to convert it to a float and print it to the screen. If not, leave a comment explaining why it cannot be.

    "25"

# 

### Type Conversion Task 2: Int Conversion

**Instructions:**
Can the following string be converted into a int? If so, write the code to convert it to a int and print it to the screen. If not, leave a comment below explaining why it cannot be.

    "14.7"

# 

### Type Conversion Task 3: Un-Stringify

**Instructions:**
***Without removing any quotation marks***, edit the following print statement to make the computer add the numbers as ints, not strings. In other words, change the code so that its output is 17, rather than 314.

    print("3" + "14")

# 

## Data Type Error Fixing Tasks:

Each task below contains some code that fails when run.

1. Copy the broken code into **main.py** and run it, to figure out what's going wrong.
2. Fix the code.
3. Then, leave a comment above the code explaining what was wrong with it and how you fixed it.

# 

### Error Task 1:

    print("My favorite day is December " + 25)

### Error Task 2:

    print(Today is my birthday)

### Error Task 3:

    Print("Some athletes are over " + str(7) + " feet tall!"

### Error Task 4:

    print "Writing Python code is easy"

### Error Task 5:

    print("The type of an int that has been cast to a str is: " + type(str(15)))

## Variables

### Variable Task 1

**Instructions:**
In the comment after the "Variable Task 1:" line in **main.py**, write what the value of hourly_wage is after the last line of code below.

    hourly_wage = 12.5
    print("You just got promoted!")
    hourly_wage = 15

# 

### Variable Task 2

**Instructions:**
In the comment after the "Variable Task 2:" line in **main.py**, write what the value of friend_count is after the last line of code below.

    friend_count = 5
    print("Making some new friends . . .")
    friend_count = friend_count + 2

# 

### Variable Task 3

**Instructions:**
In the comment after the "Variable Task 3:" line in **main.py**, write what the value of days_in_a_year is after the last line of code below.

    days_in_a_year = 365
    new_days_in_a_year = days_in_a_year + 1

# 

### Variable Task 4

**Instructions:**
**In two lines of code**, write a program that creates a variable called hello_world with the value "Hello World!", then prints that variable to the screen.

# 

### Variable Task 5

**Instructions:**
**In three lines of code**, write a program that creates a variable called my_number with the float 5.5 as its value, then creates a variable called my_number_type which contains the type of that number, then prints my_number_type to the screen.

# 

## Variables Error Fixing Tasks:

Each task below contains some code that fails when run.

1. Copy the broken code into **main.py** and run it, to figure out what's going wrong.
2. Fix the code.
3. Then, leave a comment above the code explaining what was wrong with it and how you fixed it.

# 

### Error Task 1:

    1st_name = "Miles"
    print("My first name is " + 1st_name)

### Error Task 2:

    favorite_day = 25
    print("My favorite day is December " + favorite_day)

### Error Task 3:

    my_number = str(14)
    print("my_number is: " + My_Number)

### Error Task 4:

    my_float = 15.0
    print = "my_float is: " + str(my_float)
    print(print)

# 

## Translate Psuedocode to Python
You'll be translating pseudocode functions into actual, working Python code. Look through the two examples below, then scroll down to the homework problems and use the same principles to translate the pseudocode into Python.

#

*Here are **two example solutions** to example tasks. **There's no need to complete these tasks**; instead, use them as inspiration for completing your tasks below:*

### Example Translation 1: Birthday Printer

**Pseudocode:**

    Start
      input birth_month
      input birth_day
      print "[birth_month]/[birth_day]"
    End

**Translated to Python (solution):**

    month = input("Enter your birth month (as a number): ")
    day = input("Enter your birth day (as a number): ")
    print(month + "/" + day)

**Example Run #1**
##### Input:

    Enter your birth month (as a number): 2
    Enter your birth day (as a number): 16

##### Output:

    2/16

**Example Run #2**
##### Input:

    Enter your birth month (as a number): 8
    Enter your birth day (as a number): 12

##### Output:

    8/12


### Example Translation 2: Number Adder

**Pseudocode:**

    Start
      input first_number
      input second_number
      print first_number + second_number
    End

**Translated to Python (solution):**

    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter a second number: "))
    print(first_number + second_number)

**Example Run #1**
##### Input:

    Enter a number: 24
    Enter a second number: 16

##### Output:

    40

**Example Run #2**
##### Input:

    Enter a number: 3
    Enter a second number: 5

##### Output:

    8
# 

## Your Tasks

**NOTE:** Whenever you see brackets inside of a string in pseudocode (e.g. "this is my number: [my_number]"), that means you should replace what's in the brackets with the variable it represents. You should not print the brackets.  

**NOTE:** Remember to test your code before submitting!

# 

### Translation Task 1: Exponent Machine

**Instructions:**
Implement the following pseudocode in Python in **main.py**.

**Pseudocode:**

    Start
      input number
      input exponent
      print number^exponent
    End

**Example Run #1**
##### Input:

    Please enter a number: 2
    Please enter an exponent: 5

##### Output:

    32

**Example Run #2**
##### Input:

    Please enter a number: 4
    Please enter an exponent: 2

##### Output:

    16

# 