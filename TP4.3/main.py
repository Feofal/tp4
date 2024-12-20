"""
    Nom: Gabriel Foriel Fusier
    Groupe: 401
    Description: Suite de personnage a la DND, avec sac a dos
"""

from enum import Enum
from random import randint
from dataclasses import dataclass

def dice_roll(num_dice, num_face):
    result = randint(num_dice, num_face * num_dice)
    return result

def choose_dice_roll():
    dice_roll_list = []
    for i in range(4):
        dice_roll_list.append(dice_roll(1,6))
    dice_roll_list.remove(min(dice_roll_list))
    return sum(dice_roll_list)

class Alignment(Enum):
    NONE = 0
    LAWFUL_GOOD = 1
    LAWFUL_NEUTRAL = 2
    LAWFUL_EVIL = 3
    NEUTRAL_GOOD = 4
    TRUE_NEUTRAl = 5
    NEUTRAL_EVIL = 6
    CHAOTIC_GOOD = 7
    CHAOTIC_NEUTRAL = 8
    CHAOTIC_EVIL = 9

class NPC:
    def __init__(self, name, hp, race, species, classes):
        self.strenght = choose_dice_roll()
        self.dexterity = choose_dice_roll()
        self.constitution = choose_dice_roll()
        self.intelligence = choose_dice_roll()
        self.wisdom = choose_dice_roll()
        self.charisma = choose_dice_roll()
        self.armor = dice_roll(1, 12)
        self.name = name
        self.race = race
        self.species = species
        self.hp = hp
        self.classes = classes
        self.alignment = Alignment(dice_roll(1,10) - 1)

    def show_stat(self):
        print(f"Nom: {self.name}\n{self.alignment}\nRace: {self.race}\nEspèce: {self.species}\nClasse: {self.classes}\nPv: {self.hp}\nArmure: {self.armor}\nForce: {self.strenght}\nAgilité: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nSagesse: {self.wisdom}\nCharisme: {self.charisma}\n")

    def is_alive(self):
        if self.hp <= 0:
            print("Mort")
        else:
            print("Pas mort ")
class Kobold(NPC):
    def __init__(self):
        super().__init__("Kabald", dice_roll(1, 20),"Kobold", "Kobold", "Combattant")

    def attack(self, target):
        self.target = target
        self.try_attack = dice_roll(1,20)
        match self.try_attack:
            case 20:
                self.damage = dice_roll(1, 6)
                print(f"L'attaque est reussite, {self.name} a fait {self.damage}.")
            case 1:
                self.damage = 0
                print(f"L'attaque est ratée.")
            case _ if self.try_attack >= 2 and self.try_attack <= 19 and self.try_attack > self.target.armor:
                self.damage = dice_roll(1, 6)
                print(f"L'attaque est reussite, {self.name} a fait {self.damage}.")
            case _ if self.try_attack >= 2 and self.try_attack <= 19 and self.try_attack <= self.target.armor:
                self.damage = 0
                print(f"L'attaque est ratée.")
        return self.damage

    def receive_damage(self, opponent_damage):
        self.opponent_damage = opponent_damage
        self.hp -= self.opponent_damage
        print(f"Il reste {self.hp} pv a {self.name}.")

class Hero(NPC):
    def __init__(self):
        super().__init__("Sir Otho Pouléto", dice_roll(1, 20), "Gallus", "Bright Gallus", "Bard")
        self.bagpack = Bagpack()

    def attack(self, target):
        self.target = target
        self.try_attack = dice_roll(1,20)
        match self.try_attack:
            case 20:
                self.damage = dice_roll(1, 6)
                print(f"L'attaque est reussite, {self.name} a fait {self.damage}.")
            case 1:
                self.damage = 0
                print(f"L'attaque est ratée.")
            case _ if self.try_attack >= 2 and self.try_attack <= 19 and self.try_attack > self.target.armor:
                self.damage = dice_roll(1, 6)
                print(f"L'attaque est reussite, {self.name} a fait {self.damage}.")
            case _ if self.try_attack >= 2 and self.try_attack <= 19 and self.try_attack <= self.target.armor:
                self.damage = 0
                print(f"L'attaque est ratée.")
        return self.damage

    def receive_damage(self, opponent_damage):
        self.opponent_damage = opponent_damage
        self.hp -= self.opponent_damage
        print(f"Il reste {self.hp} pv a {self.name}.")

@dataclass
class Item:
    name: str
    quantity: int

class Bagpack:
    def __init__(self):
        self.item_list = []

    def add_item(self, new_item):
        self.item_in_list = False
        for item in self.item_list:
            if item.name == new_item.name:
                item.quantity += new_item.quantity
                self.item_in_list = True
        if self.item_in_list == False:
            self.item_list.append(new_item)

    def discard_item(self, item_to_take):
        for item in self.item_list:
            if item.name == item_to_take.name:
                self.original_quantity = item.quantity
                item.quantity -= item_to_take.quantity
                if item.quantity == 0:
                    self.item_list.remove(item)
                elif item.quantity < 0:
                    print("Erreur, la quantité a enlever est supérieure a la quantité présente.")
                    item.quantity = self.original_quantity

    def show_bagpack(self):
        print(self.item_list)

h = Hero()
k = Kobold()
h.show_stat()
k.show_stat()
h.receive_damage(k.attack(h))
k.receive_damage(h.attack(k))
h.is_alive()
k.is_alive()
bg = Bagpack()
bg.add_item(Item("Potion", 100))
bg.add_item(Item("Potion", 100))
bg.discard_item(Item("Potion", 50))
bg.show_bagpack()
