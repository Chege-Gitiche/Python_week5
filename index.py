
#Assignment 1
# Base class
class Profession:
    def __init__(self, name, experience):
        self.name = name
        self._experience = experience  # Encapsulated attribute (protected)
    
    def describe(self):
        return f"{self.name} has {self._experience} years of experience."
    
    def work(self):
        return f"{self.name} is working in a general profession."

# Subclass: Doctor
class Doctor(Profession):
    def __init__(self, name, experience, specialization):
        super().__init__(name, experience)
        self.specialization = specialization

    def work(self):
        return f"Dr. {self.name} is treating patients in {self.specialization}."

# Subclass: Engineer
class Engineer(Profession):
    def __init__(self, name, experience, field):
        super().__init__(name, experience)
        self.field = field

    def work(self):
        return f"{self.name} is solving problems in the field of {self.field}."

# Subclass: Artist
class Artist(Profession):
    def __init__(self, name, experience, medium):
        super().__init__(name, experience)
        self.medium = medium

    def work(self):
        return f"{self.name} is creating art using {self.medium}."


#Assignment 2

# Base class
class Vehicle:
    def move(self):
        return "This vehicle moves in a general way."

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"
