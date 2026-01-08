#readline() : reads the data from the current pointer posisiton till 
#end of the line and moves the pointer to the next line.

myfile = open("C:\\pavi\\a0rfile.txt","r")
data = myfile.readline()
data2 = myfile.readline()
print(data)
print(data2)