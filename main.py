from classes.game import Person, bcolors
from classes.spells import Spell
from classes.inventory import Items

# Natural Magic
fire = Spell("Fire", 25, 120, "natural")
thunder = Spell("Thunder", 20, 180, "natural")
water = Spell("Water", 25, 140, "natural")
wind = Spell("Wind", 25, 160, "natural")
earth = Spell("Earth", 25, 180, "natural")

# Enhanced Magic
blizzard = Spell("Blizzard", 25, 260, "enhanced")
boulder = Spell("Boulder", 20, 240, "enhanced")
iceS = Spell("Ice Spike", 25, 280, "enhanced")
magma = Spell("Magma", 25, 240, "enhanced")
quake = Spell("Earthquake", 20, 240, "enhanced")

# Black Magic
darkT = Spell("Dark Thunder", 20, 280, "black")
meteor = Spell("Meteor", 20, 260, "black")
darkF = Spell("Dark Flames", 25, 300, "black")
darkness = Spell("Darkness", 25, 300, "black")

# White Magic
cure = Spell("Cure", 25, 800, "white")
cura = Spell("Cura", 30, 1000, "white")


# Items in Inventory
shealP = Items("Small healing potion", "potion", "Heals for 100", 700)
mhealP = Items("Medium healing potion", "potion", "Heals for 150", 850)
hhealP = Items("Hi-healing potion", "potion", "Heals for 200", 1000)
xhealP = Items("Xtreme healing potion", "potion", "Heals for 600", 600)

elixer = Items("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Items("Hi-Elixer", "elixer", "Fully restores HP/MP of entire party", 9999)

bomb = Items("Bomb", "handy", "Deals damage of 500 to one character", 500)

player_spells = [fire, thunder, magma, quake, darkT, darkF, cure, cura]
player_items = [
                {'item': shealP, 'quantity': 15}, 
                {'item': hhealP, 'quantity': 12},
                {'item': xhealP, 'quantity': 6},
                {'item': elixer, 'quantity': 12},
                {'item': hielixer, 'quantity': 10},
                {'item': bomb, 'quantity': 10},
                ]

pr1 = Person("Larvoc  ", 3500, 180, 1400, 1100, player_spells, player_items)
pr2 = Person("Preacher", 3700, 160, 1700, 600, player_spells, player_items)
pr3 = Person("Dinker  ", 3600, 260, 2900, 1000, player_spells, player_items)

en1 = Person("Sokinc", 71000, 260, 500, 2100, [], [])

players = [pr1, pr2, pr3]

running = True


print(bcolors.FAIL + bcolors.FAIL + "An Enemy Appeared" + bcolors.ENDC)

while running:
    
    print("NAME                HP                                          MP")
    print("\n")
        
    for player in players:
        player.get_stats()

    print("\n")
    en1.get_enemy_stats()    
    
    print("\n")    

    for player in players:
        print("---------------------------------------------------------------")
        player.choose_action()
        print("---------------------------------------------------------------")
        choice = input("Choose action : ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_dmg()
            en1.take_dmg(dmg)
            print(player.name + " attacks for ", bcolors.FAIL, dmg, bcolors.ENDC, "points of damage to {}. ".format(en1.name) + en1.name + " heatlh points : ", bcolors.OKGREEN, en1.get_hp(), bcolors.ENDC)
            
        if index == 1:
            player.choose_spells()
            mg_choice = int(input("Choose magic : ")) - 1

            if mg_choice == -1:
                continue

            spell = player.magic[mg_choice]
            mg_dmg = spell.generate_mgdmg()

            current_mp = player.get_mp()

            if current_mp < spell.cost:
                print(bcolors.BOLD + bcolors.FAIL + "Insufficient MP" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.typ == 'white':
                player.heal(mg_dmg)
                print(bcolors.OKBLUE + player.name + " heals for", str(mg_dmg), "health points. " + bcolors.ENDC)
            elif spell.typ == 'black':
                en1.take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + player.name + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage" + bcolors.ENDC)
            
        if index == 2:
            player.choose_items()
            item_choice = int(input("Choose Item : ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]['item']
            
            if player_items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + str(item.name) +  " is empty. " + bcolors.ENDC)
                continue

            player_items[item_choice]['quantity'] -= 1
            

            if item.typ == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + str(item.name) + " heals for ",item.prop, " HP" + bcolors.ENDC)
                
            elif item.typ == 'handy':
                en1.take_dmg(item.prop)
                print(en1.name + " took " + bcolors.FAIL, item.prop, bcolors.ENDC + " amount of damage.")
                
            elif item.typ == 'elixer':
                if item.name == "Hi-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        print(" " + bcolors.BOLD + bcolors.HEADER + i.name + "is fully healed {hp} and recharged {mp}".format(hp=i.maxhp, mp=i.maxmp) + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print("HP and MP is fully restored")
                
                
    enemy = 1
    dmg = en1.generate_dmg()
    len_team = len(players)
    sel = en1.select_target(len_team)
    players[sel].take_dmg(dmg)
    print(en1.name + " attacks for", bcolors.FAIL, dmg, bcolors.ENDC, "points of damage to {}. ".format(players[sel].name) + players[sel].name + " heatlh points : ", bcolors.OKGREEN, players[sel].get_hp(), bcolors.ENDC)

    print("---------------------------------------------------------------")
    
    if en1.get_hp() == 0 and pr1.get_hp() == 0 :
        print(bcolors.FAIL + "Enemy defeated!!!" + bcolors.ENDC)
        print(bcolors.FAIL + "Player defeated!!!" + bcolors.ENDC)        
        print(bcolors.WARNING + "But at what cost!!!" + bcolors.ENDC)
        running = False

    elif en1.get_hp() == 0:
        print(bcolors.FAIL + "Enemy defeated!!!" + bcolors.ENDC)
        print(bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
        running = False

    elif pr1.get_hp() == 0:
        print(bcolors.FAIL + "Player defeated!!!" + bcolors.ENDC)
        print(bcolors.FAIL + "You lose!!" + bcolors.ENDC)
        running = False
