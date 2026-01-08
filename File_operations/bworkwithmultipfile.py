#working with multiple files :

#master file and transaction file
#master file and detail file
#parent file and child file

#master file : consists for master information (unique data with id).

#transaction file : uses id from the master file data can be repeated.

#we require one common column when we are working with multiple files.

#read all the masterfiles and create dictionary

dfile = open("C:\\pavi\\bplacemaster.txt")
dhead = dfile.readline()
data = dfile.readlines()
dfile.close()
pdict = {}
for x in data:
    w=x.strip().split(',')
   #print(w)
    pdict[int(w[0])] = w[1]
print(pdict)

bfile=open("C:\\pavi\\bbranchmaster.txt")
head=bfile.readline()
bdata=bfile.readlines()
bdict={}
for x in bdata:
    w=x.strip().split(",")
    bdict[int(w[0])]=w[1]
print(bdict)    
#read the data from studentmaster.txt and map idplace with idplace of 
#placemaster.txt and get place name.


sfile = open("C:\\pavi\\bstudmaster.txt")
head = sfile.readline()
sdata = sfile.readlines()
sfile.close()
flist = []
for x in sdata:
    #print(x)
    w = x.strip().split(',')
    #print(w)
    placename = pdict.get(int(w[2]))
    branch=bdict.get(int(w[-1]))
    newtup = (w[0],w[1],placename,branch)
    flist.append(newtup)
for x in flist:
    print(x)
