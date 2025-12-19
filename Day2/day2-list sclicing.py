#list extraction / list sclicing :

#list[index] : returns the data in the given index

#list[start:end] : returns all the data from the given start index 
#till endindex-1

#list[:endindex] : returns all the data from the 0 index till given
#end index-1

#list[startindex:] : retruns all the data from the given start index
#till end of the list

#list[start:end:step]

#list[-index] : returns the data from end of the list
mylist = [10,20,30,40,50,60,70,80,90,100]
print(mylist[3])
print(mylist[3:8])
print(mylist[:6])
print(mylist[4:])
print(mylist[-1])
print(mylist[-5:-1])
print(mylist[2:8:2])

#to reverse the entire list:
print(mylist[::-1])

