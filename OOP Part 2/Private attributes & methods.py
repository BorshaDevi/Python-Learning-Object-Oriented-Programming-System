# Private attributes & methods  are meant to be used only within the
#  class and are not accessible from outside the class.
#  If an attribute or method is private, use two underscores(__) before the attribute or method name.

#  In Python, when we use two underscores (__) before an attribute or method name,
# it becomes name-mangled, not truly private.


class Account:
    def __init__(self,acc_on,acc_pass):
        self.acc_on=acc_on
        self.acc_pass=acc_pass
a1=Account(1234,"abc123")
print(a1.acc_on)   
# This is not good practice to access and use passwords outside of class easily.    
print(a1.acc_pass) 

# so make the password to private.
class Account1:
    def __init__(self,acc_on,acc_pass):
        self.acc_on=acc_on
        self.__acc_pass=acc_pass
a1=Account1(1234,"abc123")
print(a1.__acc_pass) # It gives the error.

class Employee:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin # attribute private
    def __check_pin(self,entere_pin):  # method private
        if self.__pin == entere_pin:
            return True 
        else:
            return False
    def balance_check(self,pin):
        if self.__check_pin(pin):
            print('Your balance is 100') 
        else:
            print('Nothing')  
# Here, __pin and __check_pin are private attribute and method.
# They cannot be accessed from outside the class, but they can be accessed within the class.
# The private method __check_pin() is used inside the balance_check() method.
e1=Employee('Alex',1234)
e1.balance_check(1234)
