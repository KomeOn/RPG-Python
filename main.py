from classes.game import Person, bcolors
from classes.spells import Spell
from classes.inventory import Items
import random

# Natural Magic
fire = Spell("Fire", 25, 520, "natural")
thunder = Spell("Thunder", 20, 580, "natural")
water = Spell("Water", 25, 540, "natural")
wind = Spell("Wind", 25, 560, "natural")
earth = Spell("Earth", 25, 580, "natural")

# Enhanced Magic
blizzard = Spell("Blizzard", 25, 660, "enhanced")
boulder = Spell("Boulder", 20, 640, "enhanced")
iceS = Spell("Ice Spike", 25, 680, "enhanced")
magma = Spell("Magma", 25, 640, "enhanced")
quake = Spell("Earthquake", 20, 640, "enhanced")

# Black Magic
darkT = Spell("Dark Thunder", 20, 880, "black")
meteor = Spell("Meteor", 20, 860, "black")
darkF = Spell("Dark Flames", 25, 900, "black")
darkness = Spell("Darkness", 25, 900, "black")

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

enemyB_spells = [water, earth, blizzard, iceS, meteor, darkness, cure, cura]
enemyM_spells = [water, blizzard, meteor, darkness, cure]

pr1 = Person("Larvoc  ", 3500, 180, 1400, 1100, player_spells, player_items)
pr2 = Person("Preacher", 3700, 160, 1700, 600, player_spells, player_items)
pr3 = Person("Dinker  ", 3600, 260, 2900, 1000, player_spells, player_items)

en1 = Person("Soknic", 71000, 260, 740, 2100, enemyB_spells, [])
en2 = Person("Mikus ", 2300, 200, 680, 220, enemyM_spells, [])
en3 = Person("Sukius", 2300, 200, 680, 220, enemyM_spells, [])

players = [pr1, pr2, pr3]

enemies = [en2, en1, en3]

running = True

enemies_copy = enemies.copy()

print(bcolors.FAIL + bcolors.FAIL + "An Enemy Appeared" + bcolors.ENDC)

while running:
    
    print("NAME                HP                                          MP")
    print("\n")
        
    for player in players:
        player.get_stats()

    print("\n")
    
    for enemy in enemies:
        enemy.get_enemy_stats()    
    
    print("\n")    

    for player in players:
        print("---------------------------------------------------------------")
        player.choose_action()
        print("---------------------------------------------------------------")
        choice = input("Choose action : ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_dmg()
            sel = player.choose_target(enemies)
            enemies[sel].take_dmg(dmg)
            print(player.name.replace(" ","") + " attacks for " + bcolors.FAIL + str(dmg) + bcolors.ENDC, "points of damage to {}. ".format(enemies[sel].name.replace(" ","")) + enemies[sel].name.replace(" ","") + " heatlh points : ", bcolors.OKGREEN, enemies[sel].get_hp(), bcolors.ENDC)
            if enemies[sel].get_hp() == 0:
                print(bcolors.BOLD + bcolors.FAIL + enemies[sel].name + " has been defeated." + bcolors.ENDC)
                del enemies[sel]

        elif index == 1:
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
                print(bcolors.OKBLUE + player.name.replace(" ","") + " heals for", str(mg_dmg), "health points. " + bcolors.ENDC)

            elif spell.typ == 'black':
                sel = player.choose_target(enemies)
                enemies[sel].take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + player.name.replace(" ","") + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage to " + enemies[sel].name.replace(" ","") + bcolors.ENDC)
                if enemies[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + enemies[sel].name + " has been defeated.")
                    del enemies[sel]
            
            elif spell.typ == 'natural':
                sel = player.choose_target(enemies)
                enemies[sel].take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + player.name.replace(" ","") + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage to " + enemies[sel].name.replace(" ","") + bcolors.ENDC)
                if enemies[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + enemies[sel].name + " has been defeated.")
                    del enemies[sel]

            elif spell.typ == 'enhanced':
                sel = player.choose_target(enemies)
                enemies[sel].take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + player.name.replace(" ","") + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage to " + enemies[sel].name.replace(" ","") + bcolors.ENDC)
                if enemies[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + enemies[sel].name + " has been defeated.")
                    del enemies[sel]
                  
        elif index == 2:
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
                sel = player.choose_target(enemies)
                enemies[sel].take_dmg(item.prop)
                print(enemies[sel].name.replace(" ","") + " took " + bcolors.FAIL, item.prop, bcolors.ENDC + " amount of damage.")
                if enemies[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + enemies[sel].name + " has been defeated.")
                    del enemies[sel]

                
            elif item.typ == 'elixer':
                if item.name == "Hi-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        print(" " + bcolors.BOLD + bcolors.HEADER + i.name.replace(" ","") + "is fully healed {hp} and recharged {mp}".format(hp=i.maxhp, mp=i.maxmp) + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print("HP and MP is fully restored")

        elif index == 3:
            defence = player.generate_def()
        
        elif index == 4:
            mana = player.rechargeMP()
            print(bcolors.BOLD + bcolors.HEADER + player.name.replace(" ","") + " recharges for MP. " + "Mana points : {}".format(player.get_mp()))

    team_h = len(players)
    team_v = len(enemies)

    defeat_teamh = 0
    defeat_teamv = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeat_teamv += 1
    
    for player in players:
        if player.get_hp() == 0:
            defeat_teamh += 1

    if defeat_teamh == team_h and defeat_teamv == team_v :
        print(bcolors.FAIL + "Enemies defeated!!!" + bcolors.ENDC)
        print(bcolors.FAIL + "Heroes defeated!!!" + bcolors.ENDC)        
        print(bcolors.WARNING + "But at what cost!!!" + bcolors.ENDC)
        running = False

    elif defeat_teamv == team_v :
        print(bcolors.FAIL + "Enemies defeated!!!" + bcolors.ENDC)
        print(bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
        running = False

    elif defeat_teamh == team_h :
        print(bcolors.FAIL + "Heroes defeated!!!" + bcolors.ENDC)
        print(bcolors.FAIL + "You lose!!" + bcolors.ENDC)
        running = False

    print("\n\n")

    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        len_team = len(players)
        sel = en1.select_target(len_team)
        

        if enemy_choice == 0:
            dmg = enemy.generate_dmg()
            players[sel].take_dmg(dmg)
            print(enemy.name.replace(" ","") + " attacks for", bcolors.FAIL, dmg, bcolors.ENDC, "points of damage to {}. ".format(players[sel].name.replace(" ","")) + players[sel].name.replace(" ","") + " heatlh points : ", bcolors.OKGREEN, players[sel].get_hp(), bcolors.ENDC)

        elif enemy_choice == 1:
            spell, mg_dmg = enemy.choose_magic()
            enemy.reduce_mp(spell.cost)
            players[sel].take_dmg(mg_dmg)

            if spell.typ == 'white':
                enemy.heal(mg_dmg)
                print(bcolors.OKBLUE + enemy.name.replace(" ","") + " heals for", str(mg_dmg), "health points. " + bcolors.ENDC)

            elif spell.typ == 'black':
                players[sel].take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ","") + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage to " + players[sel].name.replace(" ","") + bcolors.ENDC)
                if players[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + players[sel].name + " has been defeated.")
                    del players[sel]
            
            elif spell.typ == 'natural':
                players[sel].take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ","") + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage to " + players[sel].name.replace(" ","") + bcolors.ENDC)
                if players[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + players[sel].name + " has been defeated.")
                    del players[sel]
            
            elif spell.typ == 'enhanced':
                players[sel].take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ","") + " casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage to " + players[sel].name.replace(" ","") + bcolors.ENDC)
                if players[sel].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + players[sel].name + " has been defeated.")
                    del players[sel]
        #elif enemy_choice == 2:


        #print("---------------------------------------------------------------")
    
    
