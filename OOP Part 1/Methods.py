# Methods are functions that belong to objects.
# In class, there are two types of things stored:
# 1.data [attribute] ,
# 2.methods


# Attribute → what the object has
# Method → what the object does
class Car:
    shop_name='Ab shop'
    def __init__(self,name):
        self.name=name
    def run(self):
        print(self.name,'is running.')    

c1=Car('BMW')  
c1.run() 

class Car:
    shop_name='Ab shop'
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def run(self):
        print(self.name,'is running.')    
    def run_speed(self):
        return self.speed 

c1=Car('BMW',120)  
c1.run()  
print(c1.run_speed())



class Car:
    speed=0
    started=False
    def start(self):
        self.started=True
        print('car start')
    def in_speed(self ,add):
        if self.started:
            self.speed=self.speed + add
            print('vrom')
        else:
            print('You need to start your car first')
    def stop(self):
        self.speed=0
        print('stop the car')       
c1=Car()
c1.start()
c1.in_speed(40) 
c1.stop()

