#Python 3
import random

class Spell:
    def __init__(self, name, cost, dmg, typ):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.typ = typ

    def generate_mgdmg(self):
        mgl = self.dmg - 5
        mgh = self.dmg + 15
        return random.randrange(mgl, mgh)