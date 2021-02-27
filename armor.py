import random
#Armor Class
#__init__: Parameters: name: String, max_block: Integer
#block: Parameters: None

class Armor:
    def __init__(self, name, max_block):
      self.name = name
      self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value

random.randint(2, 7)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())


        #: Create instance variables for the values passed in.
        #pass


#Hero Class
#------__init__: Parameters: name:String, starting_health:Int (default value: 100)///// 
#------add_ability: Parameters: ability:Ability Object////
#-----//////attack: No Parameters//////
#-----defend: incoming_damage: Integer/////
#-----take_damage: Parameters: damage//////
#-----//////is_alive: No Parameters////////
#-----fight: Parameters: opponent: Hero Class/////
#------




    

    


