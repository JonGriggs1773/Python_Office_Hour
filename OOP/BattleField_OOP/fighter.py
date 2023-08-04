import random
from weapon import Weapon


class Fighter:
    def __init__(self, name, height, build, health=100):
        self.name = name
        self.height = height
        self.build = build
        self.health = health
        self.weapon = None


    def attack(self, enemy):
        print(f"{self.name} attacked {enemy.name} with a {self.weapon.type}")
        hit = random.randint(1, 20)
        print(f"{self.name} rolled a {hit}")
        if hit >= 15:
            print(f"{enemy.name} lost {self.weapon.damage}HP due to a critical hit from {self.name}")
            print(self.weapon.damage)
            enemy.health -= self.weapon.damage
            print(f"{enemy.name}'s Health: {enemy.health}")
        elif hit >= 10:
            damage = self.weapon.damage / 2
            print(f"{enemy.name} lost {damage}HP from a glancing blow")
            enemy.health -= damage
            print(f"{enemy.name}'s Health: {enemy.health}")
        else:
            print(f"{self.name} didn't leave a mark on {enemy.name}")



