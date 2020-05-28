#Python 3
import random
from classes.spells import Spell


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
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 5
        self.atkh = atk + 15
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items', 'Defend', 'Heal', 'Recharge']
        self.name = name

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_def(self):
        return random.randrange(0, self.df)

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, points):
        self.hp = self.hp + points
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def rechargeMP(self, points):
        self.mp = self.mp + points
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_hp(self):
        return self.hp
    
    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp = self.mp - cost

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.BOLD + bcolors.OKBLUE + "Actions : " + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ": " + item)
            i =  i + 1
    
    def choose_spells(self):
        i = 1
        print("\n")
        print(bcolors.BOLD + bcolors.FAIL + "Magic : " + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ": %-12s"%(spell.name), "\t\t", "cost : ",spell.cost, "\t\t", "damage : ",spell.dmg)    
            i = i + 1
    
    def choose_items(self):
        i = 1
        print("Inventory")
        for item in self.items:
            print("    " + str(i) + ": ",str(item['item'].name), " : ",str(item['item'].desc)," : x"+str(item['quantity']))
            i =  i + 1

    def get_enemy_stats(self):
        hp_bar = ""
        hpbar_ticks = (self.hp / self.maxhp) * 100 / 2

        while hpbar_ticks > 0:
            hp_bar += "█"
            hpbar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar +=" "

        print("                     __________________________________________________")
        print(bcolors.BOLD + str(self.name) + "   " + "%5s"%str(self.hp) + "/" +  "%5s"%str(self.maxhp) + '|' + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):

        hp_bar = ""
        hpbar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mpbar_ticks = (self.mp / self.maxmp) * 100 / 10

        while hpbar_ticks > 0:
            hp_bar += "█"
            hpbar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar +=" "

        while mpbar_ticks > 0:
            mp_bar += "█"
            mpbar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar +=" "

        print("                    _________________________                   __________")
        print(bcolors.BOLD + str(self.name) + "  " + "%4s"%str(self.hp) + "/" + "%4s"%str(self.maxhp) + '|' + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|" + "         " 
        + "%4s"%str(self.mp) + "/" + str(self.maxmp) + "|"  + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def select_target(self, num):
        start = 0
        last = num
        return random.randrange(start, last)

    def choose_target(self, enemies):
        i = 1
        print("Target :")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ": ",str(enemy.name))
                i =  i + 1
        
        choice = int(input("Choose targer : ")) - 1
        return choice

