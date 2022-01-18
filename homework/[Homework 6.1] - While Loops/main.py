# Homework 6.1

from random import randint

# Task 1: Get Water State

def WaterState(water_temp):
  if water_temp < 32:
    return "ice"
  elif water_temp > 212:
    return "steam"
  else:
    return 'water'


# Task 2: Is All Even

def IsAllEven(nums_list):
  if not(nums_list):
    return True

  for num in nums_list:
    if num % 2 != 0:
      return False

  # If for loop never returned false, that means all are even so
  return True


# Task 3: Concatenate List

def ConcatenateList(the_list):
  string = ''

  for item in the_list:
    string += str(item)

  return string

# Task 4: Douse That Fire!

def DouseFire(fire_size):
  loops = 0

  while fire_size > 0:
    bucket = randint(1, 10)
    fire_size -= bucket
    loops += 1
  
  return loops

##################################
# Extra Credit
##################################

# Task 5: Is Sorted List (+5 points)

def IsSortedList(the_list):
  lastItem = ''

  for item in the_list:
    if item == the_list[0]:
      lastItem = item
      continue
    
    if item < lastItem:
      return False
    
    lastItem = item
  
  return True



# Task 6: Get Numbers to Exact Sum (+10 points)

def GetNumbersToSum(exact_sum):
  sum = 0
  list_of_num = []

  while sum != exact_sum:
    num = randint(0, 10)
    
    if sum + num > exact_sum:
      continue
    else:
      sum += num
      list_of_num.append(num)
    
  return list_of_num