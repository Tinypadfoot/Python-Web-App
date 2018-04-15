# mylist = [1,2,3]
# mylist.append(4)
#
# print(mylist)

# print(type([1,2,3]))

#Everything in python is an object

# class Sample_class():
#     pass
#
# x = Sample_class()
# print(type(x))
#
# class Dog():
#
#     # Class Object Attribute
#     species = "mammal"
#
#     # pass
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog("Lab","Sammy")
# # other_dog = Dog(breed = "Husky")
# print(mydog.breed)
# # print(other_dog.breed)
# print(mydog.name)
# print(mydog.species)


# class Circle():
#     pi = 3.14
#
#     def __init__(self,radius=1):
#         self.radius = radius
#
# # Methods
#
#     def area(self):
#         return self.radius*self.radius * Circle.pi
#
#     def set_radius(self,new_r):
#         self.radius = new_r
#
# myc = Circle(3)
# # myc.radius = 100
# myc.set_radius(999)
# print(myc.area())

#Inheritance
# class Animal():
#     def __init__(self):
#         print("Animal Created")
#
#     def who_am_I(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         # Animal.__init__(self)
#         print("Dog Created")
#
#     def bark(self):
#         print("Woof!")
#
#     def eat(self):
#         print("Dog Eating")
#
# # mya = Animal()
# mydog = Dog()
# mydog.who_am_I()
# mydog.eat()
# mydog.bark()



#Special Methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed!")


b = Book("Python", "Jose", 200)
del b
# print(b)
# print(len(b))

# mylist = [1,2,3]
# print(mylist)
