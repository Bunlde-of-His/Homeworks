import logging

class LogCreation:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        logging.info(f"Exemplar of the Class is created: {cls.__name__}")
        return instance

class Human(LogCreation):
    CURRENT_YEAR = 2023
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    
    def __str__(self):
        return f"Human(name={self.name}, date_of_birth={self.date_of_birth})"
    
    def to_str(self):
        return f"Name: {self.name}, Date of Birth: {self.date_of_birth}"
    
    def get_age(self):
        age =  self.CURRENT_YEAR - self.date_of_birth
        return age

class Planet(LogCreation):
    def __init__(self, name):
        self.name = name
        self.humans = []
    
    def __str__(self):
        return f"Planet(name={self.name})"
    
    def to_str(self):
        return f"Planet: {self.name}"
    
    def add_human(self, humans):
        self.humans.extend(humans)
    
    def get_count(self):
        return len(self.humans)


logging.basicConfig(level=logging.INFO)

humans = [
    Human("John", 1985),
    Human("Jane", 1990),
    Human("Jack", 1978),
    Human("Jill", 1996),
]

planet = Planet("Earth")
planet.add_human(humans)

print(planet.to_str())
print(f"Humans on the planet: {planet.get_count()}")

for human in humans:
    print(f"Age: {human.get_age()} years")
    print(human) 



