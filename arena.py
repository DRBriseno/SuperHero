from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


#create instance variables named team_one and team_two that
        # will hold our teams.


class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

#Build the create_ability function for your Arena class
#create_ability method
    def create_ability(self):
        name = input("Choose your ability!  ")
        max_damage = int(input("Set Maximum Damage!!!  "))

        return Ability(name, max_damage)

#Build the create_weapon function for your Arena class
#create weapon method
#This method will allow a user to create a weapon.
# return the new weapon object.
        pass
    def create_weapon(self):
 # Prompt the user for the necessary information to create a new weapon object.
        chosen_weapon = input("Choose your weapon! ")
        weapon_damage = int(input("Set Maximum Damage!!!  "))

# return the new weapon object.
        return Weapon(chosen_weapon, weapon_damage)

#Build the create_armor function for your Arena class
#create_armor method
#This method will allow a user to create a piece of armor.

    def create_armor(self):
        #  Prompt the user for the necessary information to create a new armor object.
        armor_name = input("Choose your armor! ")
        armor_health = int(input("Set maximum security!!! "))

#  return the new armor object with values set by user.
        return Armor(armor_name, armor_health)

#Build the create_hero function for your Arena class
#create_hero function

    def create_hero(self):
        hero_name = input("Name your hero! ")
        hero = Hero(hero_name)
        add_item = None

        while add_item != "4":
           add_item = input("[1] Choose hero ability\n[2] Choose hero weapon\n[3] Choose hero armor\n[4] Finished creating hero.\n\nMake your selection: ")
           if add_item == "1":
               #add an ability to the hero
               #HINT: First create the ability, then add it to the hero
               ability_input = self.create_ability()
               hero.add_ability(ability_input)
           elif add_item == "2":
               #add a weapon to the hero
               #HINT: First create the weapon, then add it to the hero
               weapon_input = self.create_weapon()
               hero.add_weapon(weapon_input)
           elif add_item == "3":
               #add an armor to the hero
               #HINT: First create the armor, then add it to the hero
               armor_input = self.create_armor()
               hero.add_armor(armor_input)
        return hero

#Build the build_team_one and build_team_two functions for your Arena class

#TEAM 1
# This method should allow a user to create team one.
    def build_team_one(self):
        #Prompt the user to build team_one
        # Prompt the user for the number of Heroes on team one
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            # call self.create_hero() for every hero that the user wants to add to team one.
            hero = self.create_hero()
            # Add the created hero to team one.
            self.team_one.add_hero(hero)
           

#TEAM 2
# This method should allow a user to create team two.
    def build_team_two(self):
        #Prompt the user to build team_two
        # Prompt the user for the number of Heroes on team two
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            # call self.create_hero() for every hero that the user wants to add to team two.
            hero = self.create_hero()
            # Add the created hero to team two.
            self.team_two.add_hero(hero)

#Build the team_battle function for your Arena class
#This method should battle the teams together.
    def team_battle(self):
        self.team_one.attack(self.team_two)


#Team One statistics
        
    def team_one_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("Survived from " + self.team_one.name + ": " + hero.name)


#Team Two statistics

    def team_two_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("Survived from " + self.team_two.name + ": " + hero.name)


#Build the show_stats function for your Arena class. 
#This method should print out battle statistics

    def show_stats(self):
        print("Statistics for Team One")
        self.team_one_stats()
        print("Statistcis for Team Two")
        self.team_two_stats()


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena(Team("Good Guys"), Team("Bad Guys"))

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Don't you want to play again? Y for YES! N for NO! : ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
