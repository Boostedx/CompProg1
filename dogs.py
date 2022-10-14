class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll (self):
        print(self.name.title() + " rolled over!")
    def bark(self, times):
        print(self.name, 'says woof', times, 'times')
#2
#- The user defined-attributes/parameters are self, name, breed and age.
#3
#- The user-defined methods or actions are sit, roll, and bark.
#5
#- it takes the class Dog and imports it into the script so that the methods set on the dogs.py can be called onto
#the subs_dogs.py script.
#6
#- The values assigned for the parameters would be changed.
#7
#- Line 8 prints the name of dog1 and its attributed name and makes the first letter of the string capitalized.
#- Line 9 prints the indexed value from the format defined in line 10
#- Line 10 contains the format that is called in line 9, it containes the variable dog1 and its called attributes which is
#its breed and its age.
#8
#-Milo is now sitting.
#Milo rolled over!
#Milo says woof 10 times
