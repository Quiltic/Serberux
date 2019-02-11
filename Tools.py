"""
Tools
Easy show
    shows the caricters and text: max of 10 lines
Save
Load
Make new spells
    required: name, discription,  
Make new events:
    required:

"""
import pickle, os, random

def save(obj, name ):
    try:
        os.remove(name)
        with open(name, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    except:
        with open(name, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

#Items
"""
'Necronomicon'
"""
def NewItems():
    #typesMOD = {'C':[[0,4],[-3,1]],'R':[[1,6],[-5,0]],'E':[[3,8],[-7,-2]],'L':[[5,9],[-8,-4]]}
    
    stuff = {'Royal Sword': ['an ornate steel sword', 'E', 'Mainhand', 8, ['NA'], ['NA'],'Royal Sword'],
    'Wood' :  ['sturdy wood', 'C', 'Crafting'],
    'Steel Sword' :  ['a steel sword', 'R', 'Mainhand', 7, ['NA'], ['NA'], 'Steel Sword'],
    'Whip' :  ['a lenght of stiffened leather', 'E', 'Mainhand', 7, ['Bleed','NA'], ['NA'], 'Whip'],
    'Blunderbuss' :  ['a wide nozzled pistol', 'L', 'Sidehand', {'Resistance': 8,'HpBoost':0,'Damage':6, 'Dodge':-3, 'Strainmax':0}, ['Gunshot'], ['NA'],'Blunderbuss'],
    'Rope' :  ['simple ivy rope', 'C', 'Crafting'],
    'Shield' :  ['a wooden shield', 'C', 'Sidehand', {'Resistance': 3,'HpBoost':1,'Damage':0, 'Dodge':0, 'Strainmax':0},[], ['NA'],'Shield'],
    'Firewand' :  ['a simple wooden stick embued with fire', 'R', 'Mainhand', 3, ['Fire', 'NA'], ['NA'],'Firewand'],
    'Steel Shield' :  ['a wooden shield reinforced with steel', 'R', 'Sidehand', {'Resistance': 6,'HpBoost':2,'Damage':0, 'Dodge':0, 'Strainmax':0},[], ['NA'],'Steel Shield'],
    'Icewand' :  ['a simple wooden stick embued with frost', 'R', 'Mainhand', 3, ['Weak', 'NA'], ['NA'],'Icewand'],
    'Silver ore' :  ['rock with silver embeded in', 'C', 'Crafting'],
    'Royal Shield' :  ['an ornate steel shield', 'E', 'Sidehand', {'Resistance': 8,'HpBoost':3,'Damage':0, 'Dodge':0, 'Strainmax':0},[], ['NA'],'Royal Shield'],
    'Ore' :  ['rocks of various colors', 'C', 'Crafting'],
    'Sword' :  ['a simple iron sword', 'R', 'Mainhand', 6, ['NA'], ['NA'],'Sword'],
    'Picaxe' :  ['a simple wooden pickaxe', 'R', 'Mainhand', 6, ['NA'], ['NA'],'Picaxe'],
    'Bronze Key': ['a bronze key, wonder where it fits..', 'C', 'Crafting'],
    'Silver Key': ['a silver key, wonder where it fits..', 'R', 'Crafting'],
    'Gold Key': ['a gold key, wonder where it fits..', 'E', 'Crafting'],
    'Fire Orb' :  ['an orb resonating with heat', 'E', 'Sidehand', {'Resistance': -2,'HpBoost':4,'Damage':0, 'Dodge':1, 'Strainmax':6},['Firebolt'], ['NA'],'Orb'],
    'Ice Orb' :  ['an orb resonating with frost', 'E', 'Sidehand', {'Resistance': -2,'HpBoost':4,'Damage':0, 'Dodge':1, 'Strainmax':6},['Icebolt'], ['NA'],'Orb'],
    'Magic Orb' :  ['an orb resonating with power', 'E', 'Sidehand', {'Resistance': -2,'HpBoost':4,'Damage':0, 'Dodge':1, 'Strainmax':6},['Magicbolt'], ['NA'],'Orb'],
    'Water Flask' :  ['a water flask', 'R', 'Sidehand', {'Resistance': 2,'HpBoost':4,'Damage':0, 'Dodge':0, 'Strainmax':0},['Drink'], ['NA'],'Flask'],
    'Dagger' :  ['an iron dagger', 'R', 'Sidehand', {'Resistance': -2,'HpBoost':2,'Damage':2, 'Dodge':2, 'Strainmax':-1},['Backstab'], ['NA'],'Dagger'],
    'Silver dagger' :  ['a silver dagger', 'E', 'Sidehand', {'Resistance': -2,'HpBoost':2,'Damage':2, 'Dodge':4, 'Strainmax':0},['Backstab'], ['NA'],'Dagger'],
    'Mace' :  ['a heavy mace', 'R', 'Mainhand', 4, ['Stun','NA'], ['NA'], 'Mace'],
    'Axe' :  ['a normal axe', 'R', 'Mainhand', 4, ['Bleed','NA'], ['NA'], 'Hachet'],
    'Magicwand' :  ['a simple wooden stick embued with pure magic', 'R', 'Mainhand', 6, ['NA'], ['NA'], 'Majicwand'],
    'Earthwand' :  ['a simple wooden stick embued with mud', 'R', 'Mainhand', 3, ['Stun','NA'], ['NA'], 'Earthwand'],
    'Silver Firewand' :  ['a silver stick embued with pure magic', 'E', 'Mainhand', 6, ['Fire','Fire'], ['NA'], 'SilverFirewand'],
    'Silver Icewand' :  ['a silver stick embued with mud', 'E', 'Mainhand', 6, ['Weak','Weak'], ['NA'], 'SilverIcewand'],
    'Silver Magicwand' :  ['a silver stick embued with pure magic', 'E', 'Mainhand', 12, ['NA'], ['NA'], 'SilverMajicwand'],
    'Silver Earthwand' :  ['a silver stick embued with mud', 'E', 'Mainhand', 6, ['Stun','Stun'], ['NA'], 'SilverEarthwand'],
             
    }

    try:
        open("Items")
    except:
        save(stuff,'Items')
        
    Items = load("Items")
        
    for spls in Items:
        print(spls,Items[spls])
    print()
        
    while True:
        try:
            print('')
            print('')
            new = str(input("Name of 'Item': "))
            if new == "":
                break
            ex = str(input("What it looks like (Discription): "))
            rair = str(input("How rare is it (Common(C),Rare(R),Epic(E),Legendary(L)): "))
            tp = str(input("What kind of item it is (Mainhand,Sidehand,Equip,Crafting): "))
            if 'Main' in tp:
                mx = int(input("Max dmg: "))
                print("")
                print("Types: Fire,Stun,Blinded,Weak,Regenerate,Shealded,Hidden")
                print("To end put NA")
                extra = []
                while True:
                    q = str(input("On hit give the oponent: "))
                    if q == '':
                        q = 'NA'
                    extra.append(q)
                    if q == "NA":
                        break
                print("")
                print("")
                print("Types: Fire,Stun,Blinded,Weak,Regenerate,Shealded,Hidden")
                print("To end put NA")
                self = []
                while True:
                    q = str(input("Any extra things when equiped: "))
                    if q == '':
                        q = 'NA'
                    self.append(q)
                    if q == "NA":
                        break
                Items[new] = [ex,rair,tp,mx,extra,self]
            elif 'Side' in tp:
                print("")
                #print("Types: Strainmax,Dodge,Resistance,HpBoost,Damage")
                #print("To end put NA")
                extra = {'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0}
                for asdf in extra:
                    #q = str(input("Given things when equiped : "))
                    #if q == '':
                    #    q = 'NA'
                    #    a = 0
                    #else:
                    print(asdf)
                    a = int(input("Strength of effect (0 for NONE): "))
                    extra[asdf] = a
                    #if q == "NA":
                    #    break
                print("")
                print("")
                Spells = load("Spells")
                for spls in Spells:
                    print(spls,Spells[spls])
                print()
                splls = []
                while True:
                    q = str(input("Spells when equiped: "))
                    if q == '':
                        q = 'NA'
                    splls.append(q)
                    if q == "NA":
                        break

                print('')
                print('Types of summon, Ghost, SpiritAnimal, Elemental')
                q = str(input("Summon when equiped: "))
                if q == '':
                    Sum = 'NA'
                else:
                    Sum = Creachure
                    splls.append('Summon')
                
                Items[new] = [ex,rair,tp,extra,splls,Sum]

            elif 'E' in tp:
                re = int(input('How much armor does it give: '))
                print("")
                print("Types: Summoning,Strainmax,Dodge,HpBoost,Damage")
                print("To end put NA")
                extra = []
                while True:
                    q = str(input("Given things when equiped: "))
                    if q == '':
                        q = 'NA'
                        a = 0
                    else:
                        a = int(input("Strength of effect: "))
                    extra.append([q,a])
                    if q == "NA":
                        break
                
                """
                print("")
                print("")
                Spells = load("Spells")
                for spls in Spells:
                    print(spls,Spells[spls])
                print()
                splls = []
                while True:
                    q = str(input("Spells when equiped: "))
                    if q == '':
                        q = 'NA'
                    splls.append(q)
                    if q == "NA":
                        break
                #"""
                Items[new] = [ex,rair,tp,extra,splls]
            else:
                Items[new] = [ex,rair,tp]
                      
            print("")
        except:
            pass
    save(Items,"Items")
    print('')

    
def NewSpells():
    #Edit existing()
    Spells = {"Run": [0,2,['NA'],['Run']],"Pet": [-2,0,['NA'],['Flip']],"Clot": [-4,-1,['NA'],['NA']],"Slash": [3,6,['Bleed'],['NA']],"Shield": [0,2,['NA'],['Shealded']],"Icespike": [2,7,['Weak'],['NA']],"Backstab": [0,10,['Bleed'],['Weak']],"Lightning": [4,9,['Stun'],['NA']],"Arrowfire": [0,5,['Bleed'],['NA']],"Leach": [2,6,['NA'],['Regenerate']],"Gunshot": [0,5,['Weak'],['NA']],"Volly": [0,10,['Bleed'],['NA']],"Firebolt": [3,7,['Fire'],['NA']],"Heal": [-6,0,['NA'],['NA']],"Meditate": [-5,0,['NA'],['Regenerate']], "Claw": [5,8,['Bleed'],['NA']],"Drink": [-6,0,['NA'],['Clumsy']],"NOPE": [100,200,['NA'],['Regenerate']]}
    for q in Spells:
        print(q, Spells[q])
    print()
    print()

    FIXER = {'Firebolt' : ['Shoot a bolt of fire that can burn.', 3, 7, ['Fire', '', 'NA'], ['NA'], 'Fire', 'Firebolt'],
    'Icebolt' : ['Shoot a bolt of ice that can weaken.', 3, 7, ['Weak','NA'], ['NA'], 'Ice', 'Icebolt'],
    "Magicbolt" : ['Fire a bolt of pure magic.', 5, 9, ['NA'], ['NA'], 'Majic', 'Magicbolt'],
    "Heal" : ['Heal with no downsides.', -6, 0, ['NA'], ['NA'], 'Heal', 'Heal'],
    "Drink": ['Heal but become Clumsy.', -6, -1, ['NA'], ['Clumsy', 'NA'], 'Heal', 'Drink'],
    'Troll': ['Reduces enemy accuracy and damage.', -10, -1, ['Blinded', 'Blinded', 'NA'], ['Shealded', 'Shealded', 'Shealded', 'NA'], 'Heal', 'Troll'],
    'Arrowfire': ['Fire an arrow which can Bleed.', 0, 5, ['Bleed', 'NA'], ['NA'], 'Majic', 'Arrowfire'],
    'Necromancy': ['Fire a soul dealing damage and giving you health.', 2, 15, ['NA'], ['Regenerate', 'Regenerate', 'NA'], 'Majic', 'Necromancy'],
    "Clot": ['Makes your blood clot faster healing you.', -4, -1, ['NA'], ['NA'], 'Heal', 'Clot'],
    "Gunshot": ['Fire your gun.', 4, 10, ['NA'], ['Weak', 'NA'], 'Blunderbussblast', 'Gunshot'],
    "Backstab": ["Stab'em in the back.", 0, 10, ['Bleed', 'NA'], ['Weak', 'Weak', 'Stun', 'NA'], 'Earth', 'Backstab'],
             }
    try:
        open("Spells")
    except:
        save(FIXER,'Spells')
        
    Spells = load("Spells")
        
    for spls in Spells:
        print(spls,Spells[spls])
    print()
        
    while True:
        try:
            new = str(input("Name of 'Spell': "))
            if new == "":
                break
            ex = str(input("What it does (Discription): "))
            mn = int(input("Min dmg (negitive is max for healing): "))
            mx = int(input("Max dmg: "))
            print("")
            print("Types: Fire,Stun,Blinded,Weak,Regenerate,Shealded,Hidden")
            print("To end put NA")
            extra = []
            while True:
                q = str(input("Any extra things to enemy: "))
                if q == '':
                    q = 'NA'
                extra.append(q)
                if q == "NA":
                    break
            print("")
            print("")
            print("Types: Fire,Stun,Blinded,Weak,Regenerate,Shealded,Hidden")
            print("To end put NA")
            self = []
            while True:
                q = str(input("Any extra things to you: "))
                if q == '':
                    q = 'NA'
                self.append(q)
                if q == "NA":
                    break

            print()
            print('Shot types: Fire, Ice, Earth, Majic, Heal(For Healing Spells Only)')
            Shottype = str(input("What will the Shot look like?: "))
            if Shottype  == '':
                Shottype = 'Majic'

                    
            Spells[new] = [ex,mn,mx,extra,self,Shottype,new]
            print("")
        except:
            pass
    save(Spells,"Spells")
    print('')

def NewRoadEvents():
    reset = {"ForbiddenKnowledge":{'Take': {'Check': [], 'Connects': ['End'], 'Fights': [], 'Print': ['You take the book, feeling more powerful than before.', 'Enter to continue.'], 'Change': [], 'Loot': ['Necronomicon'], 'Force': 'NA', 'Dmg': 0}, 'Leave': {'Check': [], 'Connects': ['End'], 'Fights': ['WM'], 'Print': ['Right as you leave a lesser demon appears.', 'He shouts in anger for you not reading the book.', ''], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'Open': {'Check': [], 'Connects': ['Take', 'Leave'], 'Fights': ['WM', 'WM'], 'Print': ['You open the book and the whole room darkens.', 'A bit of arcane knowledge fills your mind.', 'A lesser demon appears before you, furious at your reading.', 'Take book(1) leave without book(2)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'A': {'Check': [], 'Connects': ['Open', 'Leave'], 'Fights': [], 'Print': ['Wandering around you find a dusty book covered in blood.', 'Picking it up you hear screams echo around you.', 'You stand there contemplating on opening the book.', 'Eh, whats the worst that could happen, open it(1) leave(2).'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': '1'}},"Lentest":{'L': {'Check': [], 'Connects': [], 'Fights': [], 'Print': ['This is the minimum number of words previously.', 'Great(1)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'F': {'Check': [], 'Connects': ['LR', 'MR', 'G'], 'Fights': [], 'Print': ['Farther it is then how about we test this more  and more and more and more and more and more and even more.', 'Lesser(1),More?(2),Great(3)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'A': {'Check': [], 'Connects': ['F', 'L', 'G'], 'Fights': [], 'Print': ['Lets see how far we can go with this. Lets see shall we.', 'Farther(1),Less(2),Great(3).'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}},"Carriage": {'Look': {'Check': [], 'Connects': ['Ignore', 'Fight'], 'Fights': [], 'Print': ['Looking you can see some bandits sleeping in the bushes.', 'What do you want to do?', 'Leave(1), or Fight(2).', ''], 'Change': [0, 0, 1], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'Fight': {'Check': [], 'Connects': ['Ignore'], 'Fights': ['Bandit', 'Bandit'], 'Print': ['You have been spotted! ', 'Leave(1)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'Ignore': {'Check': [], 'Connects': ['End'], 'Fights': [], 'Print': ['You move along with no trouble.', 'Continue(1)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'Search': {'Check': ['Coin'], 'Connects': ['Ignore'], 'Fights': [], 'Print': ['There is some Loot!', 'Leave(1)'], 'Change': [0, 0, 1, -1, 0], 'Loot': ['20 Gold', 'Wood', 'Iron ore', 'Silver ore'], 'Force': 'Fight', 'Dmg': 0}, 'A': {'Check': [], 'Connects': ['Ignore', 'Search', 'Look'], 'Fights': [], 'Print': ['Ahead you can see an overturned carriage. ', 'There is nobody near it and it looks full of stuff.', "What do you wan't to do?", 'Ignore it (1), Search it(2), Look around(3).'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}},"Test": {'Why': {'Check': [], 'Connects': ['Bye'], 'Fights': [], 'Print': ['So I can make this an actual game.', 'It also lets me do my own things.', 'Like give you stuff for no reason.', 'Bye(1).'], 'Change': [], 'Loot': ['Wood', 'Rock'], 'Force': 'NA', 'Dmg': 0}, 'Bye': {'Check': [], 'Connects': ['End'], 'Fights': [], 'Print': ['Seeya!', 'Hit 1 to continue.'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'Like': {'Check': [], 'Connects': ['Why', 'Bye'], 'Fights': ['C'], 'Print': ['Like fights.', 'Why(1), Bye(2)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'A': {'Check': [], 'Connects': ['Like', 'Why', 'Ok'], 'Fights': [], 'Print': ['This is the test zone.', 'We test stuff here.', 'Like what(1), Why(2), Ok(3).'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}, 'Ok': {'Check': ['Coin'], 'Connects': ['Bye'], 'Fights': [], 'Print': ['Random time!', 'Bye(1)'], 'Change': [], 'Loot': [], 'Force': 'Ok', 'Dmg': 0}}}

    try:
        open("RoadEvents")
    except:
        save(reset,'RoadEvents')
        
    
    Events = load("RoadEvents")
    for spls in Events:
        print(spls,Events[spls])
        print()
    print()
    print()
    print()
        
    while True:
        new = str(input("Name of 'Event': "))
        if new == "":
            break
        Events[new] = {}
        while True:
            newer = str(input("Name of 'Sub-Event': "))
            if newer == "":
                break
            print()
            #print("-----------------------------------------------------------------------------------------")
            #max cant go past line
            Intro = str(input("Intro: "))
            Words = [Intro]
            for a in range(3):
                print()
                #print("---------------------------------------------------------------------------------------------------------------")
                q = str(input("Extra info (Not Conectors): "))
                if q == '':
                    break
                Words.append(q)
            print()
            #print("--------------------------------------------------------------------------------------------------------------------------")
            q = str(input("Conectors sentance, 4 max conectors: "))
            Words.append(q)
            
            Words = rapping(Words)
            
            Connectors = []
            for a in range(4):
                q = str(input("Connectors to other sub-events In ORDER "))
                if q == '':
                    break
                Connectors.append(q)

            Fights = []
            for a in range(12):
                print()
                print("Badguy types: Boss, Warior(W), Bandit(B), Thermons(T), Commonmen(C), Weak Monster(WM), Strong Monster(SM)")
                q = str(input("Badguys: "))
                if q == '':
                    break
                Fights.append(q)
                
            Damage = (input("Forced Damage?: "))
            if Damage == '':
                Damage = 0
                
            Loot = []
            for a in range(5):
                q = str(input("Loot?"))
                if q == '':
                    break
                Loot.append(q)
                
            Lose = []
            for a in range(5):
                q = str(input("Remove an item if its in invintory."))
                if q == '':
                    break
                Lose.append(q)
                
            Randoms = []
            Force = []
            for a in range(1):
                print()
                print('Random types: Sneak, Attack, Coin (1/2)')
                print('Checks: Item')
                q = str(input("Check"))
                if q == '':
                    break
                else:
                    Force.append(str(input("Force to another sub-event on fail check.")))
                Randoms.append(q)
            Force.append('NA')

            areas = ['Attacking','Runing','Options','Honor','Loyalty']
            Change_area = []
            for a in areas:
                print(a)
                q = (input("Add or subtract (1 or -1)"))
                if q == '':
                    break
                Change_area.append(int(q))

            Events[new][newer] = {'Print': Words, 'Connects':Connectors,'Loot':Loot,'Remove': Lose,'Check':Randoms,'Force':Force,'Change':Change_area, 'Fights': Fights,'Dmg': Damage}
            print('')
            print('')
            print('')

    save(Events,"RoadEvents")
    print('')

    import random

def coins(num):
    x = 0
    for a in range(num):
        if random.randrange(0,2) == 1:
            x += 1
    if x == num:
        return(True)
    return(False)

def rand(thing):
    return(thing[random.randrange(0,len(thing))])

def newRoom(wantedtypes):
    #Puzel, Gathering/rest,random, fight
    '''
    Three rings: Sequence of colors above door, one ring is set but doesent have the same colors
    Example: Red Red Blue, Ring has Blue, Orange, Yellow: anser is Orange Orange Blue, Because red + yellow = Orange
    '''
    if wantedtypes == 'Town':
        Room = {}
        #Room['A'] = {'Print': ['Welcome to town.',"Where do you wan't to go?",'Leave(1), Shop(2), Inn(3), Blacksmith(4)'], 'Connects':['Leave','Shop','Inn','Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}

        Room['Blacksmith'] = {'Print': ['As you walk up you can hear the banging of metal.','What do you want to craft?','Nothing, leave(1)','A Sword for 1 Ore and Wood(2)','A Shield for 1 Ore and Wood(3)','A random Rare item for 1 Ore and Wood(4)','A random Epic item for 1 Ore, Silver ore, and Wood(5)'], 'Connects':['A','Sword','Shield','Rair','Epic'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SWORDCHECK'] = {'Print': ["You don't have one ore and wood",'Back(1)'], 'Connects':['Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['Sword'] = {'Print': ["It doesen't take long for the sword to be crafted",'Back(1)'], 'Connects':['Blacksmith'],'Take':['Wood','Ore'],'Loot':['Sword'],'Check':['Ore','Wood'],'Force':'SWORDCHECK', 'Fights': [],'Dmg': 0}
        
        Room['SHIELDCHECK'] = {'Print': ["You don't have one ore and wood",'Back(1)'], 'Connects':['Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['Shield'] = {'Print': ["It doesen't take long for the shield to be crafted",'Back(1)'], 'Connects':['Blacksmith'],'Take':['Wood','Ore'],'Loot':['Shield'],'Check':['Ore','Wood'],'Force':'SHIELDCHECK', 'Fights': [],'Dmg': 0}

        Room['RANRAIR'] = {'Print': ["You don't have one ore and wood",'Back(1)'], 'Connects':['Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['Rair'] = {'Print': ["You quickly craft the item.",'Back(1)'], 'Connects':['Blacksmith'],'Take':['Wood','Ore'],'Loot':['MRR'],'Check':['Ore','Wood'],'Force':'SHIELDCHECK', 'Fights': [],'Dmg': 0}

        Room['RANEPIC'] = {'Print': ["You don't have one ore, silver ore, and wood",'Back(1)'], 'Connects':['Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['Epic'] = {'Print': ["You quickly craft the item.",'Back(1)'], 'Connects':['Blacksmith'],'Take':['Wood','Ore','Silver ore'],'Loot':['MRE'],'Check':['Ore','Wood','Silver ore'],'Force':'RANEPIC', 'Fights': [],'Dmg': 0}

        #Room['SHIELDCHECK'] = {'Print': ["You don't have one ore and wood",'Back(1)'], 'Connects':['Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        #Room['Shield'] = {'Print': ["It doesen't take long for the shield to be crafted",'Back(1)'], 'Connects':['Blacksmith'],'Take':['Wood','Ore'],'Loot':['Shield'],'Check':['Ore','Wood'],'Force':'SHIELDCHECK', 'Fights': [],'Dmg': 0}
        

        
        Room['Inn'] = {'Print': ['The Inn is mostly empty.','Are you going to rest?','Leave(1), Rest for 5 Coins(2)'], 'Connects':['A','Rest'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['Rest'] = {'Print': ['You pay for food and drink and rest for a while.','Your at full Health and Strain.','Leave(1)'], 'Connects':['A'],'Take':['Coin','Coin','Coin','Coin','Coin'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        
        Room['Shop'] = {'Print': ['Welcome to my shop!','Are you buying or selling?','Leave(1), Buy(2), Sell(3)'], 'Connects':['A','SHOPBUY','SHOPSELL'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SHOPSELL'] = {'Print': ['Continue(1)'], 'Connects':['Shop'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SHOPBUY'] = {'Print': ['Continue(1)'], 'Connects':['Shop'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        return(Room)
    
    if coins(4):
        Room = {}
        Room['A'] = {'Print': ['Welcome to my shop!','Are you buying or selling?','Leave(1), Buy(2), Sell(3)'], 'Connects':['End','SHOPBUY','SHOPSELL'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SHOPSELL'] = {'Print': ['Continue(1)'], 'Connects':['A'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SHOPBUY'] = {'Print': ['Continue(1)'], 'Connects':['A'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        return(Room)
    elif wantedtypes == 'Shop':
        Room = {}
        Room['A'] = {'Print': ['Welcome to my shop!','Are you buying or selling?','Leave(1), Buy(2), Sell(3)'], 'Connects':['End','SHOPBUY','SHOPSELL'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SHOPSELL'] = {'Print': ['Continue(1)'], 'Connects':['A'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        Room['SHOPBUY'] = {'Print': ['Continue(1)'], 'Connects':['A'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        return(Room)
    
    m = 'A'
    Room = {}
    Loots = ['Coin','Coin','Coin','Coin','Coin','Coin','RC','RC','RC','RC','RC','RR','RE','MRE','RC','MRR','MRC','RR','RC','RC','RR','RE','MRE','MRL','MRE','MRC','MRC','MRR','MRE','MRE','MRC','MRR','MRC','MRR','RE','MRL','MRL','MRL']
    Loot=[]
    for a in range(12):
        if coins(4):
            Loot.append(rand(Loots))
    
    Randoms =[]
    Checks = ['Sneak', 'Attack','Coin']
    for a in range(len(Checks)):
        if coins(5):
            Randoms.append(rand(Checks))
        
    #Force =
    Fights = []
    Fight = ['Boss','W','B','T','C','WM', "SM",'Rat','Rat']
    for a in range(6):
        if coins(3):
            Fights.append(rand(Fight))
         
    Dmg = ["H","D","D","N","N","N","N"]
    if rand(Dmg)== 'H':
        Damage = random.randrange(-6,-1)
    elif rand(Dmg)== 'D':
        Damage = random.randrange(1,6)
    else:
        Damage = 0

    Type = ''

    if len(Randoms) > 0:
        Type = Type + 'Posable '
        
    if Damage > 0:
        Type = Type + 'Trapped '
    elif Damage < 0:
        Type = Type + 'Replenishing '

    if 'MRL' in Loot:
        Type = Type + 'Legondary '
    elif len(Loot) > 3:
        Type = Type + 'Chest '
    elif len(Loot) > 0:
        Type = Type + 'Loot '

    if 'Boss' in Fights:
        Type = Type + 'Boss '
    elif len(Fights) > 3:
        Type = Type + 'Hord '
    elif len(Fights) > 0:
        Type = Type + 'Garded '

    if Type == '':
        Type = 'Connector'
    
    words = []
    Force = 'NA'
    Connectors = ['End']
    if 'Posable' in Type:
        Force = (str(m)+'Fall')
        Room[(str(m)+'Fall')] = {'Print': ["You fall through a hole in the floor.",'Move on(1)'], 'Connects':['End'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 2}
        
    if 'Boss' in Fights:
        words.append('Congratulations!')
        Connectors.append((str(m)+'Loot'))
        words.append('Next room(1), Loot the room(2)')
        Room[str(m)] = {'Print': ['There is a captan here!','Continue(1)'], 'Connects':[(str(m)+'Fight')],'Loot':[],'Check':Randoms,'Force':Force, 'Fights': [],'Dmg': 0}
        Room[(str(m)+'Fight')] = {'Print': words, 'Connects':Connectors,'Loot':[],'Check':Randoms,'Force':Force, 'Fights': Fights,'Dmg': 0}
        
    elif len(Fights) > 0:
        words.append('Congratulations!')
        Connectors.append((str(m)+'Loot'))
        words.append('Next room(1), Loot the room(2)')
        Room[str(m)] = {'Print': ['The room is guarded!','Continue(1)'], 'Connects':[(str(m)+'Fight')],'Loot':[],'Check':Randoms,'Force':Force, 'Fights': [],'Dmg': 0}
        Room[(str(m)+'Fight')] = {'Print': words, 'Connects':Connectors,'Loot':[],'Check':Randoms,'Force':Force, 'Fights': Fights,'Dmg': 0}
        
    else:
        if len(Loot) > 0:
            words.append('There is Loot!')
        if 'Trapped' in Type:
            words.append('The room is trapped!')
        elif 'Replenishing' in Type:
            words.append('The room has a healing fountain!')
        if len(words) == 0:
            words.append('Nothing here.')
        words.append('Next room(1)')
        Room[str(m)] = {'Print': words, 'Connects':Connectors,'Loot':Loot,'Check':Randoms,'Force':Force, 'Fights': Fights,'Dmg': Damage}

    if len(Connectors) > 1:
        words = []
        if len(Loot) > 0:
            words.append('There is Loot!')
        if 'Trapped' in Type:
            words.append('The room is trapped!')
        elif 'Replenishing' in Type:
            words.append('The room has a healing fountain!')
        if len(words) == 0:
            words.append('Nothing here.')
        words.append('Next room(1)')
        Room[(str(m)+'Loot')] = {'Print': words, 'Connects':['End'],'Loot':Loot,'Check':[],'Force':'NA', 'Fights': [],'Dmg': Damage}
    #print(Room)
    return(Room)
    
def TempSpells(Value = 'NA',TYPE = 'Ran'):
    #C: 0,3; R: 1,5; E: 3,7; L: 5,8 
    #['Def', Max, Min, [Target efects], [Owner efects],'Shottype','Name Placeholder']
    valtypes = {'C':[[0,4],[-3,1]],'R':[[1,6],[-5,0]],'E':[[3,8],[-7,-2]],'L':[[5,9],[-8,-4]]}
    if TYPE == 'Ran':
        Max = random.randrange(-8,9)
    elif TYPE == 'Dmg':
        Max = random.randrange(valtypes[Value][0][0],valtypes[Value][0][1])
    elif TYPE == 'Heal':
        Max = random.randrange(valtypes[Value][1][0],valtypes[Value][1][1])
        
    if Max <= 0:
        Min = Max
        try:
            Max = random.randrange(Min+2,0)
        except:
            Max = 0
    else:
        try:
            Min = random.randrange(0,Max-2)
        except:
            Min = 0
    if Max == Min:
        Max += 2
    
    tar_eff = []
    O_eff = []
    tar_eff_ch = ['Fire','Regenerate','Hidden','Stun','Blinded','Strained','Shealded','Weak']
    for a in range(random.randrange(0,3)):
        tar_eff.append(tar_eff_ch[random.randrange(0,len(tar_eff_ch))])
    for a in range(random.randrange(0,3)):
        O_eff.append(tar_eff_ch[random.randrange(0,len(tar_eff_ch))])
    Shot = ['Fire','Ice','Earth','Majic']
    Shottype = Shot[random.randrange(0,len(Shot))]
    tar_eff.append('NA')
    O_eff.append('NA')
    return(['Placeholder',Min,Max,tar_eff,O_eff,Shottype,name()])

def TempItems(Value = 'NA',TYPE = 'Ran'):
    
    #C: 0,3; R: 1,5; E: 3,7; L: 5,8 
    #Main = [ex,rair,tp,mx,extra,self,Look]
    #Side = [ex,rair,tp,extra,splls,Sum,look]
    #Extra = [ex,rair,tp,extra,splls,look]
    #Crafting = [ex,rair,tp]
    
    Types = ['Mainhand','Sidehand']
    valtypes = ['C','R','E','L']
    typesMOD = {'C':[[0,4],[-3,1]],'R':[[1,6],[-5,0]],'E':[[3,8],[-7,-2]],'L':[[5,9],[-8,-4]]}
    if TYPE == 'Ran':
        TYPE = Types[random.randrange(0,len(Types))]
        print(TYPE)
    if Value == 'NA':
        Value = valtypes[random.randrange(0,len(valtypes))]

    item = ['Placeholder',Value,TYPE]
    effects = ['Fire','Regenerate','Hidden','Stun','Blinded','Strained','Shealded','Weak']
    
    if TYPE == 'Mainhand':
        Look = ['Sword','Steel Sword','Royal Sword','Mace','Hachet']
        item.append(random.randrange(typesMOD[Value][0][0],(typesMOD[Value][0][1]+1)))
        extra = []
        if coins(1):
            for a in range(random.randrange(0,3)):
                print(123)
                extra.append(effects[random.randrange(0,len(effects))])
        extra.append('NA')
                
        self = []
        if coins(1):
            for a in range(random.randrange(0,3)):
                self.append(effects[random.randrange(0,len(effects))])
        self.append('NA')
            
        item.append(extra)
        item.append(self)
        item.append(Look[random.randrange(0,len(Look))])
        
        
        
    elif TYPE == 'Sidehand':
        Spells = ['Firebolt','Drink','Backstab']
        Points = random.randrange(typesMOD[Value][0][0],typesMOD[Value][0][1])
        q = {}
        Buffs = ['Resistance','HpBoost','Damage','Dodge','Strainmax']
        while len(Buffs) > 1:
            if Points != 0:
                num = random.randrange((Points*-1),Points)
            else:
                num = 0
            asdf = Buffs[random.randrange(0,len(Buffs))]
            q[asdf] = num
            Buffs.remove(asdf)
            Points -= num
        else:
            q[Buffs[0]] = Points
            
        
        item.append(q)
        Spel = []
        if coins(1):
            for a in range(random.randrange(0,2)):
                Spel.append(Spells[random.randrange(0,len(Spells))])
        Spel.append('NA')
        item.append(Spel)
        item.append(['NA'])
        if 'Firebolt' in Spel:
            item.append('Orb')
        elif 'Drink' in Spel:
            item.append('Flask')
        elif 'Backstab' in Spel:
            item.append('Dagger')
        else:
            if Value == 'E':
                item.append('Steel Shield')
            elif Value == 'L':
                item.append('Royal Shield')
            else:
                item.append('Shield')
                
        #'Royal Shield' :  ['an ornate steel shield', 'E', 'Sidehand', {'Resistance': 3,'HpBoost':2,'Damage':0, 'Dodge':0, 'Strainmax':0},[], ['NA'],'Royal Shield'],
        #Max = random.randrange(valtypes[Value][0][0],valtypes[Value][0][1])

    return([name(),item])
        
    
def BadBuild(Type,Level):
    #Fight = ['Boss','W','B','T','C','WM', "SM"]
    if Type == 'C':
        BGweps = ["Sword","Steel Sword","Royal Sword"]
        HP = int(random.randrange(5,10+Level)*1.5)
        Rest = random.randrange(0,3+int(Level/2))
        Spells = ['Clot',TempSpells('C','Dmg'),TempSpells()]
        Strain = 4+int(Level/2)
        Looks = "People\\BadCommonman\\redoneC"
        Dodge = 50
        P = random.randrange(5,9)
        #Bad = {"Name": 'They','Type': "BadWarrior\\redoneC",'Mainhand': BGweps[random.randrange(0,len(BGweps))],'LvL': Level,'Hp': HP,'Dodge': 50,'MaxHp': HP,'MaxStrain': 4, 'Strain': 2,'STDodge': 50 ,'MaxP': random.randrange(5,9),'Resist':Rest,'Resistor':Rest,'Spells':['Clot',TempSpells(),TempSpells()],'Aflictions':[]}

    elif Type == 'B':
        BGweps = ["Sword","Steel Sword","Royal Sword","Firewand","Icewand"]
        HP = int(random.randrange(5,10+Level)*1.5)
        Rest = random.randrange(0,2+int(Level/2))
        Spells = [TempSpells('C','Heal'),TempSpells()]
        Strain = 4 + int(Level/2)
        Looks = "People\\BadCretan\\redoneC"
        Dodge = random.randrange(50,61) 
        P = random.randrange(4,8)
        #Bad = {"Name": 'They','Type': "BadCretan\\redoneC",'Mainhand': BGweps[random.randrange(0,len(BGweps))],'LvL': Level,'Hp': HP,'Dodge': random.randrange(50,61),'MaxHp': HP,'MaxStrain': 3, 'Strain': 3,'STDodge': random.randrange(50,61) ,'MaxP': random.randrange(4,8),'Resist':Rest,'Resistor':Rest,'Spells':[TempSpells(),TempSpells()],'Aflictions':[]}

    elif Type == 'T':
        BGweps = ["Sword","Firewand","Icewand"]
        HP = int(random.randrange(5,8+Level)*1.5)
        Rest = random.randrange(0,2+int(Level/2))
        Spells = ['Heal',TempSpells('E','Dmg'),TempSpells()]
        Strain = int(Level/4)+4
        Looks = "People\\BadWiz\\redoneC"
        Dodge = random.randrange(50,66) 
        P = random.randrange(2,5)
        #Bad = {"Name": 'They','Type': "BadWiz\\redoneC",'Mainhand': BGweps[random.randrange(0,len(BGweps))],'LvL': Level,'Hp': HP,'Dodge': 50,'MaxHp': HP,'MaxStrain': 6, 'Strain': 6,'STDodge': random.randrange(50,66) ,'MaxP': random.randrange(2,5),'Resist':Rest,'Resistor':Rest,'Spells':['Heal',TempSpells(),TempSpells()],'Aflictions':[]}

    elif Type == 'W':
        BGweps = ["Sword","Steel Sword","Royal Sword"]
        HP = int(random.randrange(5,11+Level)*1.5)
        Rest = random.randrange(0,3+int(Level/2))
        Spells = ['Clot']
        Strain = 4 +int(Level/2)
        Looks = "People\\BadWarrior\\redoneC"
        Dodge = 50
        P = random.randrange(5,9)

    elif Type == 'Rat':
        BGweps = ["None"]
        HP = int(random.randrange(3,5+Level)*1.5)
        Rest = random.randrange(-2,int(Level/2))
        Spells = ['Clot']
        Strain = 2+int(Level/2)
        Looks = "Animals\\Rat\\redoneC"
        Dodge = random.randrange(50,66) 
        P = random.randrange(3,7)
    elif Type == 'Blondbeard1':
        Bad = {"Name": 'They','Type': "People\\CaptanBlondBeard\\redoneC",'Mainhand': "Royal Sword",'AITYPE': 'Tactical','Permeffects':{'Resistance': 1,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0},'LvL': 1,'Hp': 25,'Dodge': 60,'MaxHp': 25,'MaxStrain': 6, 'Strain': 6,'STDodge': 60 ,'MaxP': 8,'Resist':0,'Resistor':0,'Spells':['Drink','Gunshot'],'Aflictions':[],'HitEffects': [],}
        return(Bad)
    elif Type == 'Blondbeard':
        Level += 6
        BGweps = ["Royal Sword"]
        HP = int(random.randrange(5,11+Level)*1.5)
        Rest = random.randrange(0,3+int(Level/2))
        Spells = ['Drink','Gunshot']
        Strain = 6 + int(Level/2)
        Looks = "People\\CaptanBlondBeard\\redoneC"
        Dodge = random.randrange(60,76)
        P = random.randrange(5,9)+int(Level/2)
    elif Type == 'Felecia':
        Level += 6
        BGweps = ["Royal Sword"]
        HP = int(random.randrange(5,11+Level)*1.5)
        Rest = random.randrange(0,3+int(Level/2))
        Spells = ['Ghost','Backstab']
        Strain = 6 + int(Level/2)
        Looks = "People\\Felecia\\redoneC"
        Dodge = random.randrange(70,86)
        P = random.randrange(5,9)+int(Level/2)
    else:
        m = ['B','T','W','C']
        return(BadBuild(m[random.randrange(0,len(m))],int(Level*1.5)))

    AITYPES = ['Run','Rush','Tactical','Random']
    HITTYPS = ['Fire','Regenerate','Hidden','Stun','Blinded','Strained','Shealded','Weak']
    HIT = []
    if (Level/5 >= 1):
        for a in range(random.randrange(0,3)):
            HIT.append(HITTYPS[random.randrange(0,len(HITTYPS))])
    
    #btypes = ["BadCretan\\redoneC","BadWarrior\\redoneC","BadWiz\\redoneC"]
    #Badtype = btypes[random.randrange(0,len(btypes))]

    #WepTypes = ["redoneSword","redoneSteelSword","redoneRoyalSword","redoneFirewand","redoneIcewand"]
    #BGwep = WepTypes[random.randrange(0,len(WepTypes))]

    #Bad = {"Name": 'They','Type': Badtype,'Mainhand': BGwep,'Hp': 5,'Dodge': 50,'MaxHp':5,'MaxStrain': 4, 'Strain': 4,'STDodge': 50 ,'MaxP': 6,'Resist':0,'Spells':[]}
    Bad = {"Name": 'They','Type': Looks,'Mainhand': BGweps[random.randrange(0,len(BGweps))],'AITYPE': AITYPES[random.randrange(0,len(AITYPES))],'Permeffects':{'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0},'LvL': Level,'Hp': HP,'Dodge': Dodge,'MaxHp': HP,'MaxStrain': Strain, 'Strain': Strain,'STDodge': Dodge ,'MaxP': P,'Resist':Rest,'Resistor':Rest,'Spells':Spells,'Aflictions':[],'HitEffects': HIT,}
    return(Bad)

def name(kind = 'Ran'):
    Start = ['Mob','Cat','Act','Ana','Ant','Bed','Bog','Axe','Hit','Hot','Bra','Boy','Box','Lax','Kid','Jar','Cut','Kin','Ice','Jun','Jay','Nil','Nax','Nan','Oak','Pic','Pak','Sea','Sap','Saw','Set','Two','Tin','Tan','Tok','Web','Wet','Quit','Qult','Yen','Quin','Aqua','Quam']
    End = ['kind','leaf','tail','land','four','rock','place','found','mojo','jazz','buzz','jonk','juke','quak','cozy','whiz','whack','joke','java','fuji','monk','lunk','dunk','shunk','juba','flux','dozy','yutz','quag','zink']

    if kind == 'town':
        name = Start[random.randrange(0,len(Start))] + End[random.randrange(0,len(End))]
        return(str(name))
        
    conso = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    consoC = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

    voulsC = ['A','E','I','O','U']
    vouls = ['a','e','i','o','u']

    #if coins(2):
    #    name = voulsC[random.randrange(0,len(voulsC))]
    #else:
    #    name = consoC[random.randrange(0,len(consoC))]

    name = Start[random.randrange(0,len(Start))]
    v = 0
    c = 0
    for a in range(random.randrange(2,4)):
        if v >= 2:
            name = name+ conso[random.randrange(0,len(consoC))]
        elif c >= 3:
            name = name + vouls[random.randrange(0,len(voulsC))] 
        elif coins(2):
            v += 1
            c = 0
            name = name + vouls[random.randrange(0,len(voulsC))]
        else:
            v = 0
            c += 1
            name = name+ conso[random.randrange(0,len(consoC))]
    return(name)


def Map(size = 'Ran'):
    MAP = {}
    #Towns
    Sizes = {'Ran':[3,8],'Small':[3,6],'Med':[5,9],'Small':[7,10]}
    Places = []
    for a in range(random.randrange(Sizes[size][0],Sizes[size][1])):
        NAME = name('town')   
        Places.append(NAME)

    for NAME in Places:
        #BUILDTYPS = ['Smith','Stable','Farm','Shrine','Tower','Apocithary']
        Connections = {}
        for a in Places:
            if a == NAME:
                pass
            elif len(Connections) < 3:
                if random.randrange(0,5):
                    Connections[a] = random.randrange(3,21)
        
        MAP[str(NAME)] = {'Connections':Connections,'Shop':{'Name':name(),'CurCoin':random.randrange(20,121),'Loot':RanStoreInv(),'Shopcosts':ShopCosts()},'Townhall':{'Quests':['Ratlord'],'Mayor':name()},'Tavern':{'Name':name(),'Quests':['CleanBasment'],'Roomcost':random.randrange(2,16)}}
    for NAME in MAP:
        Connections = {}
        for xcv in MAP[NAME]['Connections']:
            if str(NAME) not in MAP[xcv]['Connections']:
                if random.randrange(0,2):
                    MAP[xcv]['Connections'][NAME] = MAP[NAME]['Connections'][xcv]
                    Connections[xcv] = MAP[NAME]['Connections'][xcv]
                else:
                    pass
                    
        if len(Connections) < 1:
            Connections['Capital'] = random.randrange(3,21)

    return(MAP)

def RanStoreInv():
    Items = load('Items')
    Stoc = {}
    for xcv in range(random.randrange(3,7)):
        for a in Items:
            if random.randrange(0,3):
                if a not in Stoc:
                    Stoc[a] = random.randrange(1,5)
                    break
    return(Stoc)
        

def ShopCosts():
    Shopcosts = {}
    Items = load('Items')
    for a in Items:
        if Items[a][1] == 'C':
            maxcost = 3
        elif Items[a][1] == 'R':
            maxcost = 9
        elif Items[a][1] == 'E':
            maxcost = 27
        else:
            maxcost = 81
            
        if 'Mainhand' in Items[a][2]:
            maxcost += 2
        if 'Sidehand' in Items[a][2]:
            maxcost += 3
        if 'Equip' in Items[a][2]:
            maxcost += 4
        else:
            maxcost += 1

        Shopcosts[a] = random.randrange(maxcost-3,maxcost+1)
    return(Shopcosts)

def rapping(Text_list):
    List = []
    for Text in Text_list:
        while len(Text) > 46:
            List.append(str(Text[0:47]))
            Text = Text[47:]
        else:
            List.append(Text)
    return(List)

def LAZYROOMMAKER():
    '''
    Ideas:
    1/2: Resting spot which may have a fight
    2/4: Bandit raid
    Muggers 2
    Pickpocket
    4/6: Old mine which may have silver
    Old bridge
    Gathering spot: Herbs
    Traveling Merchent
    Graverobbing
    Cave
    Mosoleam
    Hedgemazes
    '''
    try:
        open("RoadEvents")
    except:
        save({},'RoadEvents')
        
    Events = load("RoadEvents")
    UsedNames = ['BChest','BChestTraped','Restingcamp','Silvermine1','Silvermine2','Silvermine3','Silvermine4']
    Room = {}
    NAME = 'Silvermine2'
    #Template
    #Room['A'] = {'Print': ['',''], 'Connects':[''],'Take':[],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    #Checks = ['Sneak', 'Attack','Coin']
    
    Room['A'] = {'Print': ['The path is becoming more rocky.',"Up ahead you can see a small camp.",'Go to it(1), Walk past(2), Watch it(3)'], 'Connects':['Camp','Past','Bush'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['Camp'] = {'Print': ['As you get closer you see that it is abandoned.',"It looks like an old mining camp.",'Look around(1), Move on(2)'], 'Connects':['Invest','Past'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['Bush'] = {'Print': ['Slipping off into the underbrush you watch.',"It doesn’t take long for you to realize no one is there.",'Look around the camp(1), Move on(2)'], 'Connects':['Invest','Past'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    
    Room['Past'] = {'Print': ['You move on leaving behind the camp.','Leave(1)'], 'Connects':['RoadEnd'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}

    Room['Invest'] = {'Print': ['The camp seems to have been deserted along time ago.','There is an entrance to the mine.','Rest(1), Investigate more(2), Go in the mine(3), Leave(4)'], 'Connects':['Rest','Invest2',"Mine",'Past'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['Invest2'] = {'Print': ['You find a box!',"Open it(1), Move on(2)"], 'Connects':['BOX','Invest3'],'Loot':[],'Check':['Coin'],'Force':'Invest3', 'Fights': [],'Dmg': 0}
    Room['Invest3'] = {'Print': ['There is nothing more of interest','Rest(1), Go in the mine(2), Leave(3)'], 'Connects':['Rest',"Mine",'Past'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['BOX'] = {'Print': ['The box opens with ease.','Move on(1)'], 'Connects':['Invest3'],'Loot':['RR','RC','RC','RR'],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    
    Room['Mine'] = {'Print': ['Going down you find unlit torches.','Lighting one you move on to find a junction.','Go left(1), Go right(2), Leave(3)'], 'Connects':['LEFT1','RIGHT1','Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['LEFT1'] = {'Print': ['Going down further you find another junction.','Go left(1), Go right(2), Exit(3)'], 'Connects':['LEFT3','DeadEnd','Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['RIGHT1'] = {'Print': ['Going down further you find another junction.','Go left(1), Go right(2), Exit(3)'], 'Connects':['DeadEnd','LEFT2','Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['LEFT2'] = {'Print': ['Continuing on you see something glittering in the light.','Go to it(1), Exit(2)'], 'Connects':['SHINEY','Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['LEFT3'] = {'Print': ['Going down further you find another junction.','Go left(1), Go right(2), Exit(3)'], 'Connects':['LEFT3','DeadEnd','Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    Room['DeadEnd'] = {'Print': ['Suddenly the ceiling starts to rumble.','You run out just before the ceiling falls in.','Continue(1)'], 'Connects':['Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 2}
    
    Room['SHINEY'] = {'Print': ['You see silver!','Using your Picaxe to dig it out.','Exit(1)'],'Take':[], 'Connects':['Invest3'],'Loot':['Silver ore','Silver ore'],'Check':['Picaxe'],'Force':'SHINEYNOT', 'Fights': [],'Dmg': 0}
    Room['SHINEYNOT'] = {'Print': ['You see silver!','Sadly you have no Picaxe to dig it out with.','Leave(1)'],'Take':[], 'Connects':['Past'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}

    Room['Rest'] = {'Print': ['You lay down and take a nap.','Your at full Health and Strain.','Continue(1)'], 'Connects':['Invest3'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    
    
    #Fighting
    #Room[str(m)] = {'Print': ['The room is guarded!','Continue(1)'], 'Connects':[(str(m)+'Fight')],'Loot':[],'Check':Randoms,'Force':Force, 'Fights': [],'Dmg': 0}
    Fights = ['Rat','Rat']
    Room['Fight'] = {'Print': ['Fearing for more to come you quickly leave.','Leave(1)'], 'Connects':['RoadEnd'],'Loot':[],'Check':[],'Force':'NA', 'Fights': Fights,'Dmg': 0}
    
    #For Crafting
    #Room[''] = {'Print': ["You don't have one # and #",'Back(1)'], 'Connects':['#'],'Loot':[],'Check':['Ore','Wood'],'Force':'##', 'Fights': [],'Dmg': 0}
    #Room[''] = {'Print': ["It doesen't take long for the sword to be crafted",'Back(1)'], 'Connects':['Blacksmith'],'Take':['Wood','Ore'],'Loot':['Sword'],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}

    #For shops
    #Room['SHOPSELL'] = {'Print': ['Continue(1)'], 'Connects':['Shop'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
    #Room['SHOPBUY'] = {'Print': ['Continue(1)'], 'Connects':['Shop'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}

    
    Events[NAME] = Room
    save(Events,"RoadEvents")
    print("DONE!")


if __name__ == '__main__':
    pass
    #Words = ['I do not know where family doctors acquired illegibly perplexing handwriting nevertheless, extraordinary pharmaceutical intellectuality counterbalancing indecipherability, transcendentalizes intercommunications incomprehensibleness','I do not know where family doctors acquired illegibly perplexing handwriting nevertheless, extraordinary pharmaceutical intellectuality counterbalancing indecipherability, transcendentalizes intercommunications incomprehensibleness','I do not know where family doctors acquired illegibly perplexing handwriting nevertheless, extraordinary pharmaceutical intellectuality counterbalancing indecipherability, transcendentalizes intercommunications incomprehensibleness']
    #print(rapping(Words))
    '''
    print(World())
    print()
    for a in range(10):
        print(name())
    print()
    #'''
    LAZYROOMMAKER()
    NewSpells()
    NewItems()
    NewRoadEvents()
    #'''
