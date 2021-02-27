import random


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()


#Build the remove_hero method for the Team class:
#remove hero
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

#Build the add_hero method for the the Team Class:
#add hero
    def add_hero(self, hero):
        self.heroes.append(hero)

#Build the view_all_heroes function for the Team class:    
#view all heroes
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)
   
   #Build the stats method for your Team class:
   #stats method
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name,kd))

   #Build the revive_heroes method for your Team class:
   #revive method
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = 100
    
#Build the attack method for your Team class:
#attack method

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)
            
# 1) Randomly select a living hero from each team (hint: look up what random.choice does)
# 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)  
        while len(living_heroes) > 0 and len(living_opponents)> 0:
                hero = random.choice(living_heroes)
                opponent = random.choice(living_opponents)

                loser = hero.fight(opponent)

# 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight

        for hero in living_heroes:
                if loser == hero.name:
                    living_heroes.remove(hero)
                    print(f"{hero.name} has been removed")
        
        for opponent in living_opponents:
                 if loser == opponent.name:
                    living_opponents.remove(opponent)
                    print(f"{opponent.name} has been removed")



#pytest -x team_test.py Returned below: ????

#dixiebriseno:superhero_team_dueler [ main {origin/main} ↓·3↑·2 | ✚ 3 ] ➭ pytest -x team_test.py====================================== test session starts ======================================
#platform darwin -- Python 3.7.9, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
#rootdir: /Users/dixiebriseno/Make_Courses/CS1.1/superhero_team_dueler
#collected 0 items                                                                               

#===================================== no tests ran in 0.00s =====================================
#ERROR: file or directory not found: team_test.py

