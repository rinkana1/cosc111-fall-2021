# **Lab 6 - Username and Password Checker**

## **Instructions**

You and your group will finish implementing a username and password checker! The idea is to make use of while loops to check the user's input and only end the while loop when a valid username or password have been given. If a user name or password fails, tell the user why it failed and ask them to try again.

### **Valid Username**

A username is valid if it adhears to the following criteria:

* Must be at least 6 characters long.
* Must only contain letters and numbers.
* Must start with a letter.

### **Valid Password**

A password is valid if it adhears to the following criteria:

* Must be at least 10 characters long.
* Must contain at least one non alpha-numeric character.
* Must contain at least one capital letter.

### **Example Output**

An example run of the program could be:

```
Hello! Please register a username and password.

username:
- Must be at least 6 characters long.
- Must only contain letters and numbers.
- Must start with a letter.

Enter your username: gollum!

Invalid username: gollum!
- Must only contain letters and numbers.

Enter your username: gollum

password:
- Must be at least 10 characters long. 
- Must contain at least one non alpha-numeric character.
- Must contain at least one capital letter.

Enter your password: My precious ring

Invalid password: My precious ring
- Must contain at least one non alpha-numeric character.

Enter your password: My precious ring!

Thank you, you have been registered as:
username: gollum
password: My precious ring!
Hello! Please register a username and password.

username:
- Must be at least 6 characters long.
- Must only contain letters and numbers.
- Must start with a letter.

Enter your username: gollum!

Invalid username: gollum!
- Must only contain letters and numbers.

Enter your username: gollum

password:
- Must be at least 10 characters long. 
- Must contain at least one non alpha-numeric character.
- Must contain at least one capital letter.

Enter your password: My precious ring

Invalid password: My precious ring
- Must contain at least one non alpha-numeric character.

Enter your password: My precious ring!

Thank you, you have been registered as:
username: gollum
password: My precious ring!
```
### **Finish the Code**

In **main.py** most of the code has already been written, but you'll notice places with 'TODO' in the comments. You must finish writting the code in these places.

**CheckPassword(password, criteria)**

This function has been declared, but you need to write the implementation. Use `CheckUsername(username, criteria)` as an example. Feel free to make use of string helper functions to validate the input in your code. For example, you might consider using any of: *len()*, *isalpha()*, *isnumeric()*, *isupper()*, *isalnum()*, etc.

This function should return `True` if the `password` passed all the criteria. It should return `False` if it fails any one of the criteria, and it should also print the criteria message that failed.

**GetValidInput(input_type, criteria)**

This function has also been declared, but you need to write the implementation. Specifically, you'll need to add a **While Loop** to retrieve user input, and then loop until a valid input is received.

The `input_type` parameter can be either `"username"` or `"password"`, so the function can use conditionals to know how to check the input accordingly. Return the validated username or password string.