import random

from elements.player import *
from elements.history import *
from elements.enemies import *
from elements.items import *
from elements.world import *

#Player object
class Player:
    def __init__(self, name, attributes = []):
        #Base player elements

        self.name = name    #Player name
        self.level = 1      #Player start level
        self.exp = 0        #Player start experience
    
        #Define player attributes using the PAECIDF system
        #This defines the attributes of the player via the attributes array of the object
        self.attributes = {
            'Power' : attributes[0],
            'Awareness' : attributes[1],
            'Endurance' : attributes[2],
            'Charm' : attributes[3],
            'Intelligence' : attributes[4],
            'Dexterity' : attributes[4],
            'Fortune' : attributes[5]
        }

        #Define the player skills relating them to the PAECIDF attributes
        self.skills = {
            'Melee':    round((self.attributes['Power'] * 2) + (round(self.attributes['Dexterity']* 4)) / 2),
            'Speech':   round((self.attributes['Charm'] * 2) + (round(self.attributes['Intelligence']* 4)) / 2),
            'Lockpick': round((self.attributes['Awareness'] * 2) + (round(self.attributes['Dexterity']* 4)) / 2),
            'Hacking':  round((self.attributes['Intelligence'] * 2) + (round(self.attributes['Fortune']* 4)) / 2),
            'Medicine': round((self.attributes['Intelligence'] * 2) + (round(self.attributes['Endurance']* 4)) / 2)
        }

        #Define basic info relating to the skills

        self.hp = round(self.attributes['Power'] * 10 + self.attributes['Endurance'] * 2)    #Player initial HP
        self.attack = round(self.attributes['Power'] * 10 + self.skills['Melee'] * 2)   #Player initial Attack Skill
        self.defense = round(self.attributes['Endurance'] * 10 + self.skills['Melee'] * 2)    #Player initial Defense Skill

        #Start checkpoints

        self.cphp = self.hp

        #Player inventory
        self.inventory = []
        self.kit = []

    #Attack an enemy
    def attack_enemy(self, enemy):
        damage = (self.attack * random.randint(1, 2)) - (enemy.defense)    #Damage made to the enemy
        if damage > 0:                          #Check if the damage is enough to hurt the enemy
            enemy.hp -= damage                  #Makes damage
            print(f"You hit the {enemy.name} for {damage} damage.")
        else:
            print("You do no damage.") #When this happens, the player attack skill is not enough to hurt the enemy
        if enemy.hp <= 0:              #When the player kills the enemy, the enemy experience will be sent to the player     
            self.exp += round(enemy.exp)
            print(f"You defeated the {enemy.name}!")
            print(f"You gain {enemy.exp} experience points.")
            loot = enemy.drop_loot()
            if loot:
                self.inventory.append(loot)         #Sends enemy loot to the player inventory
                print(f"You find a {loot.name}.")

    def level_up(self):
        if self.exp >= self.level * 10:
            self.exp -= self.level * 10
            self.level += 1
            self.hp += round((self.attributes['Power'] * 2 + self.attributes['Endurance'] * 2)/ random.randint(2, 4))
            self.attack += round((self.attributes['Power'] * 2 + self.skills['Melee'] * 2) / random.randint(2, 4))
            self.defense += round((self.attributes['Endurance'] * 2 + self.skills['Melee'] * 2) / random.randint(2, 4))
            print(f"Congratulations, you are now level {self.level}!")
    
    def rest(self):
        self.hp = self.cphp
        print('After resting, your HP is recovered')

    def use_item(self, item):
        for item in self.inventory:
            if item.name.lower() == item.name.lower():
                item.use(self)
                self.inventory.remove(item)
                print(f'You have used a {item.name}')
                return
        print(f"You don't have a {item.name} in your inventory")

