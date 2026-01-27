# Wrapping data and functions into a single unit(object)
# Keeping data safe inside a class and controlling access through methods, so outside code should not change it directly.

class BankAccount:
    def __init__(self):
        self._balance=0
        
    def deposit(self,amount):
        self._balance += amount
    def getBalance(self):
        return self._balance
acc=BankAccount()
acc.deposit(1000)
print(acc.getBalance())            
# See here,I deposit and then I see how many taka in my account.
acc._balance=10000 #Not allowed: direct access to private variables. This balance is encapsulation. Because this is private.
