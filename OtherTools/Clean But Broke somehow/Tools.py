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
import pickle, os

def save(obj, name ):
    #os.remove(name)
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

#Items
"""
'Necronomicon'
"""
    
def NewSpells():
    #Edit existing()
    Spells = {"Run": [0,2,['NA'],['Run']],"Pet": [-2,0,['NA'],['Flip']],"Clot": [-4,-1,['NA'],['NA']],"Slash": [3,6,['Bleed'],['NA']],"Shield": [0,2,['NA'],['Shealded']],"Icespike": [2,7,['Weak'],['NA']],"Backstab": [0,10,['Bleed'],['Weak']],"Lightning": [4,9,['Stun'],['NA']],"Arrowfire": [0,5,['Bleed'],['NA']],"Leach": [2,6,['NA'],['Regenerate']],"Gunshot": [0,5,['Weak'],['NA']],"Volly": [0,10,['Bleed'],['NA']],"Firebolt": [3,7,['Fire'],['NA']],"Heal": [-6,0,['NA'],['NA']],"Meditate": [-5,0,['NA'],['Regenerate']], "Claw": [5,8,['Bleed'],['NA']],"Drink": [-6,0,['NA'],['Clumsy']],"NOPE": [100,200,['NA'],['Regenerate']]}
    for q in Spells:
        print(q, Spells[q])
    print()
    print()
    try:
        open("Spells")
    except:
        save({},'Spells')
        
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
                
            Spells[new] = [ex,mn,mx,extra,self]
            print("")
        except:
            pass
    save(Spells,"Spells")

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
            print("-----------------------------------------------------------------------------------------")
            Intro = str(input("Intro max cant go past line: "))
            Words = [Intro]
            for a in range(3):
                print()
                print("---------------------------------------------------------------------------------------------------------------")
                q = str(input("Extra info (Not Conectors) Cant go past line: "))
                if q == '':
                    break
                Words.append(q)
            print()
            print("--------------------------------------------------------------------------------------------------------------------------")
            q = str(input("Conectors sentance max  is to Line 4 max conectors: "))
            Words.append(q)
            
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
                
            Randoms = []
            for a in range(1):
                print()
                print('Random types: Sneak, Attack, Coin (1/2)')
                q = str(input("Check"))
                if q == '':
                    break
                Randoms.append(q)

            Force = str(input("Force to another sub-event on fail check. Else (NA)"))
            if Force == '':
                Force = 'NA'

            areas = ['Attacking','Runing','Options','Honor','Loyalty']
            Change_area = []
            for a in areas:
                print(a)
                q = (input("Add or subtract (1 or -1)"))
                if q == '':
                    break
                Change_area.append(int(q))

            Events[new][newer] = {'Print': Words, 'Connects':Connectors,'Loot':Loot,'Check':Randoms,'Force':Force,'Change':Change_area, 'Fights': Fights,'Dmg': Damage}
            print('')
            print('')
            print('')

    save(Events,"RoadEvents")
    

if __name__ == '__main__':
    NewSpells()
    NewRoadEvents()
