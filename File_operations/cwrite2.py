#reading data from the file, do the process and write output to another file

dfile = open("C:/pavi/bplacemaster.txt")
dhead = dfile.readline()
data = dfile.readlines()
dfile.close()
pdict = {}
for x in data:
    w=x.strip().split(',')
   #print(w)
    pdict[int(w[0])] = w[1]
print(pdict)

sfile = open("C:/pavi/bstudmaster.txt")
head = sfile.readline()
sdata = sfile.readlines()
sfile.close()
flist = []
for x in sdata:
    #print(x)
    w = x.strip().split(',')
    #print(w)
    placename = pdict.get(int(w[2]))
    newtup = (w[0],w[1],placename,w[3])
    flist.append(newtup)
for x in flist:
    print(x)

wfile = open("C:/pavi/cwrite2.txt","w")
head ="id,name,place,branch"
wfile.write(head+"\n")
for x in flist:
    wstr = ','.join(x)
    wfile.write(wstr+"\n")
wfile.close()