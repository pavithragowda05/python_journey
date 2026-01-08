#4. Write a function in your library fn_gender() to transfrom m to Male and
# f to Female, implement here, write a function fn_dname() to transfrom
#dno to deptname in your library and implement here, capitalize the name.
#sample output : ('101', 'Amar', '50000', 'Male', 'Admin')
import mylib as ml
myfile = open("C:\\pavi\\aa0tabulateddata.txt")
darta=myfile.readline()
edata = myfile.readlines()
myfile.close()
#print(edata)
newdict={}
gen=[]
id=[]
sal=[]
name=[]
dep=[]
for x in edata:
    # print(x)
    w=x.strip().split(",")
    # print(w)
    n=ml.def_name(w[1])
    name.append(n)
    id.append(w[0])
    sal.append(int(w[2]))
    g=ml.fn_gender(w[-2])
    gen.append(g)
    d=ml.fn_dname(int(w[-1]))
    dep.append(d)
    
   
flist=list(zip(id,name,sal,gen,dep))
for x in flist:
    print(x)