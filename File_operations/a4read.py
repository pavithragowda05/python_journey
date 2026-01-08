#read() : reads the data from current pointer position till end of the 
#file and return data as string.

#read(n) : reads n bytes of data from current pointer position.

#seek(n) : moves the record pointer to the nth byte

myfile = open("C:\\pavi\\a0rfile.txt","r")
# data = myfile.read(10)
# data2 = myfile.read()
#print(data)
#print(data1)
myfile.seek(10)
data = myfile.read()
print(data)