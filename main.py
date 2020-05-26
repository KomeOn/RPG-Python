from classes.game import Person, bcolors
from classes.spells import Spell
from classes.inventory import Items

# Natural Magic
fire = Spell("Fire", 15, 120, "natural")
thunder = Spell("Thunder", 20, 180, "natural")
water = Spell("Water", 15, 140, "natural")
wind = Spell("Wind", 15, 160, "natural")
earth = Spell("Earth", 25, 180, "natural")

# Enhanced Magic
blizzard = Spell("Blizzard", 25, 160, "enhanced")
boulder = Spell("Boulder", 20, 140, "enhanced")
iceS = Spell("Ice Spike", 25, 180, "enhanced")
magma = Spell("Magma", 25, 140, "enhanced")
quake = Spell("Earthquake", 20, 140, "enhanced")

# Black Magic
darkT = Spell("Dark Thunder", 20, 180, "black")
meteor = Spell("Meteor", 20, 160, "black")
darkF = Spell("Dark Flames", 25, 200, "black")
darkness = Spell("Darkness", 25, 200, "black")

# White Magic
cure = Spell("Cure", 15, 120, "white")
cura = Spell("Cura", 20, 200, "white")


# Items in Inventory
shealP = Items("Small healing potion", "potion", "Heals for 100", 100)
mhealP = Items("Medium healing potion", "potion", "Heals for 150", 150)
hhealP = Items("Hi-healing potion", "potion", "Heals for 200", 200)
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
                {'item': bomb, 'quantity': 10},
                ]

pr1 = Person("Larvoc  :", 500, 180, 1400, 1100, player_spells, player_items)
pr2 = Person("Preacher:", 700, 160, 1700, 600, player_spells, player_items)
pr3 = Person("Dinker  :", 600, 260, 2900, 1000, player_spells, player_items)

en1 = Person("Sokinc", 7100, 260, 1100, 2100, [], [])

players = [pr1, pr2, pr3]

running = True


print(bcolors.FAIL + bcolors.FAIL + "An Enemy Appeared" + bcolors.ENDC)

while running:
    
    print("NAME               HP                                         MP")
    print("                   _________________________                  __________")

    for player in players:
        player.get_stats()
        
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
            print("Player 1 attacks for", bcolors.FAIL, dmg, bcolors.ENDC, "points of damage to enemy." + " Enemy heatlh points : ", bcolors.OKGREEN, en1.get_hp(), bcolors.ENDC)
            
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
                print(bcolors.OKBLUE + "Player heals for", str(mg_dmg), "health points." + bcolors.ENDC)
            elif spell.typ == 'black':
                en1.take_dmg(mg_dmg)
                print(bcolors.OKBLUE + "\n" + "Player casted " + spell.name + " spell that deals", str(mg_dmg), "points of damage" + bcolors.ENDC)
            
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
                print("Enemy took " + bcolors.FAIL, item.prop, bcolors.ENDC + " amount of damage.")
                
            elif item.typ == 'elixer':
                print("max : ",player.maxhp)
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("HP and MP is fully restored")
                
                
    enemy = 1
    dmg = en1.generate_dmg()
    pr1.take_dmg(dmg)  
    print("Enemy attacks for", bcolors.FAIL, dmg, bcolors.ENDC, "points of damage to enemy." + " Player 1 heatlh points : ", bcolors.OKGREEN, pr1.get_hp(), bcolors.ENDC)

    print("---------------------------------------------------------------")
    
    #print("Enemy HP : ", bcolors.FAIL + str(en1.get_hp()) + " / " + str(en1.get_maxhp()) + bcolors.ENDC)

    #print("Player HP : ", bcolors.OKGREEN + str(pr1.get_hp()) + " / " + str(pr1.get_maxhp()) + bcolors.ENDC)
    #print("Player MP : ", bcolors.OKBLUE + str(pr1.get_mp()) + " / " + str(pr1.get_maxmp()) + bcolors.ENDC)

    
    if en1.get_hp() == 0 and pr1.get_hp() == 0 :
        print(bcolors.FAIL + "Enemy defeated!!!" + bcolors.ENDC)
        print(bcolors.FAIL + "Player defeated!!!" + bcolors.ENDC)        
        print(bcolors.WARNING + "But at what cost!!!" + bcolors.ENDC)
    elif en1.get_hp() == 0:
        print(bcolors.FAIL + "Enemy defeated!!!" + bcolors.ENDC)
        print(bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
    elif pr1.get_hp() == 0:
        print(bcolors.FAIL + "Player defeated!!!" + bcolors.ENDC)
        print(bcolors.FAIL + "You lose!!" + bcolors.ENDC)
        running = False
