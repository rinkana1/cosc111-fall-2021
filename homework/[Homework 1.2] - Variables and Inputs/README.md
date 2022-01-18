# Homework 1.2

In this course, homework assignments will usually look something like this. There will be a list of tasks, each with instructions. Your job is to go over to **main.py** and complete each task underneath its label.

Here's an example solution to a made-up task:

    # Example Task: Get the user's name as input, store it in a variable and print it.

    name = input("Please provide your name: ")
    print("Your name is: " + name)
    
When you've finished this assignment, you should have a lot of lines in **main.py** that look something like the above.

# 

**NOTE:** Remember to test your code before submitting!

There are unit tests to run for each homework. To make it automated, each unit test looks for the exact output expected for each task. Makes sure all unit tests pass before submitting your homework.

# 

## Variables and Inputs

### Task 1: Triple Double

**Instructions:**
Take the variable defined below and double it three times, each time storing the result back into the original variable. Print the final result.

    growing_number = 15

# 

### Task 2: Value Swap

**Instructions:**
Print the values of the two variables defined below. Then, swap their values so that the first variable contains the original value of the second, and vice-versa. Print them again.

    first_number = 5
    second_number = 8

#

### Task 3: Five and Two:
**Instructions:**
Assign a variable named *five* to the value 3 and a variable named *two* to the value 7, and print the result of multiplying them together. Remember, there's nothing magic about variables' names to a computer, but choosing good ones makes your program much more readable by other humans.

#

### Task 4: Assign New Value

** Instructions**
Modify the code to assign the variable *current_year* to the current year (2021). Then print out the concatination of the variable to the end of the following string:

    "Current year is: "

Expected output:
    
    Current year is: 2021

#

### Task 5: Input Birth Year

**Instructions**
Modify the code to have the variable *birth_year* receive its value as input from the terminal instead of being assigned 0.

Concatentate the variable to the end of the following string: 

    "You were born in: "

Print the result---expected output:

    You were born in: <birth_year>

**NOTE:** You should not print the angle brackets above themselves - *<>* - instead you should replace the brackets and their contents with the proper variable.

#

### Task 6: Calculate Current Age:

**Instructions**
Calculate the person's age by subtracting *birth_year* from *current_year* (variables from last two tasks), and print out the result using the following string:

    Your age is: <age>

#

### Task 7: Total Ticket Cost:

**Instructions**
Receive as input from the terminal the following three items:

    show_name
    cost_per_ticket
    num_tickets

Calculate the total cost of all the tickets (mutiply *cost_per_ticket* by *num_tickets*), and print the total cost (with a $ sign) and a farewell note using the *show_name*. The expected output should look like this:

    Total price for <num_tickets> is $<total_cost>
    Enjoy <show_name>!

# 

### HINTS

The unit tests act as the autograder. If everything passes, you will receive full credit! The tests look for exact answers, so you'll need to make sure the strings you use for printing results match exactly. Exact capitalization, punctuation, and spaces.