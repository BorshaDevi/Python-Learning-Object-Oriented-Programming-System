# 1.Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in self.marks:
            sum +=i
        print(self.name, ' your average is ', sum//len(self.marks))    
              

s1=Student('Max',[99,97,98]) 
s1.average()    
print(s1.name,s1.marks)

#  we can change our attribute name directly.
# Like
s1.name='Arjun'
s1.average() 

# 2. Create Account class with 2 attributes -balance & account no.
# create methods for debit , credit & printing the balance.
class Account:
    def __init__(self,balance,account_No):
        self.balance=balance
        self.account_No=account_No
    def debit(self,withDraw):
        if(withDraw>self.balance):
            print('You do not have enough money.')
            return  
        self.balance=self.balance - withDraw  
        print('Tk.',withDraw,'was debited')  
        print('total balance', self.get_balance())   
    def credit(self,addMoney): 
        self.balance= self.balance + addMoney
        print('Tk.',addMoney,'was credited')
        print('total balance', self.get_balance())   
    def get_balance(self):
        return self.balance
         

a=Account(1000,12345678)
a.debit(400) 
a.credit (500)
# print(a.get_balance())


# 3. Create a Student class that has:
# attributes: name, roll, marks
# method: display_info() → prints student details
class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display_info(self):
        print(f'The student name is {self.name} The student roll is {self.roll} The student all subjects marks are {self.marks}')  
    def average_marks(self):
        return sum(self.marks)/len(self.marks)    
s1=Student('Alex',1,[82,45,60])
s1.display_info() 
print(f"average marks {s1.average_marks()}") 
print(f"average marks {s1.average_marks():.2f}") # after . how many digit we need [.2f] means 2 digit.

# 4.Create a Car class with:
# attributes: 
# method: show_car() Create 3 car objects and print their info
class Car:
    def __init__(self,brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def show_car(self):
        print(f"This car is {self.brand} brand. This model is {self.model} and this car price is {self.price:,.2f} Taka.")
car1=Car('BMW','R15',1000000)
car2 = Car('Toyota', 'Corolla', 2500000)
car3 = Car('Honda', 'Civic', 2000000)
car1.show_car()
car2.show_car()
car3.show_car()

# 5.Create a Rectangle class with:
# attributes: length, width
# method: area()
# method: perimeter()
class Rectangle():
    def __init__(self,length, width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length*self.width
        return area
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        return perimeter     

rec1=Rectangle(6,5)
print(f"Area{rec1.area()}" )       
print(f"perimeter{rec1.perimeter()}" )   

# 6.Create an Employee class:
# attributes: name, basic_salary
# method: calculate_salary()
# Rules:
# HRA = 20% of basic
# DA = 10% of basic
# Return total salary  
class EmployeeSalary():
    def __init__(self,name, basic_salary):
        self.name=name
        self.basic_salary=basic_salary
    def calculate_salary(self):
        HRA= (self.basic_salary * 20)/100
        DA=  (self.basic_salary * 10)/100
        total_salary=HRA + DA + self.basic_salary
        return total_salary


employ1=EmployeeSalary('Alex',12000)   
print( (f'Employee {employ1.name} is total salary {employ1.calculate_salary():.2f}'))  


# 7. Create a Mobile class:
# attributes: brand, price
# method: apply_discount(percent)
# Update the price after discount.

class Mobile:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price
        self.original_price = price
    def apply_discount(self,percent):
        discount=self.original_price  *(percent/100)
        self.price =self.original_price - discount
        return self.price

mob1=Mobile('Realme',15000)
print(f"This mobile brand is {mob1.brand} and this price {mob1.apply_discount(10):.2f}")



      
          


