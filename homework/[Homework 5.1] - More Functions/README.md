# Instructions

Each task will require you to define a function. Complete the tasks below in **main.py**. All work must be done individually. 

Now that we are writing functions, the tests will be checking each function's output individually, which means that your function names are important - if you don't name your functions exactly as indicated below, the tests will not pass.

**NOTE:** **You should not use the input() function in ANY of your functions** for this homework. When the instructions say "takes a value as an input," this is referring to function parameters, not input().

**NOTE:** Remember to test your code before submitting!

#

## Your Tasks

### Function 1: Get Smaller Num

**Instructions:**
Define a function called **GetSmallerNum(num1, num2)** that takes two numbers as input parameters and returns the number that is smaller. If the numbers are the same, return either of them.

**Example 1**
##### Function Call:

    result = GetSmallerNum(8, 3)
    print(result)

##### Prints:

    3

**Example 2**
##### Function Call:

    result = GetSmallerNum(5, 9)
    print(result)

##### Prints:

    5

**HINT:** Your function should not **print** anything, it should just **return** the result! 

# 

### Function 2: Get Largest Num From List

**Instructions:**
Define a function called **GetLargestNumInList(nums_list)** that takes one list of integers as an input parameter and returns the number in the list that is the largest. If the largest number occurs multiple times, return one of them. If the list is empty, don't return anything (should effectively come back 'None'), or just return None.

**Example 1**
##### Function Call:

    GetLargestNumInList([8, 9, 5, -111])

##### Return Value:

    9

**Example 2**
##### Function Call:

    GetLargestNumInList([-55, -9, -12, -7, -8, -37])

##### Return Value:

    -7

**Example 3**
##### Function Call:

    GetLargestNumInList([])

##### Return Value:

    None

**HINTs:** 
* Your function should not **print** anything, it should just **return** the result! 
* Use a for loop and an extra variable to keep track of the largest-so-far as you loop through the items.
* Might want to check for the length of the string in the beginning to handle the empty case.

# 

### Functions 3-4: Temperature Conversions

*Brrr!* If you've ever had to convert a temperature from Fahrenheit to Celsius or vice versa, you know it's a headache. Let's create some conversion functions so that we never have to do the conversion ourselves again!

Write a function called **ConvertToFahrenheit(celsius_temp)** that takes a number and **returns** that number converted from Celsuis to Fahrenheit.

Write another function called **ConvertToCelsius(fahrenheit_temp)** that takes a number and **returns** that number converted from Fahrenheit to Celsius.

**Note** All conversions must be integer conversions!

Here are the formulas to do the conversions:

* **Celsius to Fahrenheit:** Divide by 5, then multiply by 9, then add 32
* **Fahrenheit to Celsius:** Subtract 32, then multiply by 5, then divide by 9

**Hint 1:** Remember to be careful about order of operations in your code!

**Hint 2:** If you want to check your answers, Try the freezing and boiling points of water:
* 32 Fahrenheit == 0 Celsius
* 212 Fahrenheit == 100 Celsius

#

### Task 5: Compound Interest Calculator

#### Compound Interest Explained

Compound interest is how much additional money you'll receive if you invest a certain amount of money, at a given interest rate, over time. For example, if you invest **$1000**, and expect to reclaim your money after **one year** at an interest rate of **10%**, then at the end of the year you should recieve **$1100**.
* (10% of 1000 is $100, which is added back to the original $1000).

You could choose to reinvest that $1100 for another year, which will end up as **$1210** ((10% of 1100) + 1100).

#### Instructions:

Part of the program is already implemented, and can be initiated by calling the following function:

* **CompoundInterestCalculator()**

The program it executes asks for three pieces of input from the user:

* **principal** - this is the initial amount of money.
* **rate** - the is the expected interest rate as a percentage (e.g., 15% inputted as just 15).
* **time_range** - this is the amount of time to invest in years. Each year the interest rate is applied and added back to the principal.

You simply need to **implement** two functions, already defined, to calculate the compound interest over time. The program will then display the results.

#

### Functions To Implement

**CompoundInterest(principal, rate, years)**

This is the primary function that computes the actual amount of money over a given number of years, compounded annually. You just need to implement the following and return the result:

* Convert the rate percentage into a fraction (float) by dividing by 100.
* Add 1 to the converted rate
* Raise the 1+rate to the *years* power (years is the exponent).
* Multiply the result by the principle and return as final result.

The end-to-end formula should look like this:

    result = principal * ((rate / 100) + 1)^years

Example:
  
    principle = 1000
    rate = 15
    years = 5

    rate / 100 = 15/100 = 0.15
    (rate / 100) + 1 = 0.15 + 1 = 1.15
    1.15^years = 1.15^5 = 2.011
    principal * 2.011 = 1000 * 2.011 = 2011


#

**CompountInterestOverTime(principal, rate, time_range)**

This function should call the first function, *CompoundInterest* for each year in *time_range*, and store/return the results in a list.

For example, if the arguments are:

    principle = 1000
    rate = 15
    time_range = 3

Then it should call *CompoundInterest* **four** times, once each for years = 0, 1, 2, and 3.

The results should be a list:

    [1000, 1150, 1322.5, 1520.875]

#

### Example output:

**Run the function:**

    CompoundInterestCalculator()

**Outputs:**

    Welcome to the compound interest calculator!
    Please enter the initial amount in dollars: 10000
    Please enter the expected rate of return as a percetage: 20
    Please enter the length of time in years: 20
    0-$10000
    1-$12000
    2-$14400
    3-$17279
    4--$20736
    5--$24883
    6--$29859
    7---$35831
    8----$42998
    9-----$51597
    10------$61917
    11-------$74300
    12--------$89161
    13----------$106993
    14------------$128391
    15---------------$154070
    16------------------$184884
    17----------------------$221861
    18--------------------------$266233
    19-------------------------------$319479
    20--------------------------------------$383375

Notice how the money starts to grow quickly over time! Investing is awesome!

#
