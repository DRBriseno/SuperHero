# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    def bark(self):
        print("Woof!"

    # Methods are defined as their own named functions inside the class
    # Remember to put the "self" parameter every time we make a class method!

# instantiation call that creates a Dog object:
my_dog = Dog("Rex", "SuperDog")
#Adding the "breed" property on the fly
# will print "SuperDog"
# Remember python implicitly passes in "self",
# so we don't need to pass it in when we call the function!
my_dog.bark()
