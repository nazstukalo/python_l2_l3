# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter1 if fighter1.name != first_attacker else fighter2
    while attacker.health > 0 and defender.health > 0:
        defender.health = defender.health - attacker.damage_per_attack
        attacker, defender = defender, attacker
    return fighter1.name if fighter1.health > 0 else fighter2.name


declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")
