# Then use the finalitemlist to find the following: 
rfile=open("C:\\pavi\\dsaleout.txt")
head=rfile.readline()
data=rfile.readlines()
rfile.close()
count=0
for x in data:
    w=x.strip().split(",")
    # print(w)
    count+=1
print(count,"customers did bisness today in our shop")    
