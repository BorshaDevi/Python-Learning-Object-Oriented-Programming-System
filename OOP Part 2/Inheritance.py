# Inheritance allows code reusability by creating a relationship between classes.
class Car: # parent
    @staticmethod
    def start():
        print('Car Started')
    @staticmethod    
    def stop():
        print('Car Stopped')

class ToyotaCar(Car): #child # ToyotaCar inherits from Car
    def __init__(self,name,color):
        self.name=name
        self.color=color      
c1=ToyotaCar('FA',"blue")
print(c1.name)                
c1.start() 
# ToyotaCar can use start() because it inherits from the Car class, and inheritance allows 
# a child class to access the methods of its parent class.



# Inheritance Types:

# 1.Single Inheritance: Single inheritance means one parent class and one child class.
class Car: 
    @staticmethod
    def start():
        print('Car Started')
    @staticmethod    
    def stop():
        print('Car Stopped')
class ToyotaCar(Car):
    def __init__(self,name,color):
        self.name=name
        self.color=color      
c1=ToyotaCar('FA',"blue")
print(c1.name)                
c1.start() 

# 2.Multi-level Inheritance: Multilevel inheritance means parent → child → grandchild.

class Car: 
    @staticmethod
    def start():
        print('Car Started....')
    @staticmethod    
    def stop():
        print('Car Stopped')
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand 
class Truck(ToyotaCar):
    def __init__(self, type):
        self.type=type               
car1=Truck('fuel')
car1.start()

# 3.Multiple Inheritance: Multiple inheritance means one child class inherits from more than one parent class.
class A:
    var1=('welcome to A')
class B:
    var2=("welcome to B")
class C(A,B):
    var3=("Welcome to C")
    
var=C()
print(var.var1)            
print(var.var2)   

class Engine:
    def engine_type(self):
        print('fuel engine')
class Feature:
    def safety(self):
        print("Airbags and ABS")
class Car(Engine,Feature):
    def brand(self):
        print('Toyota')
c1=Car()
c1.safety()
c1.engine_type()