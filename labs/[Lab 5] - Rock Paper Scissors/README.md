#

# Lab 5 - Rock, Paper, Scissors!

## Instructions
You will complete the following tasks. Each task leads into the next, so do them in order. The task are open ended. The main thing I'll be looking for when grading is how well you made use of **functions**!!

#

### Task 1 - Create a Rock, Paper, Scissors Game!

**Instructions:**
Create a Rock, Paper, Scissors game!

* Present the options of choosing either rock, paper, or scissors to the user.
* Have the user enter in their choice as `input`.
* Have the computer make their own choice (i.e., you could use the `random.randint()` function).
* Compare the user's vs the computer's choice and determine who the winner is.
* Print the outcome to the screen.

The focus of this lab is to use **functions**. So, you should consider breaking up the bullet points above into separate functions that you can call. For example:

* A function that asks for and returns the user's input.
* A function that gets the computer's input.
* A function that, given the human's and computer's choices, determines who the winner is.
* A functions that prints the result to the user in a nice format.
* A function that initiates the game.

**Example Play Through 1:**

    Welcome to Rock Paper Scissors!

    0 - rock
    1 - paper
    2 - scissors
    Enter choice: 2

    You played scissors
    I played rock

    You lost this round!

**Example Play Through 2:**

    Welcome to Rock Paper Scissors!

    0 - rock
    1 - paper
    2 - scissors
    Enter choice: 1

    You played paper
    I played paper

    Ah, a draw!!

#

### Task 2: Best Out of Multiple Rounds

**Instructions:**
Extend your rock, paper, scissors game to play the best of of some number of rounds.

* Ask the user for the number of rounds to play.
* Use a `for` loop to play that number of rounds.
* Keep track of the win/loss record across each round.
* Output the final winner of all rounds.

You should NOT have to modify your code from task 1 much at all! Except to possibly return the result of the round.

Ideally, you should be able to add a `for` loop to run your task 1 code multiple times. You can use extra variables to keep track of the win:loss score so far.

**Example Play Through:**

    Welcome to Rock Paper Scissors!

    Best out of how many rounds? 3

    0 - rock
    1 - paper
    2 - scissors
    Enter choice: 2

    You played scissors
    I played scissors

    Ah, a draw!


    0 - rock
    1 - paper
    2 - scissors
    Enter choice: 1

    You played paper
    I played rock

    You win this round!


    0 - rock
    1 - paper
    2 - scissors
    Enter choice: 1

    You played paper
    I played rock

    You win this round!

    ----------------------------------------
    Final Result:

    Your score: 2
    My score: 0

    You are the ultimate winner!
    You now have bragging rights!