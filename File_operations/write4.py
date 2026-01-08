wfile = open("C:\\pavi\\cwrite3.txt","a")
header = "name,age,salary"
wfile.write(header+"\n")
n=int(input("enter how much data:"))
for x in range(n):
    name = input("Enter name :")
    age = int(input("Enter age :"))
    salary = int(input("Enter Salary :"))
    wlist = [name,str(age),str(salary)]
    wstr = ','.join(wlist)
    print(wstr)
    wfile.write(wstr+"\n")
wfile.close()