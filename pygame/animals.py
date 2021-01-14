#animals.py
#a look mat object orinated programming class Animal
class Animal ():
    #constructor
     def __init__(self):
         self.legs = 0;
         self.hairy = False
     def talk(self):
         return "HEllo"
     def eat(self,food):
         if food == "meat":
             return "yummm meat"

dog = Animal()
print(type(dog))
print(dog.legs)
print(dog.eat("233333"))




