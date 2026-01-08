# 1. Point of sale task: accept n number of data as per sample: 
# Id 
# Customer name 
# Gender 
# Item name 
# Category: Electronics/Food/Cloths (E/F/C) 
# Price per unit: 
# Quantity 
# Find the amount = qty * price 
# Tax amount: as per the following : 
# For Electroncis 18%, Food 5% and for Cloths 15% GST 
# Find the NetAmount: amount +  taxamount 
# Create a FinalItemList of tuples as per sample : 
# [(1,rama,m,laptop,1,50000,50000,9000,59000) 
# Then use the finalitemlist to find the following: 
# a.Total customers did business in our shop today 
# b.Total customers did the business based on gender 
# c.Total net amount collected based on item category 
# d.Total tax collected based on item category 
# e.Which category item sold highest today 
# f.Higest item purchased by Females and Males  
# BEST Wishes from SVL Team. 


file=open("C:\\pavi\\dsaledata.txt")
head=file.readline()
data=file.readlines()
file.close()
newlist=[]
for x in data:
    # print(x)
    w=x.strip().split(",")
    # print(w)
    qty=int(w[-1])
    prs=int(w[-2])
    tamt=int(qty*prs)
    if w[-3]=="F":
        tax=int(tamt*(5/100))
    elif w[-3]=="E":
        tax=int(tamt*(18/100))
    elif w[-3]=="C":
        tax=int(tamt*(15/100))
    else:
        tax=int(0)
    net=tax+tamt    
    tup=(w[0],w[1],w[2],w[3],w[4],w[-1],w[-2],str(tamt),str(tax),str(net))
    newlist.append(tup)

# for x in newlist:
#     print(x) 
wfile=open("C:\\pavi\\dsaleout.txt","w")
head="id,name,gender,productname,category,quantity,totalprice,tax,netpric"
wfile.write(head+"\n") 
for x in newlist:
    wstr=",".join(x)
    wfile.write(wstr+"\n")
wfile.close()                  
