#find persentage of male passed and female passed
rfile=open("C:\\pavi\\estudout.txt")
head=rfile.readline()
data=rfile.readlines()
rfile.close()
newdict={}
male=0
female=0
for x in data:
    w=x.strip().split(",")
    gn=w[2]
    if gn=="m":
        male+=1
    else:
        female+=1    
    grade=w[-1]
    if grade=="firstclass" or grade=="distinction" or grade=="secondclass" or grade=="thirdclass":
        if newdict.get(gn)==None:
            newdict[gn]=1
        else:
            newdict[gn]+=1     
# print("tatal male and female",male, female)        
mp=newdict["m"]
fp=newdict["f"] 
# print("male and female passed:",mp,fp)          
print("persentage of male passed:",(mp/male)*100)
print("persentage of female passed:",(fp/female)*100)
