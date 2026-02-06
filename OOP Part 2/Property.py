# When an attribute value changes, calculations depending on that attribute may not update automatically. 
# Using @property methods ensures that every time the value changes, updated results are returned.

# In normal 
class Balance:
    def __init__(self,b_s,health):
        self.b_s=b_s
        self.health=health
        self.total=self.b_s + self.health   
e1=Balance(5000,2000)
print(e1.total) # see, here total value is 7000
e1.health=3000
print(e1.total) # And here total value is also 7000.But after changing the health ,total should be 8000.
#Using @property automatically updates the total value when the health attribute changes.

class Balance:
    def __init__(self,b_salary,health):
        self.basic_salary=b_salary
        self.health=health
    @property
    def totalBalance(self):
        return (self.basic_salary + self.health )

employee1=Balance(15000,5000)
# print(employee1.totalBalance())   
# When using @property, the method cannot be called like a function.
# Because @property allows methods to behave like read-only attributes.   
print(employee1.totalBalance)  # so use this. 

employee1.basic_salary=20000
print(employee1.totalBalance) 



   