# Homework 5.1 - More Functions

# Function 1 - Get Smaller Num

def GetSmallerNum(num1, num2):
  if num1 < num2:
    return num1
  else:
    return num2

# Function 2 - Get Largest Num From List

def GetLargestNumInList(nums_list):
  if not(nums_list):
    return None
  
  nums_list.sort()
  print(nums_list)

  return nums_list[len(nums_list) - 1]

# Function 3 - Convert to Fahrenheit

def ConvertToFahrenheit(celsius_temp):
  return int(celsius_temp / 5 * 9 + 32)

# Function 4 - Convert to Celcius

def ConvertToCelsius(fahrenheit_temp):
  return int((fahrenheit_temp - 32) * 5 / 9)

# Task 5 - Compound Interest Calculator

def CompoundInterest(principal, rate, years):
  result = (((rate / 100) + 1) ** years) * principal
  return result


def CompountInterestOverTime(principal, rate, time_range):
  result = []

  for index in range(time_range + 1):
    result.append(CompoundInterest(principal, rate, index))

  return result


def DisplayInterestResultsAsBarGraph(interest_results, principal):
    if interest_results is None:
        return
    for i in range(len(interest_results)):
        result = int(interest_results[i])
        num_bars = int(result / principal)
        print(str(i) + "-"*num_bars + "$" + str(result))




def CompoundInterestCalculator():
    print("Welcome to the compound interest calculator!")
    print()

    principal = float(input("Please enter the initial amount in dollars: "))
    rate = float(input("Please enter the expected rate of return as a percetage: "))
    time_range = int(input("Please enter the length of time in years: "))
    print()

    interest_results = CompountInterestOverTime(principal, rate, time_range)

    DisplayInterestResultsAsBarGraph(interest_results, principal)





