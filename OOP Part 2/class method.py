# A class method is a method that is related to the class and does not require any specific object.
# Note- static method can't access or modify class state & generally for utility.

class Person:
    name='anonymous'
    def hello(self,name):
        # print('hello',Person.name)  
        # see here,I access class attribute with Person.name.then question is ,how can I change the class attribute?
        #  there are so many way, 
        Person.name=name
        print('1st way to change the class attribute',name)
        self.__class__.name=name
        print('2nd way to change the class attribute',name)
p1=Person()
p1.hello('Alex')  
print(Person.name)   

# But the best practice is to use @classmethod to change the class attribute.so we use @classmethod.
class Person:
    name="anonymous"
    @classmethod
    def change_name(cls,name): # cls is a reference to the class itself, similar to how self refers to the instance.
        cls.name=name
p1=Person()
p1.change_name('Alex')
print(Person.name)