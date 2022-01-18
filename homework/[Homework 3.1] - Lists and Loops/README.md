# Homework 3.1 - Lists and Loops

Complete the tasks below in **main.py**. All work must be done individually.

**NOTE:** Remember to test your code before submitting!

There are unit tests to run for each homework. To make it automated, each unit test looks for the exact output expected for each task. Makes sure all unit tests pass before submitting your homework.

#

## Your Tasks

### Task 1: Sum List

**Instructions:**
In **main.py** the following list is already defined:

     all_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

Write some code that loops through the list and outputs the total sum of every number in the list. The output should be:

    Total sum is: <total_sum>

**Note** Do not just calcualate the total_sum on your own. When grading, we will expect to see a loop that does the summation.

#

### Task 2: RSVP Names

**Instructions:**
Write code that does the following:
* Get as **input**, the number of people in the party.
* Use a *For Loop* to ask for each person's name (as **input**) and store each name in a list.
* Loop through the list of names and print them out like so:

      The following are registered to attend:
      <name1>
      <name2>
      <name3>
        ...

* If the list is empty (0 party members), then print the following:

      No one is registered.

**Example 1**:

    How many people in your party? 4
    Enter name: Frodo
    Enter name: Gandalf
    Enter name: Gollum
    Enter name: Seth
    The following are registered to attend:
    Frodo
    Gandalf
    Gollum
    Seth

**Example 2**

    How many people in your party? 0
    No one is registered.

#

### Task 3: Print If Greater Than 100

**Instructions:**
Write code that does the following:
* Get as **input**, the amount of numbers to input.
* Use a *For Loop* to to ask for each number (as **input**) and store each number in a list.
* Loop through the list of numbers and only print the numbers greater than 100.
* If *ALL* numbers in the list are less than 100, or the list is empty, then print:

      All numbers are less than 100!


**Example 1**:

    How many numbers? 4
    Enter a number: -57
    Enter a number: 103
    Enter a number: 42
    Enter a number: 5323
    103
    5323

**Example 2**

    How many numbers? 4
    Enter a number: -57
    Enter a number: 99
    Enter a number: 42
    Enter a number: 23
    All numbers are less than 100!

**Hint:** When looping through each number to print (if over 100), use a boolean variable to keep track of whether or not you encountered at least one number greater than 100.

#

### Task 4: How Many Handshakes?

**Instructions:**
Get as **input** the number of people in a room. Then use a *For Loop* to calculate how many total handshakes would happen if each person shook everyone else's hand exactly once.

**Example 1:**

    How many people in the room? 4
    6 total handshakes.

**Example 2:**

    How many people in the room? 10
    45 total handshakes.

**Example 3:**

    How many people in the room? 95
    4465 total handshakes.

**Example 4:**

    How many people in the room? 2
    1 total handshakes.

**Example 5:**

    How many people in the room? 1
    0 total handshakes.

**Hint:** Start small. Figure out how many handshakes with just 2 people, then 3, then 4, and so on. Do you see a pattern? Can you apply that pattern using a For Loop?

#

### Task 5: Find All The 'E's!

**Instructions:**
Write code that does the following:
* Gets a sentence or phrase as **input**.
* Use a *For Loop* to loop through each character in the string and count how many times *'e'* (or *'E'*) appears. It should not be case sensitive.
* Use a list to store the *index* of each *'e'* in the string.
* Print the number of e's found as so:

      Found 'e' <number_of_e> times!

* Print the list of indexes where e's are found in the string as so:

      Indexes are: <list_of_indexes>

**Example 1**:

    Enter a sentence or phrase: Hello Erin! I really enjoy Pie.
    Found 'e' 5 times!
    Indexes are: [1, 6, 15, 21, 29]

Notice how the letter 'e' and/or 'E' appears 5 times in the sentence (case insensitive)? Also notice that the list of indexes are for the input string. For example, index 1 refers to the second character in the input string, which is the first occurrence of the letter 'e'.

**Example 2**:

    Enter a sentence or phrase: Not today I think.
    Found 'e' 0 times!
    Indexes are: []

**Hints:**
* When looping through each character in the input string, you need to do so in a way that gives you the current index of the character you are considering. Perhaps something like *range* used with *len*.
* Remember, this is case-insensitive. It should work for both lowercase ('e') and uppercase ('E').
