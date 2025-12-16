#strings : string is collection characters, stored under a name,
#each character is stored in seperate index.
#index starts 0 and it is alway int.

#string extraction / string sclicing : 

#str[index]: retruns the character of the given index

#str[start:end] :returs the characters from the given start index
#till end index -1

#str[:endindex] : when start index is not specified, it will take
#start index as 0 and returns the characters till endindex -1

#str[startindex:] : returns all the characters from given start index
#till end of the string.

#str[-index] : when index is negative it will characters from the 
#end of the string.

mystr = "hello world i am pavithra from second year CSE"
print(mystr)

print(mystr[4])
print(mystr[4:15])
print(mystr[:6])
print(mystr[6:])
print(mystr[-1])
print(mystr[-7:-1])