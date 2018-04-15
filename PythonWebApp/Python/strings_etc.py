# x = set()
#
# x.add(1)
# x.add(2)
# x.add(4)
#
# x.add(4)
# x.add(4)
# print(x)
#
# converted = set ([1,1,1,1,2,2,2,3,3,3,3])
# print(converted)

#Strings

# mystring = "Hello World"
# #print(mystring[3])
#
# #Slicing
# #print(mystring[::2])
#
# #Upper
# # x = mystring.split("o")
#
# #Print formatting
# x = "Item One: {y} Item Two: {x}".format(x = "dog",y = "cat")
# print(x)
# print(mystring)


#Lists

# mylist = [1,2,3]
# # mylist = ['sagasrojnasraslng', 1,2,3,4,True,"asfsaf",[1,2,3]]
# print(len(mylist))

# mylist = [4,6,3,2,5,7,9]
# print("before reassignment:")
# print(mylist)
# mylist[0] = "new item"
# print("after reassignment:")
# print(mylist)
# listtwo = ["x",'y','z']
# mylist.extend(listtwo)

# item = mylist.pop(0)
# print(mylist)
# print(item)

#Reverse and Sort
# mylist.reverse()
# mylist.sort()

#Nested List Index

# mylist = [1,2,['x','y','z']]

#List Comprehension

matrix = [[1,2,3],[4,5,6,],[7,8,9]]

first_col = [row[0] for row in matrix]
print(first_col)
