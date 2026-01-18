# Attributes has to types.
# 1.class -> Class.attr 
# 2. Instance -> obj.attr


# Class Attribute : A variable that is shared by all instances of a class.
class Student:
    schoolName='ABC School' # class Attribute

# Instance Attribute : A variable that is unique to each individual object of a class,
# which is defined inside the __init__ method.
class Student:
    def __init__(self,name ,age):
        self.name=name # instance attribute
        self.age=age   # instance attribute