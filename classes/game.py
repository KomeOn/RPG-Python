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
    def __init__(self, hp, mp, atk, df, magic, items):
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
        print("Actions : ")
        for item in self.actions:
            print(" " + str(i) + ": " + item)
            i =  i + 1
    
    def choose_spells(self):
        i = 1
        print("Magic : ")
        for spell in self.magic:
            if 'Dark' in spell.name:
                print(str(i) + ": ",spell.name, "\t", "cost : ",spell.cost, "\t", "damage : ",spell.dmg)
                i = i + 1
                continue
            print(str(i) + ": ",spell.name, "\t\t", "cost : ",spell.cost, "\t", "damage : ",spell.dmg)    
            i = i + 1
    
    def choose_items(self):
        i = 1
        print("Inventory")
        for item in self.items:
            print(" " + str(i) + ": ",item.name, " : ",item.desc," : x5")
            i =  i + 1