import random
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack","Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]
    
    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]


    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
    
    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["Item"].name, ":", item["Item"].description, "(x" + str(item["Quantity"]) + ")")
            i+=1

    def progress_bar(self, props):
        hp_percentage = 25 * (self.hp / self.maxhp)
        mp_percentage = 10 * (self.mp / self.maxmp)
        hp_filled = int(hp_percentage)*"█"
        mp_filled = int(mp_percentage)*"█"
        hp_spaces = (25-int(hp_percentage))*" "
        mp_spaces = (10-int(mp_percentage))*" "

        hp_bar = hp_filled+hp_spaces
        mp_bar = mp_filled+mp_spaces

        if props == "hp":
            return hp_bar
        elif props == "mp":
            return mp_bar
        else:
            return 0

        
    def get_stats(self):
        print("                         _________________________          __________")
        print(bcolors.BOLD + self.name +
         str(self.hp) + "/" + str(self.maxhp) + "   |" + bcolors.OKGREEN + self.progress_bar("hp") + bcolors.ENDC + 
        "|  " + str(self.mp) + "/" + str(self.maxmp) + " |" + bcolors.OKBLUE + self.progress_bar("mp") + bcolors.ENDC + "|")

    