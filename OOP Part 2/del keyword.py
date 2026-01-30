# Used to delete object properties or object itself.

class Student:
    def __init__(self,name):
        self.name=name
s1=Student('Alex')  

del s1.name  # object properties delete.
print(s1.name) # give me an error .because s1.name is deleted.

class Car:
    def __init__(self,brand):
        self.brand=brand
c1=Car('BMW')        
del c1 # object delete
print(c1)  # give me an error .because c1 object is deleted.