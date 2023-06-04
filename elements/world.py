import random
from elements.player import *
from elements.history import *
from elements.enemies import *
from elements.items import *
from elements.world import *

class World:
    def __init__(self):
        self.locations = {}
        self.current_location = None

    def add_location(self, location):
        self.locations[location.name] = location

    def move_to_location(self, name):
        location = self.locations.get(name)
        if location:
            self.current_location = location
            print(location.description)
        else:
            print("That location does not exist.")

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def remove_enemies(self, enemy):
        self.enemies.remove(enemy)

    def get_random_enemy(self):
        return random.choice(self.enemies)