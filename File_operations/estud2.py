#find highest scorer based on gender
rfile=open("C:\\pavi\\estudout.txt")
head=rfile.readline()
data=rfile.readlines()
male={"name":"" ,"score":0}
female={"name":"" ,"score":0}
for x in data:
    w=x.strip().split(",")
    gn=w[2]
    na=w[1]
    m=int(w[-3])
    if gn=="m" and m>male["score"]:
        male["name"]=na
        male["score"]=m
    elif gn=="f" and m>female["score"]:
        female["name"]=na
        female["score"]=m
print(f"highest scorer in female {female['name']} and is marks {female['score']}")
print(f"highest scorer in male {male['name']} and is marks {male['score']}")
        