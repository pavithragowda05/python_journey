#find number of student in each grade
rfile=open("C:\\pavi\\estudout.txt")
head=rfile.readline()
data=rfile.readlines()
newdict={}
for x in data:
    w=x.strip().split(",")
    print(w)
    g=w[-1]
    if newdict.get(g)==None:
        newdict[g]=1
    else:
        newdict[g]+=1
print("number of student in each grade")        
for x in newdict: 
    print(x,":",newdict[x])
