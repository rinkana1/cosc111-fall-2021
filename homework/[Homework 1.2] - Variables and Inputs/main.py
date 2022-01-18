# Task 1: Triple Double
growing_number = 15

growing_number = growing_number * 2
growing_number = growing_number * 2
growing_number = growing_number * 2

print(growing_number)

# Task 2: Value Swap
first_number = 5
second_number = 8

print(first_number)
print(second_number)

first_number = 8
second_number = 5

print(first_number)
print(second_number)

# Task 3: Five and Two & 3 & 7

five = 3
two = 7

print(five * two)

# Task 4: Assign New Value
current_year = 2021
print("Current year is: " + str(current_year))

# Task 5: Input Birth Year
birth_year = input()
print("You were born in: " + birth_year)

# Task 6: Calculate Current Age:
age = int(current_year) - int(birth_year)

print("Your age is: " + str(age))


# Task 7: Total Ticket Cost:

show_name = input("What is the show name? ")
cost_per_ticket = input("How much does each ticket cost? ")
num_tickets = input("How many tickets are you buying? ")

total_cost = float(cost_per_ticket) * float(num_tickets)

print("Total price for " + num_tickets + " is $" + str(total_cost))

print("Enjoy " + show_name + "!")