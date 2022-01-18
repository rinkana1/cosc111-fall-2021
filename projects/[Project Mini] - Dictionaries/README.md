# Project Mini - Dictionaries

Each task will require you to define a function. Complete the tasks below in main.py. All work must be done individually.

Now that we are writing functions, the tests will be checking each function's output individually, which means that your function names are important - if you don't name your functions exactly as indicated below, the tests will not pass.

**NOTE**: You should not use the input() function in ANY of your functions for this assignment. When the instructions say "takes a value as an input argument," this is referring to function arguments, not input().

**NOTE**: Remember to test your code before submitting!

---
## **Your Tasks**

### **Function 1: Grade: Value Map**

**Instructions**: Define a function called `GetGradeMap()` that returns a dictionary that maps the grade letter to it's GPA value:

* A = 4
* B = 3
* C = 2
* D = 1
* F = 0

**Example**:

Function Call:

```py
    grade_map = GetGradeMap()
    print(grade_map)
```

Outputs:
```py
    {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
```
---
### **Function 2: Student Dictionary**

**Instructions**: Define a function called `CreateStudentRecord(firstname, lastname, age, grades)`, which takes set of attributes about a student and adds them to a single dictionary and returns the result. The dictionary's keys should be strings of the same names as the parameter names. The grades should be letter grades.

**Example 1**

Function Call:
```py
student1 = CreateStudentRecord("Edgar", "Poe", 20, ["A", "C", "B", "A"])
print(student1)
```
Return Value:
```py
{'firstname': 'Edgar', 'lastname': 'Poe', 'age': 20, 'grades': ['A', 'C', 'B', 'A']}
```
---
### **Function 3: Get Student's GPA**

**Instructions**: Define a function called `CalculateGPA(student)`, which takes as input a dictionary, with the student attributes defined in the previous task, and calculates the student's GPA. Return the result.

A GPA is calculated as follows:

* Use the Grade-to-value mapping stored in the dictionary returned from GetGradeMap().
    * Example, if the grade is a "B", use "B" as the key to look up B's value in the GradeMap to get the 3.
* For each grade the student has, sum up their corresponding values and divide the total by the number of grades. This is the GPA.

**Example 1:**

Function Call:
```py
student1 = CreateStudentRecord("Edgar", "Poe", 20, ["A", "C", "B", "A"])
gpa = CalculateGPA(student1)
print(gpa)
```
Returns:
```py
3.25
```