# **Lab 7 - Refactor Palindromes**

## **Instructions**

Consider the program, already completely written, in **main.py**. It is a Palindrome checker that asks the user to enter in two valid palindromes. The program uses a **while** Loop to check the validity of each panlidrome and keeps asking the user until they enter in a valid one. Finally, the program compares the two palindromes and determines if they are the same.

Feel free to run it and see how it interacts.

**Valid Palidrome**

An input string is considered a palidrome if the string is the exact same printed forward as it is printed backwards. For example the string *racecar*:
```
 Forward: racecar
 Backward: racecar
```
Other example palindromes:
```
 ana
 amanaplanacanalpanama
 I
 deed
```
In this program, only alphabet characters are permitted to be entered as a string (no spaces, numbers, or punctuation, etc).

**TODO:**

Notice how the program has no functions. Notice that there is duplicate code in a few places.

*Remember Function Best Practices*

Your task is to **refactor** this code in **main.py** and decompose it into various functions. The behavior should not change, only the structure of the code.

**Hints**

* Any chunks of code that appear multiple times seems like a strong candidate to move to a function.
* Any chuncks of code that seem to do a particular task might be better off as a function. For example, a function that checks a specific thing. Or a function that prints the results.