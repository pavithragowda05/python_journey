#writing data to the file :

#we can open the file in w mode : (write) or a mode (append)

#when we open the file in w mode it will checks for the file in the given 
#path, if file exists then it will overwrite the file, otherwise
#it will create new file. 

#when we open the file in a mode it will checks for the file in the given
#path, if file exists then it will append the data to the file, otherwise
#it will create a new file.

#writing input data to the file :

#file.write(data)

wfile = open("C:\\pavi\\cwrite0.txt","w")
header = "name,age,salary"
wfile.write(header+"\n")
name = input("Enter name :")
age = int(input("Enter age :"))
salary = int(input("Enter Salary :"))
wlist = [name,str(age),str(salary)]
wstr = ','.join(wlist)
print(wstr)
wfile.write(wstr+"\n")
wfile.close()