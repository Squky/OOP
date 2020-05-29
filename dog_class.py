# Abstract and create the class dog

class Dog():
    name = ""


    def __init__(self,name,age,paws):   ## This works like a constructor class would in java
        self.name = name
        self.age = age
        self.paws = paws


    def bark(self, person = ''):
        return 'woof, woof!' + person

    def fetch(self):

        return ("Imma get that ball")

    def pet(self):
        return "Yes I am"

    def eat(self,food):

        return ("Thats a tasty ", food)
