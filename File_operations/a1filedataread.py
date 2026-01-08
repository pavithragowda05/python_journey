#file handling in python

#file : File is a collection of data/information stored in a secondary 
#storage device.

#file is identified by filename and type of the file is identified by
#extension name.

#ex : myfile.txt (mfile is the name of the file and txt is the extension
#name) (txt : text file, created using notepad)

#filename is the given by the user, and extension is given by software 
#we are using to create the file.

#working with text files :

#four steps to work with files :

#open the file ---------> read the data --------> process the data  
# ------> close the file

#files handling functions :
#open()
#read()
#readline()
#readlines()
#close()
#seek()

#open() : opens the file from given path and load the data to the memory
#variablename = open("path"\filename","mode")

#mode : w : wirte, r : read, a:append
#read mode is the default mode (r).

#read() : reads the data from the current pointer posistion till end of 
#the file and returns data as string.

#variablename = file.read()

#close() : closes the opend file and clears the memory.
#file.close()

# myfile = open("D:\\Ashwath\\ns_trainings\\Python\\LVP_Batch_2\\file1.txt","r")

#\\:to define the path, to avoid special characters like \n, \t..
#we use \\

#another method to define path is to using / (slash/forward slash)

myfile = open("C:\\pavi\\a0rfile.txt","r")
data = myfile.read()
print(data)
myfile.close()
print(type(data))
print(len(data))