import random
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


class Defend:
    def __init__(self, name, incoming_damage):
      self.name = name
      self.incoming_damage = incoming_damage

    def damage(self):
        random_value = random.randint(0, self.incoming_damage)
        return random_value

class Add_Ability:
    def __init__(self, name, smackdown):
      self.name = name
      self.smackdown = smackdown

    def defend(self):
        random_value = random.randint(0, self.smackdown)
        return random_value


class Take_Hit:
    def __init__(self, name, take_damage):
      self.name = name
      self.take_damage = take_damage

    def damage(self):
        random_value = random.randrange(0,self.take_damage)
        print(random_value)