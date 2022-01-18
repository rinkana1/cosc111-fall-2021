# Project 2 - Word Monster!

In this project, we'll be implementing a game called, Word Monster!

### **How The Game Works**

* A giant monster is about to terrorize the city!
* It's thinking of a word, if we can guess all the letters in the word it is thinking of, it will go away.
* Otherwise, it will destory us all!

* The program chooses a random word from a list of words.
* The program then prints the monster approaching and a blank set of spaces for each missing letter in the hidden word.
* The user can see the blank spaces and tries to guess a letter.
* If the letter is in the word, then the letter's corresponding blank space is filled in with the guessed letter.
* If the letter is not in the word, then the monster gets closer.
* The user has 6 missed guesses before the monster arrives.

* If all letters of the word are guessed before the monster arrives, the user wins!

* (This is similar to the game Hangman)

Here is an example run of what the program output and interaction could be:

**Example 1:**

```
----------------------------------------

 ---------------- 
|                |
|                |
 ---------------- 

Word: ______ | Wrong: []

Guess a letter: a

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|       {}       |
|       {}       |
|       {}       |
|                |
 ---------------- 

Word: ______ | Wrong: [a]

Guess a letter: e

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|       {}       |
|       {}       |
|       {}       |
|                |
 ---------------- 

Word: ___e__ | Wrong: [a]

Guess a letter: i

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|       {}       |
|       {}       |
|       {}       |
|                |
 ---------------- 

Word: __ie__ | Wrong: [a]

Guess a letter: r

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|   WW  {}  WW   |
|    \\ {} //    |
|     \\{}//     |
|                |
 ---------------- 

Word: __ie__ | Wrong: [ar]

Guess a letter: t

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|   WW  {}  WW   |
|    \\ {} //    |
|     \\{}//     |
|      {**}      |
|      {**}      |
|      {**}      |
|      {**}      |
|                |
 ---------------- 

Word: __ie__ | Wrong: [art]

Guess a letter: y

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|   WW  {}  WW   |
|    \\ {} //    |
|     \\{}//     |
|      {**}      |
|     /{**}\     |
|    //{**}\\    |
|   WW {**} WW   |
|                |
 ---------------- 

Word: __ie__ | Wrong: [arty]

Guess a letter: m

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|   WW  {}  WW   |
|    \\ {} //    |
|     \\{}//     |
|      {**}      |
|     /{**}\     |
|    //{**}\\    |
|   WW {**} WW   |
|     / -- \     |
|     \    /     |
|      \  /      |
|       \/       |
|                |
 ---------------- 

Word: __ie__ | Wrong: [artym]

Guess a letter: d

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|   WW  {}  WW   |
|    \\ {} //    |
|     \\{}//     |
|      {**}      |
|     /{**}\     |
|    //{**}\\    |
|   WW {**} WW   |
|     / -- \     |
|     \    /     |
|      \  /      |
|       \/       |
|                |
 ---------------- 

Word: __ie_d | Wrong: [artym]

Guess a letter: w

----------------------------------------

 ---------------- 
|                |
|       ][       |
|      ####      |
|       {}       |
|   WW  {}  WW   |
|    \\ {} //    |
|     \\{}//     |
|      {**}      |
|     /{**}\     |
|    //{**}\\    |
|   WW {**} WW   |
|     / -- \     |
|     \@  @/     |
|      \  /      |
|       \/       |
|       ||       |
|       VV       |
|                |
 ---------------- 

Word: __ie_d | Wrong: [artymw]

----------------------------------------

NOOO! The monster is attacking, we are doomed!

The word was: shield
```
---
### **Project Requirements**

* Implement the game as described above. You should more or less follow similar flows as the example outputs above.

* Choose a single random word from the list of words. The list of words to choose from can be obtained by calling the already written `LoadWords()` function. You should be able to call it this way:

```py
word_list = LoadWords()
```
* **The user must be shown a "blank" word, that has a blank for each letter in the chosen word**. This allows the user to see the length of the word. For example, if the word was `"hello"`, we could show the user: `"_____"`.

* **The user must guess the word one letter at a time.** The user can enter a letter, if the letter is in the word, then fill in the blank space with the letter at the appropriate location (or multiple locations if the letter appears more than once). For the example above, if the user guesses `"l"`, then the blank spaces would show: `"__ll_"`.

* **The user gets no more than 6 wrong guesses.** After each guess, you can call the provided `PrintMonster(num_wrong)` function. Which will print the monster getting closer, based on the number of wrong guesses.

* **After 6 wrong guesses, the user has lost the game.** Show the final monster and print the results.

* **If the user completes the word in time.** The user won. Print the results!

* **The exact text to use in printing the output is up to you.** Feel free to have fun with the wording, spacing, etc.

* **You must use good programing best practices.** This primarily comes down to good use of **functions** and **variable naming**! There is no hard and fast rule here. However, you won't receive full credit if there are NO functions, or if the variable names don't make any sense at all.

* **Your program should NOT crash with any syntax or runtime errors!** You program should not crash. Syntax errors will receive zero points, and runtime errors will cause a significant loss in your grade. Make sure to test your program with MANY different inputs!

Optional Requirements

* **Create your own MONSTER!** An existing function, `PrintMonster(num_wrong)`, is provided for you that prints the monster, piece by piece. Try creating your own function that prints your own text-art monster! Show me some creativity! Maybe even have a couple of different monster functions that could be used.

### **Python Coding Style**

As mentioned, the project must be implemented in a way that uses good programming style and best practices as discussed in class, and in the reading on Python Style Guide. When you pass off the project, we'll particularly look for:

* Did you use functions to help organize your code, avoid code duplication, and improve code readability?
* Are your variable and function names useful and informative?
* Did you make good use of whitespace to organize your code and make it more readable?

### **Hints**

* The trickiest part might be to fill in the "blank" word with the correct letter. Make this a separate function that returns the new "blank" string (or list). For example, you could pass in as arguments the chosen word, the current blank string (or list), and the letter. It then returns a string (or list) with the letter in the correct blank spots. For example:
```py
Inputs:
    word =  "racecar"
    blank = "_______"
    letter = "r"
  
Returns:
    "r_____r"
```
* START EARLY! It will be very hard to finish this just the day it is due. Programming ALWAYS takes longer than you think.
* Pass off the project with a TA or the instructor. They will grade it on the spot for you! Or provide helpful advice and feedback!
* Remember, projects are about making use of multiple concepts we've learned so far in class.
* Consider concepts like while loops, random, conditionals, functions, etc.
* Develop a PLAN first. Write out in English the steps your program will need to take. If you're struggling with this, think about how you would explain the rules of this game to another person.
* Break up parts of the program into functions. For example, you might have a function from printing everything to the console after each guess. Or a function that fills in the blank spaces with the correctly guessed letter.