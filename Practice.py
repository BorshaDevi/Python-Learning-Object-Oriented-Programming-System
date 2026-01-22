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