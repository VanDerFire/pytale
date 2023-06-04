'''
PYTALE: Text adventure game using OOP
'''

from elements.player import *
from elements.history import *
from elements.enemies import *
from elements.items import *
from elements.world import *


player = Player('Example Player', [6, 5, 9, 5, 2, 4])
print(player.attributes)
print(player.skills)
print(player.hp)
print(player.attack)
print(player.defense)


# create some monsters
goblin = Enemy("goblin", 50, 30, 50, 6)
orc = Enemy("orc", 70, 40, 60, 15)
troll = Enemy("troll", 80, 60, 70, 30)

undefeatable = Enemy('Undefeateable', 1000, 10, 400, 10000)

# create some locations
forest = Location("forest", "You are in a dark forest.")
forest.add_enemy(goblin)
forest.add_enemy(undefeatable)
mountain = Location("mountain", "You are on a rocky mountain.")
mountain.add_enemy(orc)
dungeon = Location("dungeon", "You are in a spooky dungeon.")
dungeon.add_enemy(troll)

# create the game world
world = World()
world.add_location(forest)
world.add_location(mountain)
world.add_location(dungeon)

# start the game loop
while True:
    print()
    command = input("What do you want to do? ")
    if command == "quit":
        break
    elif command == "status":
        print(f"Name: {player.name}")
        print(f"Level: {player.level}")
        print(f"HP: {player.hp}")
        print(f"Attack: {player.attack}")
        print(f"Defense: {player.defense}")
        print(f"Experience: {player.exp}/{player.level*10}")
        print("Power Items:")
        for item in player.inventory:
            print(f"- {item.name}: {item.description}")
        print("Healing Kit: ")
    elif command == "rest":
        player.rest()
    elif command =="move":
        location_name = input("Where do you want to go? ")
        try:
            world.move_to_location(location_name)
            enemy = world.current_location.get_random_enemy()
            if enemy:
                print(f"A {enemy.name} appears!")
        except:
            pass
    elif command == "attack":
        enemy = world.current_location.get_random_enemy()
        if enemy:
            player.attack_enemy(enemy)
            if enemy.hp > 0:
                enemy.attack_player(player)
                if player.hp <= 0:
                    print("You have been defeated!")
                    break
                else:
                    print(f"The {enemy.name} attacks you for {enemy.attack} damage.")
        else:
            print("There are no monsters here.")
    elif command == "level up":
        player.level_up()
    elif command == 'use':
        item_name = input("Which item do you want to use? ")
        try:
            player.use_item(item_name)
        except:
            print("That item doesn't exists.")
    else:
        print("I don't understand that command.")

print("Thanks for playing!")
input()