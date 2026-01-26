# Abstraction means hiding the complex implementation details of a class and showing only the important things. 
class Car:
    def __init__(self):
        self.acceletor=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.acceletor=True
        self.clutch=True
        print("Car Started...")
car1=Car()
car1.start()        
#  see here I call start() to use the car. 
# I don't need to know the internal details like how the acceletor and clutch  work.
# This is abstraction — hiding complexity and showing only the important functionality.
