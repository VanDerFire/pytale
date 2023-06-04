import random
from elements.player import *
from elements.history import *
from elements.enemies import *
from elements.items import *
from elements.world import *

class Enemy:
    def __init__(self, name, hp, attack, defense, exp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp = exp

    def drop_loot(self):
        loot_table = [
            #Item("potion", "restores 20 HP", "consumable", 20),
            #Item("sword", "increases attack by 5", "weapon", 5),
            #Item("shield", "increases defense by 3", "armor", 3),
            energyDrink
        ]
        if random.random() < 0.5:
            return random.choice(loot_table)
        else:
            return None
        
    def attack_player(self, player):
         damage = (self.attack * random.randint(1, 2))
         player.hp -= damage

         print(f'the {self.name} attacks you for {damage}')