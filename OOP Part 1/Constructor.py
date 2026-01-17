# A constructor is a special method in Python that is automatically called when an object is created.

# Why use a constructor?
# Ans: We use a constructor to set initial values when an object is created.

# __init__  function
# This is a Python special method which is  called constructor.
# All classes have a function called __init__() which is always executed when the object is being initiated.


#This is called the default constructor.
class Student:
        def __init__(self):
                pass
s1 =Student() 

class Student:
        name='Alex'
        def __init__(self):  # Constructor is a special method. It can accept parameters and must have self as the first parameter.
                print('ADDing data in the database....')


s1=Student()
# we can pass multiple parameters in the constructor.

# parameterized constructors
class Student1:
        def __init__(self , fullname):
                self.name=fullname  # self.name is an instance (object) variable created inside the constructor.
                                    # self.name is called an attribute in programming.
                                    # fullname is the initial value of self.name.

s1=Student1('Alex')
print(s1.name)
# It is not mandatory to name the first parameter self; we can use any other name.
# It works, but people usually use self.

s2=Student1('Ratul')
print(s2.name)

class Car:
        def __init__(self,brand,color,price):
                self.brand=brand
                self.color=color
                self.price=price
car1=Car('BMw','Blue','$500')
print(car1.brand,car1.color,car1.price)
car2=Car('Toyota','red','$400')
print(car2.brand,car2.color,car2.price)
                
# What is self?
# Ans: Self is a reference to the current object.
# Like:
class Car:
    def __init__(self,name):
                self.name=name
c1=Car("BMW") # self