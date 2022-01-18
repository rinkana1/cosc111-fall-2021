# Lab 6 - Username and Password Checker

def CheckUsername(username, criteria):
    # Must be at least 6 characters
    if len(username) < 6:
        print(criteria[0])
        return False

    # Must only contain letters or numbers
    if not username.isalnum():
        print(criteria[1])
        return False

    # Must start with a letter
    if not username[0].isalpha():
        print(criteria[2])
        return False
    
    # All checks have passed
    return True


def CheckPassword(password, criteria):
    # TODO: Check that the password is valid according to the criteria. See CheckUsername for an example.

    # Must be at least 10 characters long.
    if len(password) < 10:
      print(criteria[0])
      return False

    # Must contain at least one non-alpha-numeric character
    if password.isalnum():
      print(criteria[1])
      return False

    # Must contain at least one capital letter.
    if password.islower():
      print(criteria[2])
      return False
    
    return True


def GetValidInput(input_type, criteria):
    if input_type == "username":
      username = input("Input username: ")

      while not CheckUsername(username, criteria):
        username = input('Input username: ')

      print("Valid username!")
      print()

      return username

    elif input_type == "password":
      password = input("Input password: ")

      while not CheckPassword(password, criteria):
        password = input('Input Password: ')

      print("Valid password!")
      print()

      return password
  
    


def GetInput(input_type, criteria):
    print(input_type + ":")
    for message in criteria:
        print(message)

    return GetValidInput(input_type, criteria)


print("Hello! Please register a username and password.")
print()

username_criteria = [
    "- Must be at least 6 characters long.",
    "- Must only contain letters or numbers.",
    "- Must start with a letter.",
]

password_criteria = [
    "- Must be at least 10 characters long.",
    "- Must contain at least one non alpha-numeric character.",
    "- Must contain at least one capital letter.",
]

username = GetInput("username", username_criteria)
print()
password = GetInput("password", password_criteria)

print()
print("Thank you, you have been registered as:")
print("username: " + str(username))
print("password: " + str(password))
