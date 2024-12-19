"""
    Nom: Gabriel Foriel Fusier
    Groupe: 401
    Description: Mix de plusieurs exercices 
"""
from dataclasses import dataclass
from math import pi
from random import randint
class StringFoo:
    def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message.upper())
sf = StringFoo()
sf.set_string("Je suis riche mon petit canard")
sf.print_string()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calcul_area(self):
        self.area = self.length * self.width
    def show_info(self):
        print(f"La longueur du rectangle: {self.length}\nLa largeur du rectangle: {self.width}\nL'aire du rectangle est de: {self.area}")
r = Rectangle(10,20)
r.calcul_area()
r.show_info()

class Circle:
    def __init__(self, ray):
        self.ray = ray
    def calcul_circumference(self):
        self.circumference = 2 * pi * self.ray
    def calcul_area(self):
        self.area = pi * self.ray ** 2
    def show_info(self):
        print(f"Le rayon du cercle: {self.ray}\nLa circonference du cercle: {self.circumference}\nL'aire du cercle est de: {self.area}")
c = Circle(10)
c.calcul_circumference()
c.calcul_area()
c.show_info()
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = randint(1,6)
        self.attack = randint(1,6)
        self.defense = randint(1,6)
        self.alive = True
    def do_attack(self):
        self.try_attack = randint(1,6) + self.attack
        return self.try_attack
    def take_damage(self,damage):
        self.damage = damage
        self.hp -= self.damage - self.defense
        if self.hp <= 0:
            self.alive = False
    def is_alive(self):
        return(self.alive)

h = Hero("Schnoz")
h.take_damage(h.do_attack())
print(h.is_alive())

@dataclass
class Attributes:
    strenght: int = randint(1,20)
    dexterity: int = randint(1,20)
    constitution: int = randint(1,20)
    intelligence: int = randint(1,20)
    wisdom: int = randint(1,20)
    charisma: int = randint(1,20)

class Hero2:
    def __init__(self, name):
        self.name = name
        self.hp = randint(1,6)
        self.attack = randint(1,6)
        self.defense = randint(1,6)
        self.stat = Attributes()
        self.alive = True
    def do_attack(self):
        self.try_attack = randint(1,6) + self.attack
        return self.try_attack
    def take_damage(self,damage):
        self.damage = damage
        self.hp -= self.damage - self.defense
        if self.hp <= 0:
            self.alive = False
    def is_alive(self):
        return(self.alive)
h2 = Hero2("Schnoz2 le rejet")
h2.take_damage(h2.do_attack())
print(h2.is_alive())
