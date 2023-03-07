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
        hungry = self.hungry
        tired = self.tired
        happy = self.happy

        if self.hungry:
            print(f"{self.name} has been fed.")
            self.hungry = False
        else:
            print(f"{self.name} is not hungry.")
    def info(self):
        if self.tired:
            print(f"{self.name} has gone to sleep.")
            self.tired = False
        else:
            print(f"{self.name} is not tired.")
    def info(self):
        if self.happy:
            print(f"{self.name} is already playing.")
        else:
            print(f"{self.name} is playing now.")
            self.happy = True



