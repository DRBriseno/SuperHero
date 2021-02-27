import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
      self.abilities = list()
      self.armors = list() 
      self.name = name
      self.starting_health = starting_health
      self.current_health = starting_health
      self.deaths = 0
      self.kills = 0


# we know the name of our hero, so we assign it here
      #self.name = name
    # similarly, our starting health is passed in, just like name
      #self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
      #self.current_health = starting_health

    # fight method
    def fight(self, opponent):
       self.opponent = opponent
       return("Fight!")

    #add_ability
    def add_ability(self, ability):
      self.abilities.append(ability)

    #add_weapon
    def add_weapon(self, weapon):
      self.abilities.append(weapon)
      print(f"{weapon.name} is armed with {weapon.name} and has it in possesion! ")
    
    #add_armor
    def add_armor(self, armor):
        self.armors.append(armor)
    
    #def_defend
    def defend(self, damage_amt):
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
        return damage_amt - total_armor
    
    #def_attack
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    #def_take_damage
    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        print(f"{self.name} took {damage} damage and is now at {self.current_health}.")
    
    #def_is_alive
    def is_alive(self):  
        if self.current_health <= 0:
            return False
        else:
            return True

 #Create this method that will act as a setter for self.kills.
 #Add the add_kill method to the Hero class:  
    #def_add_kill
    def add_kill(self, num_kills):
        self.kills += num_kills

#Create this method that will act as a setter for self.deaths.
#Add the add_death method to the Hero class: 
    #def_add_death
    def add_death(self, num_deaths):
        self.deaths += num_deaths

 #update fight to reflect what's happening during the battle. 
 #Update the fight method in the Hero class to the following:s  
    #def_add_fight
    def fight(self, opponent):  
        while self.is_alive() is True and opponent.is_alive() is True:
            opponent.take_damage(self.attack())
            if opponent.is_alive() is True:
                self.take_damage(opponent.attack())

            if self.is_alive() is False:
                opponent.add_kill(1)
                self.add_death(1)
                print(f"{self.name} has lost this battle!!")
                return self.name

            if opponent.is_alive() is False:
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{opponent.name} has lost this battle!!")
                return opponent.name


#Instance properties:
          #abilities: List
          #armors: List
          #name: String
          #starting_health: Integer
          #current_health: Integer


#if __name__ == "__main__":           
    # If you run this file from the terminal
    # this block is executed.
        #ability = Ability("Great Debugging", 50)
        #hero = Hero("Grace Hopper", 200)
        #hero.add_abilities(ability)
        #print(hero.ability)

#returned below:

#Traceback (most recent call last):      <<<<<<<why!!!???? I can't figure it out :(
  #File "hero.py", line 102, in <module>
    #hero.add_abilities(ability)
#AttributeError: 'Hero' object has no attribute 'add_abilities'   <<<<<<<come back when you have time

#__________________________________________________

#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    #ability = Ability("Great Debugging", 50)
    #hero = Hero("Grace Hopper", 200)
    #hero.add_ability(ability)
    #print(hero.abilities)

#returned below:

#[<ability.Ability object at 0x7fc608b78790>]



#_______________________________________________________

#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    #ability = Ability("Great Debugging", 50)
    #another_ability = Ability("Smarty Pants", 90)
    #hero = Hero("Grace Hopper", 200)
    #hero.add_ability(ability)
    #hero.add_ability(another_ability)
    #print(hero.attack())

#returned below: 

#30         <<<<<<<<< did return this!!!!!!
#Traceback (most recent call last):
  #File "hero.py", line 123, in <module>    <<<<<<worked on this forever and failed to figure it out
    #print(hero.attack())
  #File "hero.py", line 51, in attack
    #total_damage += ability.attack()
#TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'   <<<<<<come back to this when you have time

#____________________________________________________________

#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    #hero = Hero("Grace Hopper", 200)
    #shield = Armor("Shield", 50)
    #hero.add_armor(shield)
    #hero.take_damage(50)
    #print(hero.current_health)

#returned below:

#Grace Hopper took 50 damage and is now at 192.
#192



#__________________________________________________________

#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    #hero = Hero("Grace Hopper", 200)
    #hero.take_damage(150)
    #print(hero.is_alive())
    #hero.take_damage(15000)
    #print(hero.is_alive())

#returned below:

#Grace Hopper took 150 damage and is now at 50.
#True
#Grace Hopper took 15000 damage and is now at -14950.
#False

#__________________________________________________________

#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    #hero1 = Hero("Wonder Woman")
    #hero2 = Hero("Dumbledore")
    #ability1 = Ability("Super Speed", 300)
    #ability2 = Ability("Super Eyes", 130)
    #ability3 = Ability("Wizard Wand", 80)
    #ability4 = Ability("Wizard Beard", 20)
    #hero1.add_ability(ability1)
    #hero1.add_ability(ability2)
    #hero2.add_ability(ability3)
    #hero2.add_ability(ability4)
    #hero1.fight(hero2)


#returned below:

#40  <<<<< did return this!!!
#Traceback (most recent call last):          <<<<<worked on this forever and failed to figure it out
  #File "hero.py", line 161, in <module>
    #hero1.fight(hero2)
  #File "hero.py", line 72, in fight
    #opponent.take_damage(self.attack())
  #File "hero.py", line 51, in attack
    #total_damage += ability.attack()
#TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'  <<<<check back on this

#____________________________________________


#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
      #hero = Hero("Wonder Woman")
      #weapon = Weapon("Lasso of Truth", 90)
      #hero.add_weapon(weapon)
      #print(hero.attack())


#returned below:

#Lasso of Truth is armed with Lasso of Truth and has it in possesion! 
#58


