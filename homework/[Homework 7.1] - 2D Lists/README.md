# **Homework 7.1 - 2D Lists**

Each task will require you to define a function. Complete the tasks below in main.py. All work must be done individually.

Now that we are writing functions, the tests will be checking each function's output individually, which means that your function names are important - if you don't name your functions exactly as indicated below, the tests will not pass.

**NOTE: You should not use the input() function in ANY of your functions** for this homework. When the instructions say "takes a value as an input parameter," this is referring to function parameters, not input().

**NOTE:** Remember to test your code before submitting!

---
## **Your Tasks**
---
### **Function 1: Sum All Numbers in 2D List**

**Instructions:** Define a function called `Sum2DNumsList(nums_2d_list)`, which takes a **2D list of integers** as an input parameter, adds all the items together, and returns the result. If the 2D list is empty, return 0.

**Example 1**

Function Call:
```py
result = Sum2DNumsList([[13, 14, 12],
                        [21, 23, 33],
                        [31, 76, 13]])
print(result)
```
Return Value:
```py
236
```
**Example 2**

Function Call:
```py
all_my_lists = [[1, 2, 3, 4],
                [100, 100, 100]]
result = Sum2DNumsList(all_my_lists)
print(result)
```
Return Value:
```py
310
```
**Hints:** You could use a nested for loop to iterate through each number in the 2D list.
---
### **Function 2: Add To All**

Define a function called `AddToAll(list_of_lists, item)`. The function takes as input a 2D list, and an item. The function should append the item to the end of each inner list in the 2D list, then return the modified list.

* If there are no inner lists (not a 2D list), then don't modify the list at all.
* You can assume that any items in the outer list will always be a list and not some other type.

**Example 1**

Function Call:
```py
list_of_lists = [["frodo",    "sam",   "gandolf"],
                 ["hermione", "harry", "hagrid"],
                 ["luke",     "han",   "vader"]]
AddToAll(list_of_lists, "hulk")
print(list_of_lists)
```
Result:
```py
[["frodo",    "sam",   "gandolf", "hulk"],
 ["hermione", "harry", "hagrid", "hulk"],
 ["luke",     "han",   "vader", "hulk"]]
```
**Example 2**

Function Call:
```py
list_of_lists = []
AddToAll(list_of_lists, "hulk")
print(list_of_lists)
```
Result:
```py
[]
```
**Hint:** Iterate over each row in the outer list and append the item to the row.
---
### **Function 3: Scalar Multiplication**

**Instructions:** Define a function called `ScalarMultiply(scalar, matrix)`. This functions takes as input a scalar (any number) and a matrix (a 2D list of numbers), and multiplies each item in the matrix by the scalar. If the matrix is empty, then the result should still be an empty matrix.

* You can assume that the length of each inner list will always be the same as each other.
* Your function should modify the matrix, not create a separate copy.

**Example 1**

Function call:
```py
result = ScalarMultiply(2, [[13, 14, 12],
                            [21, 23, 33],
                            [31, 76, 13]])
print(result)
```
Return value:
```py
[[26, 28, 24],
 [42, 46, 66],
 [62, 152, 26]]
```
**Example 2**

Function call:
```py
my_matrix = [[4, 8, 0, -100]]
result = ScalarMultiply(0.5, my_matrix)
print(result)
```
Return value:
```py
[[2, 4, 0, -50]]
```
**Hints:**

* You'll need to iterate through each item in the matrix to multiply the each item by the scalar. However, you need to store each result back into the matrix. Use indexes to do this.
* Nested for loops, each iterating over a range of indexes, will allow you to reference and update each value in the matrix.
---
### **Function 4: Compute Row Averages**

**Instructions:** Define a function called `GetRowAverages(table)`. This functions takes as input a table, which is a 2D list of numbers, and computes the average for each row and returns the results as a 1-D list.

* If the outer list of the table is empty, return an empty list.
* If the inner lists are empty, return a 1-D list with zero as the average for each inner list.

Example 1
Function call:

```py
result = GetRowAverages([[10, 14, 12],
                         [21, 23, 34],
                         [31, 76, 19],
                         [3,  27, 12]])
print(result)
```

Return value:

```py
[12, 26, 42, 14]
# (10 + 14 + 12) / 3 = 12
# (21 + 23 + 34) / 3 = 26
# (31 + 76 + 19) / 3 = 42
# ( 3 + 27 + 12) / 3 = 14
[12, 26, 42, 14]
# (10 + 14 + 12) / 3 = 12
# (21 + 23 + 34) / 3 = 26
# (31 + 76 + 19) / 3 = 42
# ( 3 + 27 + 12) / 3 = 14
```

**Example 2**

Function call:
```py
my_table = [[4, 8, 0, -100]]
result = GetRowAverages(my_table)
print(result)
```
Return value:
```py
[-22]
```
**Example 3**
Function call:

```py
my_table = [[]]
result = GetRowAverages(my_table)
print(result)
```
Return value:
```py
[0]
```
**Hints:**

* Recall that to compute the average, you need to sum up every value in the row, then divide the result by the length of the row.
* The result will be a new list, with the average of each row appended to it.
* The outer for loop should iterate over each row.
* The inner for loop will be used to compute the average.
---
## **Extra Credit**
---
### **Function 5: Compute Column Averages (+10 points)**

**Instructions:** Define a function called `GetColumnAverages(table)`. This functions takes as input a table, which is a 2D list of numbers, and computes the average for each column and returns the results as a 1-D list.

* If the outer list of the table is empty, return an empty list.
* If the inner lists are empty, also return just an empty list.

Recall that to compute the average, you need to sum up every value in the column, then divide the result by the number of rows.

**Example 1*

Function call:
```py
result = GetColumnAverages([[13, 14, 12],
                            [21, 23, 33],
                            [31, 76, 13],
                            [3,  27, 10]])
print(result)
```
Return value:
```py
[17, 35, 17]
​
# For column 0: 
#    13 + 21 + 31 + 3 = 68
#    68 / 4 = 17
```
**Example 2**

Function call:
```py
my_table = [[4, 8, 0, -100]]
result = GetColumnAverages(my_table)
print(result)
```
Return value:
```py
[4, 8, 0, -100]
```
**Hints:**

* Note that this is averaging the COLUMNS, not the rows. That means that each value contributing to the average, comes from a different inner list.
* Perhaps check the for special case of an empty list in the beginning. Then you won't have to worry about index out of bounds as much later.
* Get the number of rows and number of columns early. Then you can loop over an index for the columns as the outer loop, while the inner loop can sum up the value from each row in that column.
* Remember, when indexing into a 2D list, the row index is first, then the column. E.g., `my_table[row][col]`.
* It might be helpful to initialize the result list to be same size as the number of columns as soon as you declare it. E.g, `result = [0] * num_columns`. Then to update the average, you could just index into the value that needs changing. E.g., `result[col] = average`.