#A user enters a 10-digit phone number.
# The system:
# Displays it in international format
# Shows only the last 4 digits for privacy
number=input("enter your phone number +91 :")
if(len(number)==10):
    print("in international format +91",number)
    print("XXXXXX"+number[6:])
else:
    print("invalid number")