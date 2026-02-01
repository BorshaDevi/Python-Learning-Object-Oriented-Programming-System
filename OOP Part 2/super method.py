# super() means accessing the parent class (its methods or constructor).
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started....")
       
class Toyota(Car):
    def __init__(self, name,type):
        super().__init__(type) 
        self.name=name
        super().start()     
car1=Toyota('pario','fuel') 
print(car1.type)   


class Car: 
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print('Car Started....')
    @staticmethod    
    def stop():
        print('Car Stopped')
class ToyotaCar(Car):
    def __init__(self,brand,type):
        super().__init__(type)
        self.brand=brand 
class Truck(ToyotaCar):
    def __init__(self, name,brand,type):
        super().__init__(brand,type)
        self.name=name 
        
                      
car1=Truck('Tacoma',"Toyota","fuel")
print(car1.type)
print(car1.brand)
car2=Truck('Tundra','Toyota',"Gas")
print(car2.type)
print(car2.name)

