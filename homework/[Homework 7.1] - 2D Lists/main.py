# Homework 7.1 - 2D Lists

# Function 1 - Sum All Items in 2D List

def Sum2DNumsList(nums_2d_list):
  total_sum = 0

  for i in nums_2d_list:
    for j in i:
      total_sum += j
  
  return total_sum

# Function 2 - Add To All

def AddToAll(list_of_lists, item):
  for i in list_of_lists:
    i.append(item)

# Function 3 - Scalar Multiplication

def ScalarMultiply(scalar, matrix):
  x_index = 0
  y_index = 0
  for i in matrix:
    y_index = 0
    for j in i:
      matrix[x_index][y_index] *= scalar
      y_index += 1
    x_index += 1
  
  return matrix

# Function 4: Get Row Averages

def GetRowAverages(table):
  averages = []

  for i in table:
    averages.append(sum(i) / len(i))
  
  return averages

################
# Extra Credit
################

# Function 5 - Get Column Averages (+10 points)

def GetColumnAverages(table):
  if not table:
    return []

  averages = []

  for i in range(len(table[0])):
    column_average = 0

    for j in range(len(table)):
      column_average += table[j][i]

    column_average /= len(table)
    averages.append(column_average)
  
  return averages