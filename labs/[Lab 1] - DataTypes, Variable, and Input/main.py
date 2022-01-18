.3# Lab - Numbers, Data Types, Variables, Input
# Write the names of the members of your breakout group here:
#   1. (myself)
#   2.
#   3.
#   4.

#########################################################
# Data Types ############################################
#########################################################

# Type Conversion Task 1: Float Conversion
print(float("25"))


# Type Conversion Task 2: Int Conversion

#You cannot convert this string to a int because an int cannot be a decimal

# Type Conversion Task 3: Un-Stringify
print(int("3") + int("14"))


# Error Task 1:
print("My favorite day is December " + str(25))

# Could not concatonate an integer with a string
# Converted integer to string

# Error Task 2:
print("Today is my birthday")

# Cannot print values that aren't assigned
# Added quotes

# Error Task 3:
print("Some athletes are over " + str(7) + " feet tall!")

# Print is not a function and parentheses were not closed
# Fixed print function and closed parentheses

# Error Task 4:
print("Writing Python code is easy")

# Missing parentheses
# Added parentheses

# Error Task 5:
print("The type of an int that has been cast to a str is: " + str(type(str(15))))

# Could not concatenate type onto string 
# Converted type value into string

#########################################################
# Variables #############################################
#########################################################

# Variable Task 1:
# Final value of hourly_wage: 15


# Variable Task 2:
# Final value of friend_count: 7


# Variable Task 3:
# Final value of days_in_a_year: 366


# Variable Task 4:

hello_world = "Hello World!"
print(hello_world)


# Variable Task 5:

my_number = 5.5
my_number_type = type(my_number)
print(my_number_type)

# Variable Error Task 1:

first_name = "Miles"
print("My first name is " + first_name)

# Variable name cannot contain Numbers
# Replaced numbers with letters

# Variable Error Task 2:

favorite_day = 25
print("My favorite day is December " + str(favorite_day))

# Cannot concatonate int to String 
# Converted favorite_day to string

# Variable Error Task 3:

my_number = str(14)
print("my_number is: " + my_number)

# My_Number is not the same as my_number
# Fixed capitalization of my_number

# Variable Error Task 4:

my_float = 15.0
value = "my_float is: " + str(my_float)
print(value)

# Cannot have print (or other functions) as a variable name 
# Changed variable name to value

#########################################################
# Psuedocode ############################################
#########################################################

# Translation 1: Exponent Machine

number = int(input("Please enter a number: "))
exponent = int(input("Please enter an exponent: "))
print(number ** exponent)