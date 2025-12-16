#type casting : type conversion : converting data from one type to 
#another type (explict conversion)

#datatype(variablename)

x = 100
print(type(x))
print(x)
fx = float(x)
print(fx)
print(type(fx))

y=100.56
print(y)
iy = int(y)
print(iy)

#converting numbers stored as string to int/float

s="10000"
print(type(s))
fs = float(s)
print(fs)
print(type(fs))

i="1000a"
fi = float(i)
#we get an error, as all the characters are not digits

