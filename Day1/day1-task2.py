# A user tries to log in by entering a username.
# The system checks whether the input is empty or valid and responds accordingly.

# Concepts used:
# String handling, conditional logic

username = input("Enter your username: ")
if(len(username)!=0):
    print(f"welcome {username}!")
    print("your login successful")
else:
    print("username is not entered!")
    print("Try again!")

