myfile=open("C:\\pavi\\aaa1.txt")
head=myfile.readline()
data=myfile.readlines()
myfile.close()
dep=[]
pls=[]
dat={}
for x in data:
    w=x.strip().split(",")
    print(w)
    p=w[2]
    dep.append(p)
    pl=w[3]
    pls.append(pl)
    if dat.get((pl,p))==None:
        dat[(pl,p)]=1
    else:
        dat[(pl,p)]+=1
# print(dat) 
newdat={}       
for k in pls:
    for i in dep:
        newdat[k,i]=0
# print(newdat)        

newdat.update(dat)
for x in  newdat:
    print(x,":",newdat[x])