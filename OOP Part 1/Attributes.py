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


class Car:
    car_brand='BMW'
    def __init__(self,color,price):
        self.color=color
        self.price=price
car1=Car('blue',"$200")
print(Car.car_brand)   


class Car:
    car_brand='Toyota'# class attribute
    color='Anonymous' # Class attribute (default value if no color is provided)
                      
    def __init__(self,color, price):
        self.color=color # obj attribute . obj attribute > class attribute
        self.price=price
c1=Car('black','$300')
print(c1.color)        