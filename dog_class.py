# Abstract and create the class dog

class Dog():
    name = ""


    def __init__(self,name):   ## This works like a constructor class would in java
        self.name = name

    def bark(self, person = ''):
        return 'woof, woof!' + person

    def fetch(self):

        return ("Imma get that ball")

    def eat(self,food):

        return ("Thats a tasty ", food)
