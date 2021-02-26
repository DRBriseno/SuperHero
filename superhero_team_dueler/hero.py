class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):


# we know the name of our hero, so we assign it here
      self.name = name
    # similarly, our starting health is passed in, just like name
      self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
      self.current_health = starting_health

    def fight(self, opponent):
       self.opponent = opponent
       return("Fight!")

####

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
     hero_2 = Hero("Wonder Woman", 200)
     print(hero_2.name)
     print(hero_2.current_health) 

#### 

####


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
     hero_1 = Hero("Dumbledore", 200)
     print(hero_1.name)
     print(hero_1.current_health)  

####


import random

opponents = [
    "Wonder Woman", "Dumbledore"]
#print(f"All names:{opponents}/n")
idx = random.randint(0,len(opponents)-1)
print(f"{opponents[idx]} won! ")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero_1 = Hero("Wonder Woman")
    hero_2 = Hero("Dumbledore")
    hero_1.fight(hero_2)

#Ability Class
#__init__: Parameters: name: String, max_damage:Integer
#attack: No Parameters

#import random

class Ability:
    
    def __init__(self, name, max_damage):
      self.name = name
      self.max_damage = max_damage

    def attack(self):
      random_value = random.randrange(0,self.max_damage)
      print(random_value)

 #Armor Class
#__init__: Parameters: name: String, max_block: Integer
#block: Parameters: None

    import random

class Armor:
    def __init__(self, name, max_block):
      self.name = name
      self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value

#Assault Class ... Just Because I Want To
#__init__: Parameters: name: String, max_block: Integer
#block: Parameters: None

class Assault:
    def __init__(self, name, max_strike):
      self.name = name
      self.max_strike = max_strike

    def strike(self):
        random_value = random.randint(0, self.max_strike)
        return random_value

#Hero Class
#__init__: Parameters: name:String, starting_health:Int (default value: 100)
#add_ability: Parameters: ability:Ability Object
#attack: No Parameters
#defend: incoming_damage: Integer
#take_damage: Parameters: damage
#is_alive: No Parameters
#fight: Parameters: opponent: Hero Class

    



