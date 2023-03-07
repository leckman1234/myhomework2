class Student:
    def __init__(self,name,species,hungry,tired,happy):
        self.name = name
        self.species = species
        self.hungry = True
        self.tired = True
        self.happy = False
    def info(self):
        name = self.name
        species = self.species
        hungary = self.hungry
        tired = self.tired
        happy = self.happy
    if self.hungry:
        print(f"{self.name} has been fed.")
        self.hungry = False
    else:
        print(f"{self.name}"is not hungary)

