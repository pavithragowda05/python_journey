import mylib as ml
myfile=open("C:\\pavi\\estumarks.txt")
head=myfile.readline()
data=myfile.readlines()
myfile.close()
new=[]
for x in data:
    w=x.strip().split(",")
    # print(w)
    s1=int(w[-6])
    s2=int(w[-5])
    s3=int(w[-4])
    s4=int(w[-3])
    s5=int(w[-2])
    s6=int(w[-1])
    tot=s1+s2+s3+s4+s5+s6
    avg=(tot/600)*100
    grade=ml.fn_grade(s1,s2,s3,s4,s5,s6,avg)
    tup=(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],str(tot),str(avg),grade)
    new.append(tup)
# for x in new:
#     print(x) 
wfile=open("C:\\pavi\\estudout.txt","w") 
whead="id,name,gender,branch,s1,s2,s3,s4,s5,s6,totalmarks,average,grade"     
wfile.write(whead+"\n")
for x in new:
    wstr=",".join(x)
    wfile.write(wstr+"\n")
wfile.close()    