# e.Which category item sold highest today 
rfile=open("C:\\pavi\\dsaleout.txt")
head=rfile.readline()
data=rfile.readlines()
rfile.close()
newdict={}
for x in data:
    w=x.strip().split(",")
    c=w[4]
    itm=int(w[5])
    if newdict.get(c)==None:
        newdict[c]=itm
    else:
        newdict[c]+=itm
# for x in newdict:
#     print(x,":",newdict[x])   
e=newdict["E"]
f=newdict["F"]
c=newdict["C"]
# print(e,f,c)
if e>f and e>c:
    print("electronic item saled high")
elif f>e and f>c:
    print("food item slaed high") 
elif c>f and c>e:
    print("cloths soled high")
else:
    print("all are equal")           