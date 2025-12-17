# <!-- A telecom company wants to build a small Python program that helps a customer recharge their phone.
# The program should:
# 1. Ask the user for:
# Their name (string)
# Their 10-digit mobile number (string)
# Recharge amount (number)
# 2. The system must:
# Validate the phone number has exactly 10 digits
# Calculate GST of 18%
# Calculate total bill = recharge + GST
# Show last 4 digits of the mobile number for privacy -->

name=input("enter your name: ")
number=input("enter your phone number: ")
recharge_amount=int(input("enter recharge amount:"))
if(len(number)==10):
    print(f"Hello {name}!")
    print("international number:+91-",number)
    print("Private view:","*"*6+number[-4:])
    print("Recharge:₹",recharge_amount)
    gst=(recharge_amount)*0.18
    print("total gst is:",gst)
    print("total bill: ",recharge_amount+gst)
    
else:
    print("invalid number entered!") 
    print("Try again")   
