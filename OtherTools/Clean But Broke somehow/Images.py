import pygame, random, time,os, threading
from threading import Thread
from Tools import *
from Fight import *

def visuals(Player, background):
    #Bace hand at 4,13
    #C1: 5,14
    #C3: 3,12
    #Attacking 
    #Hit 2,13
    global Bturn
    global Gturn
    global Playing
    global putin
    global Conferm

    pygame.init()

    clock = pygame.time.Clock()

    
    #ptypes = ["Cretan\\redoneC","Warrior\\redoneC","Wiz\\redoneC"]
    #btypes = ["BadCretan\\redoneC","BadWarrior\\redoneC","BadWiz\\redoneC"]
    PlayType = Player['Type']

    #WepTypes = ["redoneSword","redoneSteelSword","redoneRoyalSword","redoneFirewand","redoneIcewand"]
    wep = Player['Mainhand']
    
    gameDisplay = pygame.display.set_mode((200,200))
    DIR = os.getcwd().replace("NEWTEST",'')
    #Img = pygame.image.load(str("D:\\Python35-32\\Game\\Cretan\\"+ img+ '0.png')).convert_alpha()
    try:
        Img = pygame.image.load(str(DIR+"Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        Wep = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()

    except:
        IS_BROKE
        #Img = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        #Wep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        
    try:
        Back = pygame.image.load(DIR+"Image Assets\\Background\\redone"+background+".png").convert_alpha()
    except:
        ISBROKE
        #Back = pygame.image.load("E:\\Python35-32\\Game\\Image Assets\\Background\\redone"+background+".png").convert_alpha()


    display_width = Back.get_width()
    display_height = Back.get_height()

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Game')

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render("", 0, (255, 100, 100))
    gameDisplay.blit(textsurface,(200,50))


    M = False
    x = 0
    achual_stuff(Player,'A',Room,'A')
    n = False

    while Playing:
        events = pygame.event.get()       
        for event in events:
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    n = achual_stuff(Player,3,Room)
                elif event.key == pygame.K_1:
                    n = achual_stuff(Player,1,Room)
                elif event.key == pygame.K_2:
                    n = achual_stuff(Player,2,Room)
                elif event.key == pygame.K_DOWN:
                    Turn = 4
                elif event.key == pygame.K_RETURN:
                    Spells = achual_stuff(Player,1,Room)
            else:
                putin = 3
        
                #Turn = 3
        '''
        print(pause)
        while pause:
            print(pause)
            Conferm = True
            time.sleep(1)
        Conferm = False
        '''
                
        """              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        """
        #0,1,2,3,4,?,A,M
        Goodpl = [[20,85],[25,90],[20,85],[15,80],[15,80],[170,110],[10,85]]
        #Badpl = [[690,70],[695,65],[700,60],[695,65],[700,60],[530,90],[705,65]]
        
        gameDisplay.blit(Back, (0,0))
        
        gameDisplay.blit(Img, (0,20))
        gameDisplay.blit(Wep, (Goodpl[int(x)][0],Goodpl[int(x)][1]))
        

        #matoc = 0
        #for a in range(len(EXTRATEXT)-1):
        #    matoc += 1
        #    if matoc > 3:
        #         break
        #"""
        for a in range(9):
            try:
                textsurface = myfont.render(str(EXTRATEXT[a+1]), 0, (0,0,0))
                gameDisplay.blit(textsurface,(215,(10+(a*25))))
            except:
                pass
        
        #textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-2]), 0, (0,0,0))
        #gameDisplay.blit(textsurface,(215,(40)))
        #textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-3]), 0, (0,0,0))
        #gameDisplay.blit(textsurface,(215,(70)))#+(a*(30))
        #"""
        
        pygame.display.update()
        clock.tick(60)
        
        
        x += .04 
        if x > 4:
            x = 0

        if M:
            #BREAK
            time.sleep(1)
            x = 0
            y = 0
            Bturn = ""
            Gturn = ""
            M = False      
                
            
        """  
        if "Miss" in Gturn:
            BType = 'Miss.png'
            Bwep = ".png"
            
            GType = 'PAttack.png'
            Gwep = 'PAttack.png'
            M = True
            
            x = 5
            y = 0
            Shottype = wep + "blast.png"
            BShottype = "redoneNone.png"
            
        elif "Hit" in Gturn:
            BType = 'Hit.png'
            Bwep = ".png"
            
            GType = 'PAttack.png'
            Gwep = 'PAttack.png'
            M = True
            x = 5
            y = 6
            Shottype = wep + "blast.png"
            BShottype = "redoneNone.png"
        """
        
        if M != True:
            GType = str(int(x))+'.png'
            BType = str(int(x))+'.png'
            Gwep = ".png"
            Bwep = ".png"
            Shottype = "redoneNone.png"
            BShottype = "redoneNone.png"

        try:
            Img = pygame.image.load(str(DIR+"Image Assets\\"+PlayType+GType)).convert_alpha()
            Wep = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()
            
        except:
            BROKEN
            #Img = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+PlayType+GType)).convert_alpha()
            #Wep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()

        
        if n != False:
            #print(n)
            if n == True:
                time.sleep(2)
                if len(Room[quarg]['Fights']) != 0:
                    for a in Room[quarg]['Fights']:
                        #Turn = 4
                        Demofight(Player,a)
                n = False
            else:
                #print(n)
                time.sleep(1.5)
                q = n
                n = False
                #print(q)
                n =achual_stuff(Player,'A',Room,q)
                #print(n)
                
        
    pygame.quit()
    quit()

def achual_stuff(Player,inp,Room,force = False):
    #print("Crap")
    global EXTRATEXT
    global quarg
    global Turn
    global Playing

    while len(EXTRATEXT) > 4:
        EXTRATEXT.remove(EXTRATEXT[0])
    #print(events)
    #print("Test")
    T = True
    while T:
        #Events[new][newer] = {'Print': Words, 'Connects':Connectors,'Loot':Loot,'Check':Randoms,'Force':Force,'Change':Change_area, 'Fights': Fights,'Dmg': Damage}
        #try:
        #print("Test1")
        if force != False:
            quarg = force
            EXTRATEXT = []
            
        else:
            quarg = Room[quarg]['Connects'][int(inp-1)]
            EXTRATEXT = []

        if quarg == 'End':
            Playing = False
            break
        #print(Room['A'])
        
        if quarg == 'A':
            EXTRATEXT = []
        #print(quarg)
        for a in range(len(Room[quarg]['Print'])-1):
            EXTRATEXT.append('')
            EXTRATEXT.append(Room[quarg]['Print'][a])

        

            #for a in Room[quarg]['Fights']:
                #Turn = 4
            #    Demofight(Player,a)
            #Turn = 3

        if Room[quarg]['Dmg'] != 0:
            EXTRATEXT.append('')
            EXTRATEXT.append(("You took %s damage!" % (Room[quarg]['Dmg'])))
            Player['Hp'] = Player['Hp'] - int(Room[quarg]['Dmg'])

        if Room[quarg]['Loot'] != []:
            L = "You found: "
            EXTRATEXT.append('')
            for a in Room[quarg]['Loot']:
                L = L + str(a) + ', '
                Player['Loot'].append(a)
            L = L +  '!'
            EXTRATEXT.append(L)

        if len(Room[quarg]['Check']) != 0:
            if Room[quarg]['Check'][0] == 'Coin':
                q = random.randrange(0,2)
            elif Room[quarg]['Check'][0] == 'Sneak':
                q = random.randrange(0,2)
            elif Room[quarg]['Check'][0] == 'Attack':
                q = random.randrange(0,2)
            if q == 1:
                EXTRATEXT.append('')
                EXTRATEXT.append(Room[quarg]['Print'][len(Room[quarg]['Print'])-1])
                return(Room[quarg]['Force'])
            else:
                T = False
        else:
            T = False

        if len(Room[quarg]['Fights']) != 0:
            EXTRATEXT.append('')
            EXTRATEXT.append(Room[quarg]['Print'][len(Room[quarg]['Print'])-1])
            return(True)

        EXTRATEXT.append('')
        EXTRATEXT.append(Room[quarg]['Print'][len(Room[quarg]['Print'])-1])
        time.sleep(.05)
        return(False)
            
            #print("Test3")
        #"""

    #Turn = 4

def Startmethod():
    visuals(Player,"BackgroundDStory")
    #Thread(target = achual_stuff).start()
    while Turn != 100:
        if Turn == 3:
            visuals(Player,"BackgroundDStory")
            Turn = 2


EXTRATEXT = []
Turn = 2
Playing = True
quarg = ''

Events = load('RoadEvents')
Room = Events["ForbiddenKnowledge"]#'Carriage'
#Room = {"A": {'Connects':['B','C','D'] ,'Print': ['To B(1),C(2),D(3)',len('How far can I achualy go? I mean realy.')]},'B': {'Connects':['C','D','E'] ,'Print': ['To C(1),D(2),E(3)']},'C': {'Connects':['D','E'] ,'Print': ['To D(1),E(2)']},'D':{'Connects':['E','A'] ,'Print': ['To E(1),A(2)']},'E': {'Connects':['A'] ,'Print': ['END.']}}
Player = {"Name": 'You','Type': "Cretan\\redoneC",'Mainhand': "redoneSteelSword",'Loot': [],'Hp': 20,'Dodge': 50, 'Spells': ["Firebolt",'Drink'],'MaxHp':20, 'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 6,'Resist':0}


Startmethod()
        #print("Hello")
        #Thread(target = achual_stuff).start()

