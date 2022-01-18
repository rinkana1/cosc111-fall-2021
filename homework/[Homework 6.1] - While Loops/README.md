# Instructions

Each task will require you to define a function. Complete the tasks below in **main.py**. All work must be done individually.

Now that we are writing functions, the tests will be checking each function's output individually, which means that your function names are important - if you don't name your functions exactly as indicated below, the tests will not pass.

**NOTE: You should not use the input() function in ANY of your functions** for this homework. When the instructions say "takes a value as an input," this is referring to function parameters, not input().

**NOTE:** Remember to test your code before submitting!


___

## Your Tasks

___

### **Function 1: Get Water State (conditionals review)**

**Instructions:** Define a function called `WaterState(water_temp)` that takes, as the input parameter, the water tempurature. The function should then return whether it is `"ice"` (temperature below 32), `"water"` (temperature between 32 and 212), or `"steam"` (temperature above 212).

**Example 1**

Function Call:

```py
WaterState(13)
```

Return Value:

```py
"ice"
```

**Example 2**

Function Call:

```py
WaterState(97)
```

Return Value:

```py
"water"
```

**HINT:** Your function itself should not print anything, it should just return the result as a string!

___

### **Function 2: Is All Even (loop review)**

**Instructions**: Define a function called `IsAllEven(nums_list)` that takes one list of integers as an input parameter and returns `True` if EVERY number in the list is even. Otherwise, return `False`. If the list is empty, return `True`.

**Example 1**

Function Call:
```py
IsAllEven([2,-4,0,100,14])
```
Return Value:
```py
True
```
**Example 2**

Function Call:
```py
IsAllEven([4,0,10,7,26])
```
Return Value:
```py
False
```

**Example 3**

Function Call:
```py
IsAllEven([])
```
Return Value:
```py
True
```

**HINTs:**

* Your function should not print anything, it should just return the result!
* Use a for loop OR a while loop to look at each number is the list.
    * If you encounter an odd number, then you can return False right away.
    * After the for loop is over, return True since you didn't encounter any odd numbers.

___

### **Function 3: Concatenate List (loop review)**

**Instructions:** Define a function called `ConcatenateList(the_list)` that takes one list of items (of any type) as an input parameter. The function should concatenate all items in the list together to form one string. Return that string.

**Example 1**

Function Call:
```py
ConcatenateList(["You", "Are", "The", "Bees", "Knees"])
```
Return Value:
```py
"YouAreTheBeesKnees"
```
**Example 2**

Function Call:
```py
ConcatenateList([-4,":",0,":",3.7,":",77])
```
Return Value:
```py
"-4:0:3.7:77"
```
**Example 3**

Function Call:
```py
ConcatenateList([])
```

Return Value:
```
""
```

**HINTs:**

* Your function should not print anything, it should just return the result!
* Have a string variable that starts out as empty (""). Contatenate items in the list to the end of this string one by one.
* Use a for loop OR while loop to iterate over every item in the list, and concatenate them to the end of your result string.
* The type of data in the list could be anyting, ints, float, booleans. Make sure to convert them to string before concatenating.

---

### **Function 4: Douse That Fire! (while loops!)**

**Instructions:** Define a function called `DouseFire(fire_size)` that takes, as an input parameter, the size of the fire (integer). The function should continually try to douse the fire with buckets of water until the fire is out. The function should return how many buckets of water it took to douse the fire.

Douse the fire should work as follows:

* While the fire is still going (fire_size is greater than zero).
    * Get a randomly sized bucket of water (between 1 and 10).
    * Decrease the fire_size by the size of the bucket.
* Return the number of buckets it took to douse the fire.

**Example 1**

Function Call:

```py
num_buckets = DouseFire(100)
```

Return Value:

```py
26  # Could be different for each call since random
```

**Example 2**

Function Call:
```py
num_buckets = DouseFire(0)
```
Return Value:
```py
0
```
**HINTs:**

* Your function should not print anything, it should just return the result!
* Use a while loop to keep getting random buckets and decreasing the fire_size until fire_size is no longer greater than zero.
* Remember, the size of each bucket should be random between 1 and 10. Import random and use the randint() function.
* Use a variable to count each bucket during each iteration of the loop.

---
## **Extra Credit Problems (10 points each)**
---
### **Function 5: Is Sorted List**

**Instructions:** Define a function called `IsSortedList(the_list)` that takes one list of items as an input parameter. The function should return `True` if the list is in sorted order (least to greatest). Otherwise, the function should return `False`. If the list is empty, return `True`.

**Example 1**

Function Call:
```py
IsSortedList([3,6,6,6,13,21])
```
Return Value:
```py
True
```
**Example 2**

Function Call:
```py
IsSortedList(["abby", "chris", "john"])
```
Return Value:
```py
True
```
**Example 3**

Function Call:
```py
IsSortedList([3,6,4,6])
```
Return Value:
```py
False
```
**HINTs:**

* Use a for loop to look at each item in the list.
* You'll need a way to remember or refer to the previous item in the list.

---

### **Function 6: Get Numbers to Exact Sum (+10 points)**

**Instructions:** Define a function called `GetNumbersToSum(exact_sum)` that takes, as an input parameter, the exact target sum. The function then needs randomly select numbers (between 0 and 10) and add them to a list until the numbers in the list sum to exactly `exact_sum`. If a randomly selected number causes the total sum to exceed exact sum, then you should NOT add it to the list, but simply try again with the next random number. Return the list of numbers that sum to exactly `exact_sum`.

**Example 1**

Function Call:
```py
numbers = GetNumbersToSum(11)
```
Return Value:

```py
# Could be different for each call since random
[2,5,1,3]
# or
[7,4]
# or
[10,1]
# Etc
# Could be different for each call since random
[2,5,1,3]
# or
[7,4]
# or
[10,1]
# Etc
```

**Example 2**

Function Call:
```py
numbers = GetNumbersToSum(0)
```
Return Value:
```py
[]
```
**HINTs:**

* Use a while loop to keep getting random numbers and adding them to the total sum and appending to the list.
* Remember, each number should be random between 0 and 10.
* If a number will cause the total to exceed exact_sum, skip it and wait for the next iteration.