from elements.player import *
from elements.history import *
from elements.enemies import *
from elements.items import *
from elements.world import *

class Item:
    def __init__(self, name, description, category, value):
        self.name = name
        self.description = description
        self.category = category
        self.value = value

class healingItem(Item):
    def __init__(self, name, description, category, value, healingPower):
        super().__init__(name, description, category, value)
        self.healingPower = healingPower

    def use(self, player):
        player.health += self.healingPower

#Create items
energyDrink = healingItem('Energy Drink', 'Restores 20 hp', 'Healing', 20, 20)