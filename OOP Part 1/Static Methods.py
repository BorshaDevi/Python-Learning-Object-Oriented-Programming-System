# Static Method is used when do not need an object and only need logic.



#  Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
#  without permanently modifying it.



class Utils:
    @staticmethod   # this is called decorator.
    def add (a,b):
        return a+b
#  see ,there are not mention any object.
print(Utils.add(2,2))



class Customer:
    def __init__(self,name):
        self.name=name

    # def hello():
    #     print('Hello')     # If I print like that, it's gives error.
    
    #  so for that , we need to mention @staticmethod 

    @staticmethod
    def hello():
        print('Hello')  

    def history_c(self,entry):
        self.entry=entry  

    @staticmethod
    def calculet(a,b):
        return a+b



c1=Customer('Alex')
Customer.hello()
c1.history_c('9:00 am')
print(Customer.calculet(2,5))



