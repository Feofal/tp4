"""
    Nom: Gabriel Foriel Fusier
    Groupe:401
    Description: Classe DND
"""
from random import randint

def dice_roll(num_dice, num_face):
    result = randint(num_dice, num_face * num_dice)
    return result
def choose_dice_roll():
    dice_roll_list = []
    for i in range(4):
        dice_roll_list.append(dice_roll(1,6))
    dice_roll_list.remove(min(dice_roll_list))
    return sum(dice_roll_list)
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
    def show_stat(self):
        print(f"Nom: {self.name}\nRace: {self.race}\nEspèce: {self.species}\nClasse: {self.classes}\nPv: {self.hp}\nArmure: {self.armor}\nForce: {self.strenght}\nAgilité: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nSagesse: {self.wisdom}\nCharisme: {self.charisma}\n")
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

h = Hero()
k = Kobold()
h.show_stat()
k.show_stat()
h.receive_damage(k.attack(h))
k.receive_damage(h.attack(k))












