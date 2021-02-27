import random
from armor import Armor


#Ability Class
#__init__: Parameters: name: String, max_damage:Integer
#attack: No Parameters

#import random


##Instead of remaking our Hero class first, let's start with the classes our Hero class will need to use.

#Our hero will need an ability to be able to save the world. let's start by creating a class named Ability that our hero can use.

#Let's give our Ability class two simple methods, __init__, and attack.

#First, in your project directory, make a file named ability.py to contain all the code for the Ability class

class Ability:
    def __init__(self, name, max_damage):
      self.name = name
      self.max_damage = max_damage

    def attack(self):
        random_value = random.randrange(0,self.max_damage)
        print(random_value)

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class

random.randint(2, 7)



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())





        

 