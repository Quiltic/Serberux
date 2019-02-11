import pygame, random, time,os, threading
from threading import Thread
from Tools import *
from Fight import *
from Invintory import *

#Seberux
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
    wep = str('redone'+Player["MainhandLooks"].replace(' ',''))
    Swep = str('redone'+Player["SidehandLooks"].replace(' ',''))
    
    gameDisplay = pygame.display.set_mode((200,200))
    DIR = os.getcwd().replace("NEWTEST",'')
    #Img = pygame.image.load(str("D:\\Python35-32\\Game\\Cretan\\"+ img+ '0.png')).convert_alpha()
    try:
        Img = pygame.image.load(str(DIR+"Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        Wep = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        Side = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ Swep+ '.png')).convert_alpha()

    except:
        wep = 'redonePlaceholder'
        Img = pygame.image.load(str(DIR+"Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        Wep = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        #IS_BROKE
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
    pygame.display.set_caption('Serberux')

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)#Max Didges is 47
    textsurface = myfont.render("", 0, (255, 100, 100))
    gameDisplay.blit(textsurface,(200,50))


    M = False
    x = 0
    global Shop
    Shop = {'Name':name(),'CurCoin':random.randrange(20,121),'Loot':RanStoreInv(),'Shopcosts':ShopCosts()}
    
    n = achual_stuff(Player,'A',Room,'A')
    while Playing:
        events = pygame.event.get()       
        for event in events:
            #print(event)
            if n != 'Inv':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        n = achual_stuff(Player,3,Room)
                    elif event.key == pygame.K_1:
                        n = achual_stuff(Player,1,Room)
                    elif event.key == pygame.K_2:
                        n = achual_stuff(Player,2,Room)
                    elif event.key == pygame.K_4:
                        n = achual_stuff(Player,4,Room)
                    elif event.key == pygame.K_5:
                        n = achual_stuff(Player,5,Room)
                    elif event.key == pygame.K_DOWN:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_m:
                        n = Invintory(Player,background,'Mag')
                    elif event.key == pygame.K_i:
                        n = Invintory(Player,background,'Inv')
                    elif event.key == pygame.K_n:
                        n = Invintory(Player,background,'ShopSell',Shop)
                    elif event.key == pygame.K_b:
                        n = Invintory(Player,background,'ShopBuy',Shop)
                    elif event.key == pygame.K_s:
                        save(Player,'Player')
                    elif event.key == pygame.K_l:
                        global Reset
                        Reset = True
                        return('Quicktil')
                        
                    #elif event.key == pygame.K_RETURN:
                    #    Spells = achual_stuff(Player,1,Room)
                elif pygame.mouse.get_pressed()[0] == True:
                    if ((pygame.mouse.get_pos()[0] < 40) and (pygame.mouse.get_pos()[1] < 40)):
                        n = Invintory(Player,Back,'Inv')
                    elif ((pygame.mouse.get_pos()[0] < 200) and (pygame.mouse.get_pos()[1] < 40)):
                        n = Invintory(Player,Back,'Mag')
                    if ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 40)):
                        #n = achual_stuff(Player,0,Room)
                        pass
                    elif ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 75)):
                        n = achual_stuff(Player,1,Room)
                    elif ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 110)):
                        n = achual_stuff(Player,2,Room)
                    elif ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 145)):
                        n = achual_stuff(Player,3,Room)
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
        GoodplS = [[135,85],[140,90],[135,85],[130,80],[135,85],[170,110],[10,85]]
        #Badpl = [[690,70],[695,65],[700,60],[695,65],[700,60],[530,90],[705,65]]
        
        gameDisplay.blit(Back, (0,0))
        
        gameDisplay.blit(Img, (0,20))
        gameDisplay.blit(Wep, (Goodpl[int(x)][0],Goodpl[int(x)][1]))
        gameDisplay.blit(Side, (GoodplS[int(x)][0],GoodplS[int(x)][1]))
        

        #matoc = 0
        #for a in range(len(EXTRATEXT)-1):
        #    matoc += 1
        #    if matoc > 3:
        #         break
        #"""
        for a in range(11):
            try:
                textsurface = myfont.render(str(EXTRATEXT[a+1]), 0, (0,0,0))
                gameDisplay.blit(textsurface,(215,(10+(a*18))))
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
            wep = str('redone'+Player["MainhandLooks"].replace(' ',''))
            Swep = str('redone'+Player["SidehandLooks"].replace(' ',''))
            Img = pygame.image.load(str(DIR+"Image Assets\\"+PlayType+GType)).convert_alpha()
            Wep = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()
            Side = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ Swep+ Gwep)).convert_alpha()
            
        except:
            wep = str('redonePlaceholder')
            Img = pygame.image.load(str(DIR+"Image Assets\\"+PlayType+GType)).convert_alpha()
            Wep = pygame.image.load(str(DIR+"Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()
            #Img = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+PlayType+GType)).convert_alpha()
            #Wep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()

        if n != False:
            #print(type(n))    
            if n == True:
                #time.sleep(len(EXTRATEXT))
                if len(Room[quarg]['Fights']) != 0:
                    for a in Room[quarg]['Fights']:
                        #Turn = 4
                        Demofight(Player,a)
                        Player['Xp'] = Player['Xp'] + random.randrange(100,201)
                n = False
            elif 'End' in n:
                q = n
                n = False
                Playing = True
                return(q)
            elif (n == 'Inv') or (n == 'Mag')or (n == 'Play'):
                n = False
            elif type(n) == dict:
                Shop = n
                n = False
                #print('STORE!')
            else:
                #print(n)
                q = n
                #print(q)
                n = False
                #print(q)
                if q != None:
                    #time.sleep(1.5)
                    n =achual_stuff(Player,'A',Room,q)
                #print(n)
        if Player['Hp'] <= 0:
            break
    

        
        
    #pygame.quit()
    #quit()
#Global used, quarg, Current
def achual_stuff(Player,inp,Room,force = False):
    #print("Crap")
    global EXTRATEXT
    global quarg
    global Turn
    global Playing
    
    #while len(EXTRATEXT) > 4:
    #    EXTRATEXT.remove(EXTRATEXT[0])
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
            try:
                quarg = Room[quarg]['Connects'][int(inp-1)]
                #print(Room[quarg]['Connects'])
                EXTRATEXT = []
            except:
                return(False)

        if 'End' in quarg:
            Playing = False
            return(quarg)
        #print(Room['A'])

        #print(Room[quarg]['Connects'])
        if quarg == 'A':
            EXTRATEXT = []
        #print(quarg)
        #'Permeffects':{'Resistance': 0,'HpBoost':0,'Damage':0 'Dodge':0, 'Strainmax':0}
        #print(Room[quarg]['Check'])
        if len(Room[quarg]['Check']) != 0:
            if Room[quarg]['Check'][0] == 'Coin':
                q = random.randrange(0,10)
            elif Room[quarg]['Check'][0] == 'Sneak':
                if int(Player['STDodge']+Player['Permeffects']['Dodge']/10) > 1:
                    q = random.randrange(0,int(Player['STDodge']+Player['Permeffects']['Dodge']/10))
                else:
                    q = 0
            elif Room[quarg]['Check'][0] == 'Attack':
                if int((Player['MaxP']+Player['Permeffects']['Damage'])/4) > 1:
                    q = random.randrange(0,int((Player['MaxP']+Player['Permeffects']['Damage'])/4)+1)
                else:
                    q = 0
                
            elif Room[quarg]['Check'][0] == 'InvAttack':
                if int((Player['MaxP']+Player['Permeffects']['Damage'])/4) > 1:
                    q = random.randrange(0,int((Player['MaxP']+Player['Permeffects']['Damage'])/4)+1)
                else:
                    q = 0
                    
                if q <= 4:
                    q = 10
                else:
                    q = 0
            else:
                for a in Room[quarg]['Check']:
                    #if a in  
                    #print(Room[quarg]['Check'])
                    #print(Player['Loot'][a])
                    try:
                        if Player['Loot'][a] >= 1:
                            print(True)
                            q = 10
                        else:
                            q = 0
                            break
                    except:
                        q = 0
                        break
            if q <= 4:
                EXTRATEXT.append('')
                EXTRATEXT.append(Room[quarg]['Print'][len(Room[quarg]['Print'])-1])
                return(Room[quarg]['Force'])
            else:
                T = False
        else:
            if Room[quarg]['Force'] != 'NA':
                return(Room[quarg]['Force'])
            T = False

        try:
            if len(Room[quarg]['Take']) != 0:
                for a in Room[quarg]['Take']:
                    if a == 'Coin':
                        Player['Coin'] -= 1
                    else:
                        try:
                            Player['Loot'][a] -= 1
                        except:
                            pass
        except:
            pass
            
        for a in range(len(Room[quarg]['Print'])-1):
            EXTRATEXT.append('')
            EXTRATEXT.append(Room[quarg]['Print'][a])

        

            #for a in Room[quarg]['Fights']:
                #Turn = 4
            #    Demofight(Player,a)
            #Turn = 3

        if Room[quarg]['Dmg'] != 0:
            EXTRATEXT.append('')
            if Room[quarg]['Dmg'] >= 0:
                EXTRATEXT.append((" You took %s damage!" % (Room[quarg]['Dmg']*Player['LvL'])))
            else:
                EXTRATEXT.append((" You healed for %s!" % (abs(Room[quarg]['Dmg']*Player['LvL']))))
            Player['Hp'] = Player['Hp'] - int(Room[quarg]['Dmg'])*Player['LvL']

        if Room[quarg]['Loot'] != []:
            Items = load("Items")
            Loots = ['RC','RR','RE','MRC','MRR','MRE','MRL']
            L = " You found: "
            EXTRATEXT.append('')
            for a in Room[quarg]['Loot']:
                if a == 'Coin':
                    L = L + str(a) + ', '
                    Player['Coin'] += 1
                elif a in Loots:
                    if 'MR' in a:
                        a = a.replace('MR', '')
                        it = TempItems(a,TYPE = 'Ran')
                        L = L + str(it[0]) + ', '
                        try:
                            Player['Loot'][it[0]] = it[1]
                            #print(Player['Loot'])
                        except:
                            print(it)
                    else:
                        lt = []
                        for it in Items:
                            if Items[it][1] == a[1]:
                                lt.append(it)
                        it = lt[random.randrange(0,len(lt))]
                        L = L + str(it) + ', '
                        try:
                            Player['Loot'][it] += 1
                        except:
                            Player['Loot'][it] = 1
                    
                else:
                    #print(type(a))
                    L = L + str(a) + ', '
                    try:
                        Player['Loot'][str(a)] += 1
                    except:
                        Player['Loot'][str(a)] = 1
                    
            L = L[0:int(len(L)-2)] +  '!'
            EXTRATEXT.append(L)

        

        if len(Room[quarg]['Fights']) != 0:
            EXTRATEXT.append('')
            EXTRATEXT.append(Room[quarg]['Print'][len(Room[quarg]['Print'])-1])
            return(True)
        
        
        EXTRATEXT.append('')
        EXTRATEXT.append(Room[quarg]['Print'][len(Room[quarg]['Print'])-1])
        
        if quarg == 'SHOPBUY':
            return(Invintory(Player,'BackgroundDStory','ShopBuy',Shop))
        if quarg == 'SHOPSELL':
            return(Invintory(Player,'BackgroundDStory','ShopSell',Shop))
        if quarg == 'Rest':
            Player['Hp'] = Player['MaxHp']+ (Player['Permeffects']['HpBoost'])*4
            Player['Strain'] = Player['MaxStrain']+ Player['Permeffects']['Strainmax']
            
        time.sleep(.05)
        return(False)
            
            #print("Test3")
        #"""

    #Turn = 4
    pygame.quit()

def Startmethod():
    Events = load('RoadEvents')
    Backg = "BackgroundForestStory"
    
    """
    If you like tradeing gives more traders: If you like fighting gives more fights: if you like crafting gives more crafting, if you like...
    Likes = {'Trading': 0,'Fighting': 0,'Crafting': 0,'Minigame': 0,'Puzels': 0}
    """
    global Room
    global Reset
    #visuals(Player,"BackgroundDStory")
    #Thread(target = achual_stuff).start()
    Roomcount = 0
    TOWNZONEDISTANCE = random.randrange(6,12)
    try:
        World = load('World')
        Player = load('Player')
        Room = World['Curroom']
        print("Loaded")
        #if World['Location'] in World['Map']:
    except:
        PlayerTypes = ["People\\Cretan\\redoneC","People\\Warrior\\redoneC","People\\Wiz\\redoneC"]
        Player = {"Name": 'You','Type': PlayerTypes[random.randrange(0,len(PlayerTypes))],'Mainhand': "None",'Sidehand': 'None','MainhandLooks': "None",'SidehandLooks': 'None','Extra': 'None','LvL': 1,'Xp': 0 ,'HitEffects': [],'Permeffects':{'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0},'Resistor':0,'Aflictions':[],'Loot': {},'Coin': 5,'Hp': 20,'Dodge': 50, 'Spells': [],'KnownSpells': [TempSpells('R','Heal'),TempSpells('R','Dmg'),TempSpells()],'MaxHp':20, 'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 2,'Resist':0,'Room': 'Random'}

        World = {'Map':Map('Small'), 'CurrentQuest':'NA', 'Time':0, 'Location':'Start', 'Distance':0,'Curroom': {'A': {'Check': [], 'Connects': ['B','End'], 'Fights': [], 'Print': [' You wake up on an infamilear beach.',' Hopefuly you remember some magic',' M for Magic.',' If your in a menu hit 0 to leave it.',' Hit (1) to continue.'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0},'B': {'Check': [], 'Connects': ['C','End'], 'Fights': [], 'Print': [' You scavange everything around before leaving.',' Hit I to look in invintory and to equip items.',' Continue(1)'], 'Change': [], 'Loot': ['Ore','Wood'], 'Force': 'NA', 'Dmg': 0},'C': {'Check': [], 'Connects': ['EndTown'], 'Fights': [], 'Print': [' Ahead is a town.', ' Go to the blacksmith and make a sword.',' Continue(1)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}}}
        Room = World['Curroom']
        for a in World['Map']:
            print(a)
            World['Location'] = str('Traveling'+a)
            break
    #print(TOWNZONE)
    #Quests examples
    #mainquest = {'RoomDistance': 13, 'Name':'Sanctuary', 'Prerequasits':['LvL3','ItemROCK'], 'Loot':['XP500','HANDS']}
    while 1:
        #print(Room)
        
        nextroom = visuals(Player,Backg)
        Backg = "BackgroundForestStory"
        if 'Traveling' in nextroom:
            c = nextroom.replace('End','')
            c = c.replace('Traveling','')
            TOWNZONEDISTANCE = World['Map'][World['Location']]['Connections'][c]
        if Reset:
            #global Player
            Player = load('Player')
            World = load('World')
            Reset = False
            try:
                if 'Traveling' in World['Location']:
                    Room = newRoom('p')
                else:
                    try:
                        Room = Events[World['Location']]
                    except:
                        Room = newRoom('p')
            except:
                Room = newRoom('p')
        elif World['Distance'] == TOWNZONEDISTANCE:
            Backg = "BackgroundTownStory"
            World['Distance'] = 0
            World['Location'] = World['Location'].replace('Traveling','')
            Room = newRoom('Town')
            startname = 'Welcome to ' + str(World['Location']) + ' town.'
            Room['A'] = {'Print': [startname,"Where do you wan't to go?",'Leave(1), Shop(2), Inn(3), Blacksmith(4)'], 'Connects':['Leave','Shop','Inn','Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
            lsts = []
            dist = ["Where do you wan't to go?"]
            b = 1
            for a in World['Map'][World['Location']]['Connections']:
                lsts.append(str('EndTraveling' + a))
                dist.append(str(a + '('+str(b)+')'))
                b += 1
                #print(dist)
            Room['Leave'] = {'Print': dist, 'Connects':lsts,'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
        else:
            if 'Town' in nextroom:
                Backg = "BackgroundTownStory"
                World['Distance'] = 0
                World['Location'] = World['Location'].replace('Traveling','')
                Room = newRoom('Town')
                startname = 'Welcome to ' + str(World['Location']) + ' town.'
                Room['A'] = {'Print': [startname,"Where do you wan't to go?",'Leave(1), Shop(2), Inn(3), Blacksmith(4)'], 'Connects':['Leave','Shop','Inn','Blacksmith'],'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
                lsts = []
                dist = ["Where do you wan't to go?"]
                b = 1
                for a in World['Map'][World['Location']]['Connections']:
                    lsts.append(str('EndTraveling' + a))
                    dist.append(str(a + '('+str(b)+')'))
                    b += 1
                    #print(dist)
                Room['Leave'] = {'Print': dist, 'Connects':lsts,'Loot':[],'Check':[],'Force':'NA', 'Fights': [],'Dmg': 0}
                
                
            else:
                try:
                    Room = Events[nextroom.replace('End','')]
                except:
                    for a in Events:
                        if coins(3):
                            Room = Events[a]
                            print(a)
                            break
                        else:
                            Room = newRoom('p')
                            
        World['Curroom'] = Room
        save(Player,'Player')
        save(World,'World')
        if Player['Hp'] <= 0:
            break
        World['Distance'] +=1
        Player['Xp'] = Player['Xp'] + random.randrange(20,81)
        if Player['Xp'] >= ((Player['LvL']*Player['LvL'])*170):
            n = Invintory(Player,"BackgroundForestStory",'Play')
    print(Roomcount)


EXTRATEXT = []
Turn = 2
Playing = True
quarg = ''

#Events = load('RoadEvents')
#Room = Events['Carriage']#"Boardercross","ForbiddenKnowledge"

"""
Ideas:
Light pusel: Turn all lights on: lights randomly turn one another off. 
"""
#Room = {'A': {'Check': [], 'Connects': ['B','End'], 'Fights': [], 'Print': [' You wake up on an infamilear beach.',' Hopefuly you remember some magic',' M for Magic.',' If your in a menu hit 0 to leave it.',' Hit (1) to continue.'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0},'B': {'Check': [], 'Connects': ['C','End'], 'Fights': [], 'Print': [' You scavange everything around before leaving.',' Hit I to look in invintory and to equip items.',' Continue(1)'], 'Change': [], 'Loot': ['Ore','Wood'], 'Force': 'NA', 'Dmg': 0},'C': {'Check': [], 'Connects': ['EndTown'], 'Fights': [], 'Print': [' Ahead is a town.', ' Go to the blacksmith and make a sword.',' Continue(1)'], 'Change': [], 'Loot': [], 'Force': 'NA', 'Dmg': 0}}

#Room = {'A': {'Check': [], 'Connects': ['SHOPSELL','SHOPBUY','End'], 'Fights': [], 'Print': [' Welcome to my shop.'," Do you wan't to buy or sell?"], 'Change': [], 'Loot': ['Sword'], 'Force': 'NA', 'Dmg': 0}}

#Room = {"A": {'Connects':['B','C','D'] ,'Print': ['To B(1),C(2),D(3)',len('How far can I achualy go? I mean realy.')]},'B': {'Connects':['C','D','E'] ,'Print': ['To C(1),D(2),E(3)']},'C': {'Connects':['D','E'] ,'Print': ['To D(1),E(2)']},'D':{'Connects':['E','A'] ,'Print': ['To E(1),A(2)']},'E': {'Connects':['A'] ,'Print': ['END.']}}
PlayerTypes = ["People\\Cretan\\redoneC","People\\Warrior\\redoneC","People\\Wiz\\redoneC"]
Player = {"Name": 'You','Type': PlayerTypes[random.randrange(0,len(PlayerTypes))],'Mainhand': "None",'Sidehand': 'None','MainhandLooks': "None",'SidehandLooks': 'None','Extra': 'None','LvL': 1,'Xp': 0 ,'HitEffects': [],'Permeffects':{'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0},'Resistor':0,'Aflictions':[],'Loot': {},'Coin': 5,'Hp': 20,'Dodge': 50, 'Spells': [],'KnownSpells': [TempSpells('R','Heal'),TempSpells('R','Dmg'),TempSpells()],'MaxHp':20, 'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 2,'Resist':0,'Room': 'Random'}

#'Permeffects':{'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0}
#'QUARG':['Words on page.','C','Mainhand',234,[],[],'Sword'

Reset = False
Startmethod()
        #print("Hello")
        #Thread(target = achual_stuff).start()

