s = 'django'

# print(s[0])
#
# print(s[-1])
#
# print(s[:4])
#
# print(s[1:4])
#
# print(s[4:])
# print(s[::-1])

l = [3,7,[1,4,'hello']]
# print("Before reassignment")
# print(l)
#
# l[-1][-1] = "Goodbye"
# print("After reassignment")
# print(l)

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# print(d1['simple_key'])
# # print(d2['k1']['k2']
# print(d2['k1']['k2'])
# # print(d3['k1']['nest_key'][0]
# print(d3['k1'][0]['nest_key'][1][0])
# mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
#
# x = set(mylist)
# print(x)

age = 4
name = "Sammy"

print("Hello my dog's name is {a} and he is {b} years old.".format(a=name,b=age))

# print("Hello my dog's name is")
