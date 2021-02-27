#class Animal:
    #def __init__(self, name, sleep_duration):
        #self.name = name
        #self.sleep_duration = sleep_duration

    #def sleep(self):
        #print(
            #"{} sleeps for {} hours".format(
                #self.name,
                #self.sleep_duration))

# Note that the class Dog takes in Animal as a parameter!
#class Dog(Animal):
    #def bark(self):
        #print("Woof! Woof!")
#Instantiate a new Dog object and call the sleep and bark methods this way.

#my_dog = Dog("Sophie", 12)
#my_dog.sleep()
#my_dog.bark()
#You should see this output in the terminal.

#Sophie sleeps for 12 hours
#Woof! Woof!



class Animal:

    def __init__(self,name):
        self.name = name
        print("animal initialized")

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping!")

my_animal = Animal("Major")
my_frog = Frog("Kermit")


#_________________________________________________

#my_animal.eat()
#my_frog.jump()
#my_animal.drink()
#my_frog.eat()

#returns below:

#animal initialized
#animal initialized
##Major is eating.
#Kermit is jumping!
#Major is drinking.
#Kermit is eating.




#animal.py
#class Animal:
  #def __init__(self, name):
    #self.name = name

  #def eat(self):
    #print('{} is eating'.format(self.name))

  #def drink(self):
    #print('{} is drinking'.format(self.name))

#class Frog(Animal):
    #def jump(self):
        #print('{} is jumping'.format(self.name))

#returns below:
#animal initialized
#animal initialized