from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic 
fire = Spell("Fire", 10, 160, "black")
lightning = Spell("Lightning", 5, 90, "black")
blizzard = Spell("Blizzard", 10, 160, "black")
meteor = Spell("Meteor", 20, 350, "black")
quake = Spell("Quake", 7, 110, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


#Create some Items
#Healing items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100", 100)
superpotion = Item("Super Potion", "potion", "Heals 500", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party memer", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

#Damage items
grenade = Item("Grenade", "attack", "Deals 500 DMG", 500)

#List of spells/items held by the player
player_spells = [fire, lightning, blizzard, meteor, quake, cura, cura]
player_items = [{"Item": potion, "Quantity": 15},
                {"Item": hipotion, "Quantity": 5},
                {"Item": superpotion, "Quantity": 5},
                {"Item": elixer, "Quantity": 1},
                {"Item": hielixer, "Quantity": 1},
                {"Item": grenade, "Quantity": 5}]

# Instatiate peoples
player1 = Person("Marchwarden  :", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Player 2     :", 952, 65, 60, 34, player_spells, player_items)
player3 = Person("Player 3     :", 460, 65, 60, 34, player_spells, player_items)
enemy = Person("hoe1", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("==========================================")
    print("\n\n")
    print("NAME                     HP                                 MP")
    print("                         _________________________          __________")
    for player in players:
        player.get_stats()
    print("\n")
    
    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            #returns back to previous choice option
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for" + str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals ", str(magic_dmg), "points of damage." +bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            #returns back to previous choice option
            if item_choice == -1:
                continue

            item = player.items[item_choice]["Item"]
            if player.items[item_choice]["Quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue
            player.items[item_choice]["Quantity"] -= 1
            

            #item type determines what properties to use.
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP", bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " heals for max HP/MP", bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.OKBLUE + "\n" + item.name + "deals ", str(item.prop), "points of damage." +bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("------------------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif players[0].get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False

    