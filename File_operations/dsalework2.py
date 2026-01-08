# b.Total customers did the business based on gender 
rfile=open("C:\\pavi\\dsaleout.txt")
head=rfile.readline()
data=rfile.readlines()
rfile.close()
newdict={}
for x in data:
    w=x.strip().split(",")
    gn=w[2]
    if newdict.get(gn)==None:
        newdict[gn]=1
    else:
        newdict[gn]+=1
for x in newdict:
    print(x,":",newdict[x])            
