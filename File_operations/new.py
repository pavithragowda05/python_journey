new=[]
n=int(input("enter how much passenger:"))
for x in range(n):
    name=input("enter your name:")
    place=input("place you did travel")
    fare=int(input("enter far"))
    tup=(name,place,fare)
    new.append(tup)
newdict={}
for x in new:  
    pls=x[1]
    if newdict.get(pls)==None:
        newdict[pls]=1
    else:
        newdict[pls]+=1
print(newdict)            
