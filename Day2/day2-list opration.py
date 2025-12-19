#list is mutable in nature : list allows modification (we can modify the list)
#append() : (adding data to the end) adds the data to the end of the list
#list.append(data)

#insert() : inserts the element at given index
#list.insert(index,data)

#remove() : removes the given data from the list
#list.remove(data)

mylist = [10,20,30,40,50,60,70,80,90,100]
print(mylist)

mylist.append(200)
print(mylist)

mylist.insert(2,25)
print(mylist)

mylist.remove(25)
print(mylist)

#to modify the element
#list[index]=new value

mylist[3]=400
print(mylist)



