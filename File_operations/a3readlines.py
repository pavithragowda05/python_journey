#readlines() : reads the data from the current pointer posisiton till 
#end of the file and returns the data as list.
#each line of data will be one element of list, data are splited on
#the basis of \n

myfile = open("C:\\pavi\\a0rfile.txt","r")
data = myfile.readlines()
print(data)
myfile.close()

for x in data:
    # print(x)
    print(x.strip())