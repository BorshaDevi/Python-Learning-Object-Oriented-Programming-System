# # 1.Create student class that takes name and marks of 3 subjects as arguments in constructor.
# # Then create a method to print the average.
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum +=i
#         print(self.name, ' your average is ', sum//len(self.marks))    
              

# s1=Student('Max',[99,97,98]) 
# s1.average()    
# print(s1.name,s1.marks)

# #  we can change our attribute name directly.
# # Like
# s1.name='Arjun'
# s1.average() 

# # 2. Create Account class with 2 attributes -balance & account no.
# # create methods for debit , credit & printing the balance.
# class Account:
#     def __init__(self,balance,account_No):
#         self.balance=balance
#         self.account_No=account_No
#     def debit(self,withDraw):
#         if(withDraw>self.balance):
#             print('You do not have enough money.')
#             return  
#         self.balance=self.balance - withDraw  
#         print('Tk.',withDraw,'was debited')  
#         print('total balance', self.get_balance())   
#     def credit(self,addMoney): 
#         self.balance= self.balance + addMoney
#         print('Tk.',addMoney,'was credited')
#         print('total balance', self.get_balance())   
#     def get_balance(self):
#         return self.balance
         

# a=Account(1000,12345678)
# a.debit(400) 
# a.credit (500)
# # print(a.get_balance())


# # 3. Create a Student class that has:
# # attributes: name, roll, marks
# # method: display_info() → prints student details
# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def display_info(self):
#         print(f'The student name is {self.name} The student roll is {self.roll} The student all subjects marks are {self.marks}')  
#     def average_marks(self):
#         return sum(self.marks)/len(self.marks)    
# s1=Student('Alex',1,[82,45,60])
# s1.display_info() 
# print(f"average marks {s1.average_marks()}") 
# print(f"average marks {s1.average_marks():.2f}") # after . how many digit we need [.2f] means 2 digit.

# # 4.Create a Car class with:
# # attributes: 
# # method: show_car() Create 3 car objects and print their info
# class Car:
#     def __init__(self,brand, model, price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def show_car(self):
#         print(f"This car is {self.brand} brand. This model is {self.model} and this car price is {self.price:,.2f} Taka.")
# car1=Car('BMW','R15',1000000)
# car2 = Car('Toyota', 'Corolla', 2500000)
# car3 = Car('Honda', 'Civic', 2000000)
# car1.show_car()
# car2.show_car()
# car3.show_car()

# # 5.Create a Rectangle class with:
# # attributes: length, width
# # method: area()
# # method: perimeter()
# class Rectangle():
#     def __init__(self,length, width):
#         self.length=length
#         self.width=width
#     def area(self):
#         area=self.length*self.width
#         return area
#     def perimeter(self):
#         perimeter=2*(self.length+self.width)
#         return perimeter     

# rec1=Rectangle(6,5)
# print(f"Area{rec1.area()}" )       
# print(f"perimeter{rec1.perimeter()}" )   

# # 6.Create an Employee class:
# # attributes: name, basic_salary
# # method: calculate_salary()
# # Rules:
# # HRA = 20% of basic
# # DA = 10% of basic
# # Return total salary  
# class EmployeeSalary():
#     def __init__(self,name, basic_salary):
#         self.name=name
#         self.basic_salary=basic_salary
#     def calculate_salary(self):
#         HRA= (self.basic_salary * 20)/100
#         DA=  (self.basic_salary * 10)/100
#         total_salary=HRA + DA + self.basic_salary
#         return total_salary


# employ1=EmployeeSalary('Alex',12000)   
# print( (f'Employee {employ1.name} is total salary {employ1.calculate_salary():.2f}'))  


# # 7. Create a Mobile class:
# # attributes: brand, price
# # method: apply_discount(percent)
# # Update the price after discount.

# class Mobile:
#     def __init__(self, brand, price):
#         self.brand=brand
#         self.price=price
#         self.original_price = price
#     def apply_discount(self,percent):
#         discount=self.original_price  *(percent/100)
#         self.price =self.original_price - discount
#         return self.price

# mob1=Mobile('Realme',15000)
# print(f"This mobile brand is {mob1.brand} and this price {mob1.apply_discount(10):.2f}")


# # 8. Create a Book class:
# # attributes: title, author, available (True/False)
# # methods:
# # borrow_book()
# # return_book()
# # If book not available, show message.
# class Book:
#     def __init__(self,title, author, available=True):
#         self.title=title
#         self.author=author
#         self.available=available
#     def borrow_book(self):
#         if self.available == True:
#             print(f"please take your book")
#             self.available=False
#         else:
#             print('This book is not available.')    
#     def return_book(self):
#         self.available=True
#         print("Thank you for return book")
# c1=Book('MyLife','Alex')
# c2=Book('MyLife','Alex')
# c1.borrow_book()
# c2.borrow_book()
# c1.borrow_book()
# c1.return_book()
# c1.borrow_book()

# # 9.Create a Product class:
# # attributes: name, price, quantity
# # method: total_price()
# # Create multiple objects and calculate grand total.
# products=[]
# class Product:
#     def __init__(self,name, price, quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def total_price(self):
#          return self.price * self.quantity
# products.append(Product('apple',10,5)) 
# products.append(Product('mango',5,2)) 
# products.append(Product('banana',5,4)) 
# products.append(Product('lici',6,5)) 
# products.append(Product('jackfruit',20,3)) 
# print(products)

# grand_total=0
# for p in products:
#     # print(p.total_price())
#     grand_total +=p.total_price()
# print(grand_total)    

# # 10.Create an ATM class:
# # attributes: pin, balance
# # methods:
# # check_pin(pin)
# # withdraw(amount)
# # check_balance()
# # Withdrawal only works if PIN is correct.

# class ATM:
#     def __init__(self,pin,balance):
#         self.pin=pin
#         self.balance=balance
#     def check_pin(self, entered_pin):
#         if(self.pin == entered_pin):
#             return True
#         else:
#             print("PIN is not correct")
#             return False
            
#     def withdraw(self,entered_pin,amount):
#         if self.check_pin(entered_pin):
#             if amount > self.balance:
#                 return print(f"Insufficient balance")
#             else:
#                 self.balance -=amount
#                 print(f"Successfully withdraw {amount} tk.")
#         else:
#             print('Cannot withdraw')

#     def check_balance(self,entered_pin):
#         if self.check_pin(entered_pin):
#             return print(f"Now your total balance is {self.balance} tk.") 
#         else:
#             print("Cannot show balance due to wrong PIN")   
        
# c1=ATM(12345,1000)
# c1.withdraw(12345,500) 
# c1.check_balance(1234)   

# # 11. Create a Person class:
# # attributes: name, age
# # method: is_adult()
# # If age ≥ 18 → Adult, else Minor.
# class Person:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
#     def is_adult(self):
#         if self.age >=18:
#             print('Adult')
#         else:
#             print('Minor')  
# p1=Person('Alex',17)       
# p1.is_adult()           

# Qs:12. Define a Circle class to create a circle with radius r using the constructor.
    # Define an Area() method of the class which calculates the area of the circle.
    # Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        area=(3.1416) * (self.radius**2)
        print(area)
    def Perimeter(self):
        perimeter= (2*3.1416 *self.radius)
        print(perimeter)
c1=Circle(21) 
c1.Area()               
c1.Perimeter()               



# Qs:13. Define a Employee class with attributes role,department & salary.This class also as a showDetails() method.
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print (f"Employee role is {self.role} . Department {self.department} and salary {self.salary}")
e1=Employee("software Engineer","IT",50000)
e1.showDetails()
# Qs: 14  Create an Engineer class that inherits properties from Employee & has additional attributes:name & age. 
class Engineer(Employee): 
    def __init__(self,name,age,role,department,salary):
        self.name=name
        self.age=age
        super().__init__(role,department,salary)
    def showEngineer(self):    
        print(f"Employee name {self.name},age {self.age}")
        super().showDetails()

eng=Engineer('Rahul',25,"Backend Developer","IT",50000)
eng.showEngineer()        
       

