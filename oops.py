
## Multi-level Inheritance
# class Animal:
#     def speak(self):
#         return 'Animal is speaking'
    
# class  dog(Animal):
#     def bark(self):
#         return 'Dog is barking'

# class child(dog):
#     def eat(self):
#         return 'Child is eating'

# d = child()
# print(d.speak())
# print(d.bark())
# print(d.eat())

### Multiple Inheritance

from ast import ClassDef
from re import L
from time import sleep

class Marks:

    totmarks = []
    classmarks = []
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name
        # self.marks= []
    def display(self):
        print(f'Name:{self.name}\nRoll no:{self.roll}')

class P(Marks):
    def physics(self):
        n1 = int(input('Enter Physics marks: '))
        self.totmarks.append(n1)

class C(Marks):
    def chem(self):
        n2 = int(input('Enter chem marks: '))
        self.totmarks.append(n2)

class M(Marks):
    def maths(self):
        n3 = int(input('Enter maths marks: '))
        self.totmarks.append(n3)

class overall(P,C,M,Marks):
    def marksheet(self):
        total = sum(self.totmarks)
        avg = total/len(self.totmarks)
        self.classmarks.append(total)
        print(f'Total Marks are:{total}\nAverage of {self.name} is:{avg}')
print('-------------------------///----------------------')
# class final(overall):
#     def output(self):
#         print(f'The Total average of class is: {sum(self.classmarks)/len(self.classmarks)}')
print('----//----')
n = int(input('Enter No of Students in class: '))
while n > 0:       
    roll=int(input('Enter student Roll  no: '))
    name=input('Enter Student Name: ')
    print('-----//----')
    M1 = Marks(roll,name)
    M1.display()
    P1 = P(roll,name)
    P1.physics()
    C1 = C(roll,name)
    C1.chem()
    Maths = M(roll,name)
    Maths.maths()
    print('------//-----')
    o = overall(roll,name)
    o.marksheet()

    # f = final(roll,name) 
    # f.output()
    n = n-1


