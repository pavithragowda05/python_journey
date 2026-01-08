#task : to find the total salary of the employees

efile = open("C:\\pavi\\aa0tabulateddata.txt")
edata = efile.readlines()
efile.close()
#print(edata)
tot=0
for x in edata:
    #print(x)
    w = x.strip().split(',')
    print(w)
    tot+=int(w[2])
print(f"Total salary {tot}")

#note : we get an error as "salary" will be added with number