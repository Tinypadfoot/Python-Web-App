# x = 25

def my_func():
     x = 50
     return x
#
# print(x)
# print(my_func())
my_func()
# print(x)

#Local Level

# lambda x: x**2

#Enclosing Function Leves

# name = "This is a global name."
#
# def greet():
#     name = "Sammy"
#
#     def hello():
#         print("Hello " + name)
#
#     hello()
#
# greet()
# print(name)

#Built-in Level
x = 50

def func():
    # print("x is:", x)
    # x = 1000
    # print("local x changed to:",x)

    # global x
    x = 1000
    return x

print("before func call, x is:",x)
# func()
# print(x)
x = func()
print("after func call, x is:",x)
