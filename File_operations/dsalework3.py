# c.Total net amount collected based on item category 

rfile=open("C:\\pavi\\dsaleout.txt")
head=rfile.readline()
data=rfile.readlines()
rfile.close()
newdict={}
for x in data:
    w=x.strip().split(",")
    c=w[4]
    amt=int(w[-1])
    if newdict.get(c)==None:
        newdict[c]=amt
    else:
        newdict[c]+=amt
for x in newdict:
    print(x,":",newdict[x])            