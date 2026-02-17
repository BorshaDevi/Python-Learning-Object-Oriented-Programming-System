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


# 8. Create a Book class:
# attributes: title, author, available (True/False)
# methods:
# borrow_book()
# return_book()
# If book not available, show message.
class Book:
    def __init__(self,title, author, available=True):
        self.title=title
        self.author=author
        self.available=available
    def borrow_book(self):
        if self.available == True:
            print(f"please take your book")
            self.available=False
        else:
            print('This book is not available.')    
    def return_book(self):
        self.available=True
        print("Thank you for return book")
c1=Book('MyLife','Alex')
c2=Book('MyLife','Alex')
c1.borrow_book()
c2.borrow_book()
c1.borrow_book()
c1.return_book()
c1.borrow_book()

# 9.Create a Product class:
# attributes: name, price, quantity
# method: total_price()
# Create multiple objects and calculate grand total.
products=[]
class Product:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
         return self.price * self.quantity
products.append(Product('apple',10,5)) 
products.append(Product('mango',5,2)) 
products.append(Product('banana',5,4)) 
products.append(Product('lici',6,5)) 
products.append(Product('jackfruit',20,3)) 
print(products)

grand_total=0
for p in products:
    # print(p.total_price())
    grand_total +=p.total_price()
print(grand_total)    

# 10.Create an ATM class:
# attributes: pin, balance
# methods:
# check_pin(pin)
# withdraw(amount)
# check_balance()
# Withdrawal only works if PIN is correct.

class ATM:
    def __init__(self,pin,balance):
        self.pin=pin
        self.balance=balance
    def check_pin(self, entered_pin):
        if(self.pin == entered_pin):
            return True
        else:
            print("PIN is not correct")
            return False
            
    def withdraw(self,entered_pin,amount):
        if self.check_pin(entered_pin):
            if amount > self.balance:
                return print(f"Insufficient balance")
            else:
                self.balance -=amount
                print(f"Successfully withdraw {amount} tk.")
        else:
            print('Cannot withdraw')

    def check_balance(self,entered_pin):
        if self.check_pin(entered_pin):
            return print(f"Now your total balance is {self.balance} tk.") 
        else:
            print("Cannot show balance due to wrong PIN")   
        
c1=ATM(12345,1000)
c1.withdraw(12345,500) 
c1.check_balance(1234)   

# 11. Create a Person class:
# attributes: name, age
# method: is_adult()
# If age ≥ 18 → Adult, else Minor.
class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def is_adult(self):
        if self.age >=18:
            print('Adult')
        else:
            print('Minor')  
p1=Person('Alex',17)       
p1.is_adult()  

# Polymorphism :

# 1:
class Bird:
   def fly(self):
      pass         
class Sparrow():
   def fly(self):
      print("Sparrow can fly")
class Ostrich():
   def fly(self):
      print("Ostrich cannot fly")
birds =[Sparrow(),Ostrich()]
for bird in birds:
   bird.fly()
   
# 2 :
class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("Meow Meow")
class Dog(Animal):
    def sound(self):
        print('Bark Bark')
class Cow(Animal):
    def sound(self):
        print("Moo Moo")                   
animals=[Cat(),Dog(),Cow()]
for ani in animals:
    ani.sound()  



# 3:
class Payment:
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        pass    
class BkashPayment(Payment):
    def pay(self):
        print(f"{self.amount} pay using Bkash")   
class CardPayment(Payment):
    def pay(self):
        print (f"{self.amount} pay using Card")       
class CashPayment(Payment):
    def pay(self):
        print (f"{self.amount} pay using Cash")     
payments=[BkashPayment(50000),CardPayment(1000),CashPayment(20000)]
for pa in payments:
    pa.pay()



# 4:
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(3.1416 * (self.radius ** 2))
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length * self.width)
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print((0.5) *self.base* self.height)

shapes=[Circle(5),Rectangle(4,5),Triangle(6,4)]  
for shap in shapes :
    shap.area()  




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
# Qs: 14 . Create an Engineer class that inherits properties from Employee & has additional attributes:name & age. 
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
       
# QS:15 . Create a class called Order which stores item & its price.
        # Use Dunder function __gt__() to convey that:
            #  order1> order2 if price of order1 > price of order2.
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price > ord2.price

ord1=Order('Chips',50)
ord2=Order('Chocolate',30)
print(ord1 > ord2)

# 16. Compare Shapes
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length * self.width
        return area
    def __gt__(self,area2):
        check =self.area() > area2.area()
        return check
class Square():
    def __init__(self,length):
        self.length=length    
    def area(self):
        area=(self.length)**2
        return area
    

r1=Rectangle(3,4)   
s1=Square(4)                 
if(r1> s1):
    print('Rectangle is bigger')
else:
    print("Square is bigger")  


# 17:Container Length
class Bag:
    def __init__(self,list_it):
        self.list_item=list(list_it)
    def __len__(self):
        return len(self.list_item)
b=Bag(('lipstick','brush','powder'))
print(len(b)) 

# 18: Reverse Printing
class Message:
    def __init__(self,text):
        self.text=text
    def __str__(self):
        return self.text[::-1]
m=Message('Hello World')    
print(m)
# 19: Combining Shapes
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length * self.width    
        return area
    def __add__(self,area2):
        newlength=self.length +area2.length
        newWidth=self.width + area2.length
        return Rectangle(newlength,newWidth)
    def __str__(self):
        return (f"{self.length} is length and {self.width} is width of Rectangle.")
class Square(Rectangle): 
    def __init__(self, length):
        super().__init__(length,length)
        
r=Rectangle(3,4)
s=Square(4)
newShape=r + s
print(newShape)
print(newShape.area())

# 20: Implement __eq__ for Complex numbers → check if two numbers are equal.
class ComplexNumber:
    def __init__(self,nu1,nu2):
        self.nu1=nu1
        self.nu2=nu2
    def __eq__(self, num2):
        return self.nu1 == num2.nu1 and self.nu2 == num2.nu2
c1=ComplexNumber(3,4)    
c2=ComplexNumber(3,4)    
if(c1 == c2):
    print('2 numbers are equeal')
else:
    print('2 numbers are not equeal')          

#21: Implement __repr__ for debug-friendly printing.
class Debug:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __repr__(self):
        return (f"{self.name} and {self.roll}")    
d=Debug('Alex',10)
print(d)
#22: Combine __len__ and Polymorphism: create Polygon base class and different shapes → print number of sides using len().
class Polygon:
    def __init__(self,sides):
        self.sides=sides
    def __len__(self):
        return self.sides
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
class Square(Polygon):
    def __init__(self):
        super().__init__(4)

t=Triangle() 
print(len(t))  
s=Square()  
print(len(s)) 

# 23: Book Comparison -> pages return,compare two books depend on pages.
class Book:
    def __init__(self,title,pages):
        self.title= title
        self.pages= pages
    def __str__(self):
        return (f"This is {self.title} book and this pages length {self.pages}.")    
    def __len__(self):
        return self.pages
    def __gt__(self,seo2):
        compare=self.pages> seo2.pages
        return compare
b1=Book('A Little Life',200)
b2=Book('The Bance Code',400)
print(b1)
print(len(b1))
print(b2)
print(len(b2))
if (b1>b2):
    print(f"{b1.title} book length is bigger.")
else:
     print(f"{b2.title} book length is bigger.")   


# 24: BankAccount -> addition two account balance , check equal balance
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __add__(self,bal2):
        return self.balance + bal2.balance
    def __eq__(self,bal2):
        return self.balance == bal2.balance
    def __str__(self):
        return (f"{self.owner} is your balance {self.balance} ") 

own1=BankAccount("Alex",500)
print(own1)
own2=BankAccount("Eva",500)
value=own1 + own2
print(value)
if(own1 == own2):
    print(own1.owner ,'and ',own2.owner ,"youre balance are equal" )
else:
    print(own1.owner ,'and ',own2.owner ,"youre balance are not equal" )