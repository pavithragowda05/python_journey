# f.Higest item purchased by Females and Males  
rfile=open("C:\\pavi\\dsaleout.txt")
head=rfile.readline()
data=rfile.readlines()
rfile.close()
male={"itemname":"","qty":0}
female={"itemname":"","qty":0}
for x in data:
    w=x.strip().split(",")
    print(w)
    gn=w[2]
    qty=int(w[5])
    iname=w[3]
    if gn=="m" and qty>male["qty"]:
        male["itemname"]=iname
        male["qty"]=qty
    elif gn=="f" and qty>female["qty"]:
        female["itemname"]=iname
        female["qty"]=qty    

print(f"the {male['itemname']} is purshased highest by male")
print(f"the {female['itemname']} is purchased by highly by female")