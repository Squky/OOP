

class Cat():

    def __init__(self,name,age,fur_colour,gender,was_in_Cats_the_musical):
        self.name = name
        self.age = age
        self.fur_colour = fur_colour
        self.gender = gender
        self.cats_musical = was_in_Cats_the_musical

    def meow(self):
        return " ~meooow~ "


    def purr(self):
        return " *pprruurrr"

    def play(self,toy=""):
        if(toy!=""):
            return self.name + " playss with " + toy
        else :
            return self.name + " starts playing around"


    def eat(self,food):
        return food + " isn't my favourite but I guess it'll do.."

    def pet(self):
        return "Yes you are"

    def attri(self):        # Method which creates a dictionary of all the attributes of this class
        attributes ={
            "name" : self.name,
            "age" : self.age,
            "fur_colour" : self.fur_colour,
            "gender" :  self.gender,
            "Was in Cats the musical? " : self.cats_musical


        }

        for i in attributes:        ## ...and returns it in a formatted list style to the user
            print(i,": ",attributes[i])