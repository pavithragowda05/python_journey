#writing multiple data to the file :

name = ['amar','akbar','antony']
age = [40,45,50]
salary = [90000,60000,80000]

wfile = open("C:/pavi/cwrite1.txt","w")
header = "name,age,salary"
wfile.write(header+"\n")
elist = list(zip(name,age,salary))
for x in elist:
    wlist = [x[0],str(x[1]),str(x[-1])]
    wstr = ','.join(wlist)
    print(wstr)
    wfile.write(wstr+"\n")
wfile.close()