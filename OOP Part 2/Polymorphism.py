
# # When the same operator is allowed to have different meanings  according to the context.
# print(1+2) # 3  additions .(number type)
# print("Toma"+"to" ) # Tomato concatenation.(str type)
# print([1,2,3] + [4,5,6]) # [1,2,3,4,5,6] combines two lists. (list type)
# # This is an example of polymorphism  because the same operator performs different actions depending on the data type.

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

num1=Complex(1,4)
num1.showNumber() 

num2=Complex(6,5)
num2.showNumber() 

# Dunder function/ magic method:
# In python, methods that have double underscore before and after their name are called dunder function/magic method.
# There are so many dunder function in python.
# __add__ -> a+b
# __sub__ -> a-b
# __mul__ -> a*b
# __truediv__ -> a/b
# __mod__ -> a % b
# __floordiv__ -> a//b