#task : to find the total salary of the employees
#reading data from the tabular seperating header and data

efile = open("C:\\pavi\\aa0tabulateddata.txt")
header = efile.readline()
edata = efile.readlines()
efile.close()
#print(edata)
tot=0
print(header)
for x in edata:
    #print(x)
    w = x.strip().split(',')
    print(w)
    tot+=int(w[2])
print(f"Total salary {tot}")

#tasks :
#I. 
# 1.find the total salary based on gender
#2. find the total employees based on dno
#3. segregate employee names based on dno
#4. Write a function in your library fn_gender() to transfrom m to Male and
# f to Female, implement here, write a function fn_dname() to transfrom
#dno to deptname in your library and implement here, capitalize the name.
#sample output : ('101', 'Amar', '50000', 'Male', 'Admin')

