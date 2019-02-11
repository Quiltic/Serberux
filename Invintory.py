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
    global EXTRATEXT
    global Current

    pygame.init()
    Playing = True
    EXTRATEXT = []

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
        wep = str('redonePlaceholder')
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
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render("", 0, (255, 100, 100))
    gameDisplay.blit(textsurface,(200,50))


    M = False
    x = 0
    if 'Buy' in TP:
        stuff = invin(Shop)
    else:
        stuff = invin(Player)
    
    n = achual_stuff(Player,999,stuff)
    SHIFT = False
    Current = 'None'
    while Playing:
        try:
            events = pygame.event.get()       
            for event in events:
                #print(event)
                if event.type == pygame.KEYDOWN:
                    ph = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]
                    for a in range(len(ph)):
                        if event.key == ph[a]:
                            if SHIFT:
                                a += 9
                                SHIFT = False
                            n = achual_stuff(Player,a+1,stuff,Current)
                            if 'Buy' in TP:
                                stuff = invin(Shop)
                            else:
                                stuff = invin(Player)
                                
                    if event.key == pygame.K_DOWN:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_LSHIFT:
                        if SHIFT:
                            SHIFT = False
                        else:
                            SHIFT = True
                    if event.key == pygame.K_RSHIFT:
                        if SHIFT:
                            SHIFT = False
                        else:
                            SHIFT = True
                        
                    elif event.key == pygame.K_0:
                        n = achual_stuff(Player,0,stuff)
                elif pygame.mouse.get_pressed()[0] == True:
                    if ((pygame.mouse.get_pos()[0] < 40) and (pygame.mouse.get_pos()[1] < 40)):
                        n = achual_stuff(Player,0,stuff)
                    elif ((pygame.mouse.get_pos()[0] < 200) and (pygame.mouse.get_pos()[1] < 40)):
                        n = achual_stuff(Player,0,stuff)
                    if ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 40)):
                        n = achual_stuff(Player,0,stuff)
                    elif ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 75)):
                        n = achual_stuff(Player,1,stuff,Current)
                    elif ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 110)):
                        n = achual_stuff(Player,2,stuff,Current)
                    elif ((pygame.mouse.get_pos()[0] > 750) and (pygame.mouse.get_pos()[1] < 145)):
                        n = achual_stuff(Player,3,stuff,Current)
                        
                    if 'Buy' in TP:
                        stuff = invin(Shop)
                    else:
                        stuff = invin(Player)
        except:
            n = achual_stuff(Player,999,stuff)
        #0,1,2,3,4,?,A,M
        Goodpl = [[20,85],[25,90],[20,85],[15,80],[15,80],[170,110],[10,85]]
        GoodplS = [[135,85],[140,90],[135,85],[130,80],[135,85],[170,110],[10,85]]
        #Badpl = [[690,70],[695,65],[700,60],[695,65],[700,60],[530,90],[705,65]]
        
        gameDisplay.blit(Back, (0,0))
        
        gameDisplay.blit(Img, (0,20))
        gameDisplay.blit(Wep, (Goodpl[int(x)][0],Goodpl[int(x)][1]))
        gameDisplay.blit(Side, (GoodplS[int(x)][0],GoodplS[int(x)][1]))

        for a in range(9):
            try:
                textsurface = myfont.render(str(EXTRATEXT[a+1]), 0, (0,0,0))
                gameDisplay.blit(textsurface,(215,(10+(a*25))))
            except:
                pass

        
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
            #BROKEN
            #Img = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+PlayType+GType)).convert_alpha()
            #Wep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()

        if n != False:
            #print(n)
            if n == 'End':
                Playing = True
                n = False
                break
                
            if n == True:
                time.sleep(len(EXTRATEXT))
                n = False
            elif (n == 'Inv') or (n == 'Mag') or (n == 'Play'):
                pass
            elif n == '999':
                n =achual_stuff(Player,999,stuff)
            else:
                #print(n)
                time.sleep(1.5)
                q = n
                n = False
                #print(q)
                n =achual_stuff(Player,999,stuff)
                #print(n)
        if Player['Hp'] <= 0:
            break

        
        
    #pygame.quit()
    #quit()

def achual_stuff(Player,option,stuff,CurrentI = 'None'):
    global EXTRATEXT
    global Current
    Items = load('Items')
    Spells = load('Spells')
    Fornow = {'Fire':'Burning','Stun':'Stuned','Weak':'Weakend','Regenerate':'Regenerating','Bleed':'Bleeding','NA':'','':''}
    SideHandSpells = ['Firebolt','Drink','Backstab','Icebolt']

    try:
        Up = [EXTRATEXT[len(EXTRATEXT)-3],EXTRATEXT[len(EXTRATEXT)-2],EXTRATEXT[len(EXTRATEXT)-1]]
    except:
        pass
    
    while len(EXTRATEXT) > 4:
        EXTRATEXT.remove(EXTRATEXT[0])
    EXTRATEXT = []

    #for a in Player['Loot']:
    #    print(a)
    #    if Player['Loot'][a] == 0:
    #        stuffnthings = stuff.remove(stuff.index(str(a)))
    #Loot = [[Item,amount],[Itemstats,amount]]
    #Main = [ex,rair,tp,mx,extra,self,Look]
    #Side = [ex,rair,tp,extra,splls,Sum,look]
    #Extra = [ex,rair,tp,extra,splls,look]
    #Crafting = [ex,rair,tp]
    if TP == 'Inv':
        if option == 999:    
            if Player['Mainhand'] != 'None':
                if Player['Loot'][Player['Mainhand']] == 0:
                    Player['Mainhand'] = 'None'
                    Player['MainhandLooks'] = 'None'
                    Player['MaxP'] = Player['LvL']+1
                    Player['HitEffects'] = []
                        
            if Player['Sidehand'] != 'None':
                if Player['Loot'][Player['Sidehand']] == 0:
                    Player['Sidehand'] = 'None'
                    Player['SidehandLooks'] = 'None'
                    Player['Permeffects'] = {'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0}
                    for a in Player['Spells']:
                        if a in SideHandSpells:
                            Player['Spells'].remove(a)
                
        #elif Player['Mainhand'] not in Player['Loot']:
        #    achual_stuff(Player,3,stuff,Player['Mainhand'])

        
        T = True
        while T:
            
            #EXTRATEXT = ['',' Your Invintory : Hit 0 to Leave']
            if option == 999:
                EXTRATEXT = ['',' Your Invintory : Hit 0 to Leave']
                Notdone = True
                a = 0
                #c = 0
                
                while Notdone:
                    fx = ''
                    for b in range(4):
                        try:
                            fx = (fx + ' ' + str(stuff[a+b]) + '('+str(a+b+1)+'),')
                            #c += 1
                            #if c >= 9:
                                #
                        except:
                            Notdone = False
                            break
                    EXTRATEXT.append(fx)
                    a += 4
            elif option == 0:
                return('End')
            elif CurrentI != 'None':
                if option == 1:
                    Current = 'None'
                    return('999')
                elif option == 2:
                    #print(Player['Loot'][Current])
                    try:
                        Player['Loot'][Current] -= 1
                    except:
                        Player['Loot'][Current] = 0
                        Player['Coin'] += 1
                        
                    Current = 'None'
                    return('999')
                elif option == 3:
                    print(Current)
                    #'MaxHp':20, 'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 6,'Resistor':0,'HitEffects': [],'Permeffects':[]
                    if ((Current == Player['Mainhand']) or (Current == Player['Sidehand']) or(Current == Player['Extra'])):
                        #try:
                        if 'Main' in Items[Current][2]:
                            Player['Mainhand'] = 'None'
                            Player['MainhandLooks'] = 'None'
                            Player['MaxP'] = Player['LvL']+1
                            Player['HitEffects'] = []
                            
                        elif 'Side' in Items[Current][2]:
                            Player['Sidehand'] = 'None'
                            Player['SidehandLooks'] = 'None'
                            Player['Permeffects'] = {'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0}
                            for a in Player['Spells']:
                                if a in SideHandSpells:
                                    Player['Spells'].remove(a)
                            
                        elif 'Extra' in Items[Current][2]:
                            Player['Extra'] = 'None'

##                        except:
##                            #For Random Items    
##                            if 'Main' in Player['Loot'][Current][2]:
##                                Player['Mainhand'] = 'None'
##                                Player['MainhandLooks'] = 'None'
##                                Player['MaxP'] = Player['LvL']+1
##                                Player['HitEffects'] = []
##                                
##                            elif 'Side' in Player['Loot'][Current][2]:
##                                Player['Sidehand'] = 'None'
##                                Player['SidehandLooks'] = 'None'
##                                Player['Permeffects'] = {'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0}
##                                for a in Player['Loot'][Current][4]:
##                                    if a in Player['Spells']:
##                                        Player['Spells'].remove(a)
##                                
##                                
##                            elif 'Extra' in Player['Loot'][Current][2]:
##                                Player['Extra'] = 'None'
                    else:
                        #print("Types: Fire,Stun,Blinded,Weak,Regenerate,Shealded,Hidden")
                        #("Types: Strainmax,Dodge,Resistance,HpBoost,Damage")
                        #Main = [ex,rair,tp,maxDMG,extra,self,look]
                        #Side = [ex,rair,tp,extra,splls,Sum,look]
                        #Extra = [ex,rair,tp,extra,splls,look]
                        #Crafting = [ex,rair,tp]

                        try:
                            if 'Main' in Items[Current][2]:
                                Player['Mainhand'] = Current
                                Player['MainhandLooks'] = Items[Current][6]
                                Player['MaxP'] = Player['LvL']+1
                                Player['MaxP'] += Items[Current][3]
                                Player['HitEffects'] = Items[Current][4]
                                #Player['Permeffects'] = Items[Current][5]
                                
                                
                            elif 'Side' in Items[Current][2]:
                                Player['Sidehand'] = Current
                                Player['SidehandLooks'] = Items[Current][6]
                                Player['Permeffects'] = Items[Current][3]
                                for a in Player['Spells']:
                                    if a in SideHandSpells:
                                        Player['Spells'].remove(a)
                                        
                                for a in Items[Current][4]:
                                    if a != 'NA':
                                        if a not in Player['Spells']:
                                            Player['Spells'].append(a)
                                
                                
                            elif 'Extra' in Items[Current][2]:
                                Player['Extra'] = Current

                        except:
                            if 'Main' in Player['Loot'][Current][2]:
                                Player['Mainhand'] = Current
                                Player['MainhandLooks'] = Player['Loot'][Current][6]
                                Player['MaxP'] = Player['LvL']+1
                                Player['MaxP'] += Player['Loot'][Current][3]
                                Player['HitEffects'] = Player['Loot'][Current][4]
                                #Player['Permeffects'] = Items[Current][5]
                                    
                                
                            elif 'Side' in Player['Loot'][Current][2]:
                                Player['Sidehand'] = Current
                                Player['SidehandLooks'] = Player['Loot'][Current][6]
                                Player['Permeffects'] = Player['Loot'][Current][3]
                                for a in Player['Spells']:
                                    if a in SideHandSpells:
                                        Player['Spells'].remove(a)
                                for a in Player['Loot'][Current][4]:
                                    if a != 'NA':
                                        if a not in Player['Spells']:
                                            Player['Spells'].append(a)
                                
                                
                            elif 'Extra' in Player['Loot'][Current][2]:
                                Player['Extra'] = Current
                                
                    Current = 'None'
                    return('999')
                        
                    
            
                
            else:
                try:
                    Item = Items[stuff[option-1]]
                except:
                    Item = Player['Loot'][stuff[option-1]]
                    #print(Item)
                    #Item = Player['Loot']["Name"]
                    
                Current = stuff[option-1]#Item
                EXTRATEXT = ['']
                try:
                    EXTRATEXT.append(' %s: You have %s of them.' % (stuff[option-1],int(Player['Loot'][stuff[option-1]])))
                except:
                    EXTRATEXT.append(' %s: You have 1 of them.' % (stuff[option-1]))
                EXTRATEXT.append(" It is %s." % (Item[0]))
                EXTRATEXT.append(" It's a %s item." % (Item[2]))
                if 'Main' in Item[2]:
                    
                    EXTRATEXT.append(" It's max bonus dmg is %s." % (Item[3]))
                    if len(Item[4]) > 1:
                        l = ''
                        for a in Item[4]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It does %son hit." % (l))
                    #if len(Item[5]) > 1:
                    #    l = ''
                    #    for a in Item[5]:
                    #        if a == 'NA':
                    #            break
                    #        l = l + a + ' '
                    #    EXTRATEXT.append(" It gives %s on equip." % (l))
                elif 'Side' in Item[2]:
                    EXTRATEXT.append(" It gives: Resistance %s" % (Item[3]['Resistance']))
                    EXTRATEXT.append(" HpBoost %s: Damage %s" % (Item[3]['HpBoost'],Item[3]['Damage']))
                    EXTRATEXT.append(" Dodge %s: Strain %s" % (Item[3]['Dodge'],Item[3]['Strainmax']))
                    #{'Resistance': 0,'HpBoost':0,'Damage':0, 'Dodge':0, 'Strainmax':0}
                    if len(Item[4]) > 1:
                        l = ''
                        for a in Item[4]:
                            if a == 'NA':
                                break
                            l = l + a + ' '
                        EXTRATEXT.append(" It gives %s spells on equip." % (l))
                    #try:
                        #EXTRATEXT.append(" It gives %s minon type." % (Item[5]))
                    #except:
                    #   pass
                elif 'Extra' in Item[2]:
                    l = ''
                    for a in Item[3]:
                        if a == 'NA':
                            a = 'nothing'
                        l = l + a + ' '
                    EXTRATEXT.append(" It gives %son equip." % (l))
                    l = ''
                    for a in Item[4]:
                        if a == 'NA':
                            a = 'nothing'
                        l = l + a + ' '
                    EXTRATEXT.append(" It gives %s spells on equip." % (l))
                
                if 'Crafting' != Item[2]:
                    if ((Current == Player['Mainhand']) or (Current == Player['Sidehand']) or(Current == Player['Extra'])):
                        EXTRATEXT.append(" Go back(1), Trash(2), Unequip(3).")
                    else:
                        EXTRATEXT.append(" Go back(1), Trash(2), Equip(3).")
                else:
                    EXTRATEXT.append(" Go back(1), Trash(2).")
                
            return('Inv')



        
    elif TP == "Mag":
        T = True
        while T:
            #['Placeholder',Min,Max,tar_eff,O_eff,Shottype,name()]
            if option == 999:
                EXTRATEXT = ['',' Your Known Magic : Hit 0 to Leave']
                Notdone = True
                a = 0
                
                while Notdone:
                    fx = ''
                    for b in range(4):
                        try:
                            fx = (fx + ' ' + str(Player['KnownSpells'][a+b][6]) + '('+str(a+b+1)+'),')
                            #print(Spells[Player['KnownSpells'][a+b]][6])
                        except:
                            try:
                                fx = (fx + ' ' + str(Player['KnownSpells'][a+b]) + '('+str(a+b+1)+'),')
                            except:
                                Notdone = False
                                break
                    EXTRATEXT.append(fx)
                    a += 4
            elif option == 0:
                return('End')
            elif CurrentI != 'None':
                if option == 1:
                    Current = 'None'
                    return('999')
                elif option == 2:
                    #print(Player['Loot'][Current])
                    Player['KnownSpells'].remove(CurrentI)
                    Current = 'None'
                    return('999')
                elif option == 3:
                    if CurrentI in Player['Spells']:
                        Player['Spells'].remove(CurrentI)
                    else:
                        if len(Player['Spells']) > 2:
                            Player['Spells'][0] = CurrentI
                        else:
                            Player['Spells'].append(CurrentI)
                    Current = 'None'
                    return('999')
                        
            else:
                EXTRATEXT = ['']
                try:
                    Spell = Spells[Player['KnownSpells'][option-1]]
                    EXTRATEXT.append(' %s' % (Player['KnownSpells'][option-1]))
                except:
                    Spell = Player['KnownSpells'][option-1]
                    EXTRATEXT.append(' %s' % (Player['KnownSpells'][option-1][6]))
                    #['Placeholder',Min,Max,tar_eff,O_eff,Shottype,name()]
                    
                Current = Spell#Item
                
                EXTRATEXT.append(" It is %s." % (Spell[0]))
                #EXTRATEXT.append(" It's a %s item." % (Item[2]))
                if Spell[1] >= 0:
                    EXTRATEXT.append(" It's max dmg is %s." % (Spell[2]))
                    EXTRATEXT.append(" It's min dmg is %s." % (Spell[1]))
                    if len(Spell[3]) > 1:
                        l = ''
                        for a in Spell[3]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It does %son hit." % (l))
                    if len(Spell[4]) > 1:
                        l = ''
                        for a in Spell[4]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It gives %son use." % (l))
                    EXTRATEXT.append(" It has a %s shot." % (Spell[5]))
                elif Spell[1] < 0:
                    EXTRATEXT.append(" It's max heal is %s." % (abs(Spell[1])))
                    EXTRATEXT.append(" It's min heal is %s." % (abs(Spell[2])))
##                    if len(Spell[3]) > 1:
##                        l = ''
##                          for a in Spell[3]:
##                          if a == 'NA':
##                                break
##                            l = l + a
##                        EXTRATEXT.append(" It does %s on hit." % (l))
                    if len(Spell[4]) > 1:
                        l = ''
                        for a in Spell[4]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It gives %son use." % (l))
                        
                    #EXTRATEXT.append(" It has a %s shot." % (Spell[5]))
                if Spell in Player['Spells']:
                    EXTRATEXT.append(" Go back(1), Forget(2), Unequip(3).")
                else:
                     EXTRATEXT.append(" Go back(1), Forget(2), Equip(3).")
        
            return('Mag')
        
    elif TP == "Play":
        global Loadbearing
        Use = [['Incresse Max Health & ','Incresse Max Strain & ', 'Gain a random spell & '],['Resistance','Dodge','gain another random spell']]
        #Up = ['Incresse Max Health and Resistance(1)','Incresse Max Strain and Dodge(2)','gain 2 random spells(3)']
        #Pirks - Greedy(enemys always give a coin), Leach(heal 1 from a phis hit),  
        T = True
        while T:
            #['Explination','Name',Pos_effects,Negeffects,visual?]
            if option == 999:
                EXTRATEXT = ['',(' Caricter Level %s : Hit 0 to Leave' % (Player['LvL']))]
                Notdone = True
                a = 0
                while Notdone:
                    fx = ' Active Spells: '
                    if len(Player['Spells']) > 0:
                        #print(Player['Spells'])
                        for b in range(4):
                            try:
                                print(Player['Spells'][a+b][1])
                                if Player['Spells'][a+b] in SideHandSpells:
                                    fx = (fx + ' ' + str(Player['Spells'][a+b]) +',')
                                else:
                                    fx = (fx + ' ' + str(Player['Spells'][a+b][6]) +',')
                                #print(Spells[Player['KnownSpells'][a+b]][6])
                            except:
                                try:
                                    fx = (fx + ' ' + str(Player['Spells'][a+b][6]) +',')
                                except:
                                    Notdone = False
                                #try:
                                #    fx = (fx + ' ' + str(Player['Spells'][a+b]) + ',')
                                #except:
                                #    Notdone = False
                                #    break
                    else:
                        fx = fx + ' None'
                        Notdone = False
                    EXTRATEXT.append(fx)
                    a += 4
                EXTRATEXT.append(' Max Health: %s, Max Damdge: %s' % ((Player['MaxHp'] + (Player['Permeffects']['HpBoost']*4),(Player['MaxP'] + Player['Permeffects']['Damage']))))
                EXTRATEXT.append(' Dodge Chance: %s, Armor: %s' % ((Player['STDodge']-40 + (Player['Permeffects']['Dodge']*5)),(Player['Resistor']+ Player['Permeffects']['Resistance'])))
                EXTRATEXT.append(' Max Strain: %s' % ((Player['MaxStrain']+ Player['Permeffects']['Strainmax'])))

                if Player['Xp'] >= ((Player['LvL']*Player['LvL'])*170):
                    Player['LvL'] = Player['LvL'] + 1
                    Player['MaxP'] = Player['MaxP'] + 1
                    Player['MaxStrain'] = Player['MaxStrain'] + 1
                    Up = [(Use[0][random.randrange(0,len(Use[0]))]+Use[1][random.randrange(0,len(Use[1]))]),(Use[0][random.randrange(0,len(Use[0]))]+Use[1][random.randrange(0,len(Use[1]))]),(Use[0][random.randrange(0,len(Use[0]))]+Use[1][random.randrange(0,len(Use[1]))])]
                    #print(Player['LvL'])
                    EXTRATEXT.append(' You Leveled up!')
                    EXTRATEXT.append(' %s(1)' % (Up[0]))
                    EXTRATEXT.append(' %s(2)' % (Up[1]))
                    EXTRATEXT.append(' Or %s(3)' % (Up[2]))
                    Loadbearing = True
            elif option == 0:
                return('End')
            elif CurrentI != 'None':
                if option == 1:
                    Current = 'None'
                    return('999')
                elif option == 2:
                    #print(Player['Loot'][Current])
                    Player['KnownSpells'].remove(CurrentI)
                    Current = 'None'
                    return('999')
            else:
                EXTRATEXT = ['']
                try:
                    T = Up[option-1]
                except:
                    break
                    #['Placeholder',Min,Max,tar_eff,O_eff,Shottype,name()]
                    
                #Current = Spell#Item
                if Loadbearing != False:
                    if 'Health' in T:
                        Player['MaxHp'] = Player['MaxHp'] + 4
                    if 'Resistance' in T:
                        Player['Resistor'] = Player['Resistor'] + 1
                    if 'Strain' in T:
                        Player['MaxStrain'] = Player['MaxStrain'] + 1
                    if 'Dodge' in T:
                        Player['STDodge'] = Player['STDodge'] + 5
                    if 'another random spell' in T:
                        Player['KnownSpells'].append(TempSpells('E'))
                    if 'random spell &' in T:
                        Player['KnownSpells'].append(TempSpells('E'))
                    
                    Loadbearing = False
                return('999')
            return('Play')
            #'''
    elif TP == 'ShopSell':
        # 1: Go back, 2: Sell one 3: Sell all 
        T = True
        while T:
            #EXTRATEXT = ['',' Your Invintory : Hit 0 to Leave']
            if option == 999:
                EXTRATEXT = ['',' Current Invintory : Hit 0 to go back', (' You have %s Coins : They have %s Coins' % (Player['Coin'],Shop['CurCoin']))]
                Notdone = True
                a = 0
                if Shop['CurCoin'] <= 0:
                    EXTRATEXT.append(" I can't buy anymore from you.")
                    EXTRATEXT.append(" Hit 0 to go back.")
                    Notdone = True
                    
                while Notdone:
                    fx = ''
                    for b in range(4):
                        try:
                            fx = (fx + ' ' + str(stuff[a+b]) + '('+str(a+b+1)+'),')
                        except:
                            Notdone = False
                            break
                    EXTRATEXT.append(fx)
                    a += 4
            elif option == 0:
                return('End')
            elif CurrentI != 'None':
                if option == 1:
                    Current = 'None'
                    return('999')
                elif option == 2:
                    #print(Player['Loot'][Current])
                    if Shop['CurCoin'] < Shop['Shopcosts'][Current]:
                        return('999')
                    Player['Loot'][Current] -= 1
                    try:
                        Shop['Loot'][Current] += 1
                    except:
                        Shop['Loot'][Current] = 0
                    Player['Coin'] += Shop['Shopcosts'][Current]
                    Shop['CurCoin'] -= Shop['Shopcosts'][Current]
                    Current = 'None'
                    return('999')
                    
                elif option == 3:
                    if Shop['CurCoin'] < Shop['Shopcosts'][Current]*Player['Loot'][Current]:
                        return('999')
                    Player['Coin'] += Shop['Shopcosts'][Current]*Player['Loot'][Current]
                    Shop['CurCoin'] -= Shop['Shopcosts'][Current]*Player['Loot'][Current]
                    Shop['Loot'][Current] = Player['Loot'][Current] 
                    Player['Loot'][Current] = 0
                    Current = 'None'
                    return('999')
                            
            else:
                Current = stuff[option-1]#Item
                try:
                    Item = Items[Current]
                except:
                    Item = Player['Loot'][Current]
                    print(Item)
                    #Item = Player['Loot']["Name"]
                    
                
                EXTRATEXT = ['']
                EXTRATEXT.append(' %s: You have %s of them.' % (Current,Player['Loot'][Current]))
                EXTRATEXT.append(" It sells for %s coins." % (Shop['Shopcosts'][Current]))
                if Shop['CurCoin'] < Shop['Shopcosts'][Current]:
                        EXTRATEXT.append(" They can't buy any.")
                EXTRATEXT.append(" It is %s." % (Item[0]))
                EXTRATEXT.append(" It's a %s item." % (Item[2]))
                if 'Main' in Item[2]:
                    EXTRATEXT.append(" It's max bonus dmg is %s." % (Item[3]))
                    if len(Item[4]) > 1:
                        l = ''
                        for a in Item[4]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It does %son hit." % (l))
                    if len(Item[5]) > 1:
                        l = ''
                        for a in Item[5]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It gives %s on equip." % (l))
                elif 'Side' in Item[2]:
                    EXTRATEXT.append(" It gives: Resistance %s" % (Item[3]['Resistance']))
                    EXTRATEXT.append(" HpBoost %s: Damage %s" % (Item[3]['HpBoost'],Item[3]['Damage']))
                    EXTRATEXT.append(" Dodge %s: Strain %s" % (Item[3]['Dodge'],Item[3]['Strainmax']))
                    if len(Item[4]) > 1:
                        l = ''
                        for a in Item[4]:
                            if a == 'NA':
                                break
                            l = l + a + ' '
                        EXTRATEXT.append(" It gives %s spells on equip." % (l))
                    #try:
                        #EXTRATEXT.append(" It gives %s minon type." % (Item[5]))
                    #except:
                    #    pass
                elif 'Extra' in Item[2]:
                    l = ''
                    for a in Item[3]:
                        if a == 'NA':
                            a = 'nothing'
                        l = l + a + ' '
                    EXTRATEXT.append(" It gives %son equip." % (l))
                    l = ''
                    for a in Item[4]:
                        if a == 'NA':
                            a = 'nothing'
                        l = l + a + ' '
                    EXTRATEXT.append(" It gives %s spells on equip." % (l))

                if Shop['CurCoin'] < Shop['Shopcosts'][Current]:
                    EXTRATEXT.append(" Go back(1).")
                elif Shop['CurCoin'] < Shop['Shopcosts'][Current]*Player['Loot'][Current]:
                    EXTRATEXT.append(" Go back(1), Sell one(2).")
                else:
                    EXTRATEXT.append(" Go back(1), Sell one(2), Sell all(3).")
                
            return('Inv')

    elif TP == 'ShopBuy':
        # 1: Go back, 2: Sell one 3: Sell all 
        T = True
        while T:
            #EXTRATEXT = ['',' Your Invintory : Hit 0 to Leave']
            if option == 999:
                EXTRATEXT = ['',' Shop Invintory : Hit 0 to go back', (' You have %s Coins : They have %s Coins' % (Player['Coin'],Shop['CurCoin']))]
                Notdone = True
                a = 0
                if Player['Coin'] <= 0:
                    EXTRATEXT.append(" You have no more cash.")
                    EXTRATEXT.append(" Hit 0 to go back.")
                    Notdone = True
                    
                while Notdone:
                    fx = ''
                    for b in range(4):
                        try:
                            fx = (fx + ' ' + str(stuff[a+b]) + '('+str(a+b+1)+'),')
                        except:
                            Notdone = False
                            break
                    EXTRATEXT.append(fx)
                    a += 4
            elif option == 0:
                return('End')
            elif CurrentI != 'None':
                if option == 1:
                    Current = 'None'
                    return('999')
                elif option == 2:
                    if Player['Coin'] < Shop['Shopcosts']:
                        return('999')
                    #print(Player['Loot'][Current])
                    try:
                        Player['Loot'][Current] += 1
                    except:
                        Player['Loot'][Current] = 1
                        
                    Shop['Loot'][Current] -= 1 
                    Player['Coin'] -= Shop['Shopcosts'][Current]
                    Shop['CurCoin'] += Shop['Shopcosts'][Current]
                    Current = 'None'
                    return('999')
                    
                elif option == 3:
                    if Player['Coin'] < Shop['Shopcosts'][Current]*Shop['Loot'][Current]:
                        return('999')
                    Player['Coin'] -= Shop['Shopcosts'][Current]*Shop['Loot'][Current]
                    Shop['CurCoin'] += Shop['Shopcosts'][Current]*Shop['Loot'][Current]
                    
                    try:
                        Player['Loot'][Current] += Shop['Loot'][Current]
                    except:
                        Player['Loot'][Current] = 0
                        Player['Loot'][Current] += Shop['Loot'][Current]
                    Shop['Loot'][Current] = 0
                    Current = 'None'
                    return('999')
                            
            else:
                Current = stuff[option-1]#Item
                try:
                    Item = Items[Current]
                except:
                    Item = Player['Loot'][Current]
                    print(Item)
                    #Item = Player['Loot']["Name"]
                    
                
                EXTRATEXT = ['']
                EXTRATEXT.append(' %s: They have %s of them.' % (Current,Shop['Loot'][Current]))
                EXTRATEXT.append(" It sells for %s coins." % (Shop['Shopcosts'][Current]))
                if Player['Coin'] < Shop['Shopcosts'][Current]:
                        EXTRATEXT.append(" You can't buy any.")
                EXTRATEXT.append(" It is %s." % (Item[0]))
                EXTRATEXT.append(" It's a %s item." % (Item[2]))
                if 'Main' in Item[2]:
                    EXTRATEXT.append(" It's max bonus dmg is %s." % (Item[3]))
                    if len(Item[4]) > 1:
                        l = ''
                        for a in Item[4]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It does %son hit." % (l))
                    if len(Item[5]) > 1:
                        l = ''
                        for a in Item[5]:
                            if a == 'NA':
                                break
                            if a in Fornow:
                                l = l + Fornow[a] + ' '
                            else:
                                l = l + a + ' '
                        EXTRATEXT.append(" It gives %s on equip." % (l))
                elif 'Side' in Item[2]:
                    EXTRATEXT.append(" It gives: Resistance %s" % (Item[3]['Resistance']))
                    EXTRATEXT.append(" HpBoost %s: Damage %s" % (Item[3]['HpBoost'],Item[3]['Damage']))
                    EXTRATEXT.append(" Dodge %s: Strain %s" % (Item[3]['Dodge'],Item[3]['Strainmax']))
                    if len(Item[4]) > 1:
                        l = ''
                        for a in Item[4]:
                            if a == 'NA':
                                break
                            l = l + a + ' '
                        EXTRATEXT.append(" It gives %s spells on equip." % (l))
                    #try:
                    #    EXTRATEXT.append(" It gives %s minon type." % (Item[5]))
                    #except:
                    #    pass
                elif 'Extra' in Item[2]:
                    l = ''
                    for a in Item[3]:
                        if a == 'NA':
                            a = 'nothing'
                        l = l + a + ' '
                    EXTRATEXT.append(" It gives %son equip." % (l))
                    l = ''
                    for a in Item[4]:
                        if a == 'NA':
                            a = 'nothing'
                        l = l + a + ' '
                    EXTRATEXT.append(" It gives %s spells on equip." % (l))
                
                if Player['Coin'] < Shop['Shopcosts'][Current]*Shop['Loot'][Current]:
                    EXTRATEXT.append(" Go back(1), Buy one(2).")
                elif Player['Coin'] < Shop['Shopcosts'][Current]:
                    EXTRATEXT.append(" Go back(1).")
                else:
                    EXTRATEXT.append(" Go back(1), Buy one(2), Buy all(3).")
                
            return('Inv')
    


def invin(Target):
    stuff = []
    for s in Target['Loot']:
        if Target['Loot'][s] != 0:
            stuff.append(s)
    return(stuff)

    
def Invintory(Player,Back,Type,Shopss=[]):
    global TP
    global Shop
    TP = Type
    Shop = Shopss
    visuals(Player,Back)
    if 'Shop' in TP:
        print('S')
        return(Shop)
    return('Inv')




#Player = {"Name": 'You','Type': "Cretan\\redoneC",'Mainhand': "None",'Sidehand': 'None','Extra': 'None','LvL': 1,'Xp': 0 ,'Resistor':0,'Aflictions':[],'Loot': {},'Hp': 20,'Dodge': 50, 'Spells': [],'KnownSpells': [TempSpells(),TempSpells(),TempSpells(),TempSpells(),TempSpells(),TempSpells()],'MaxHp':20, 'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 6,'Resist':0}

#Invintory(Player,'B', 'Mag')
        #print("Hello")
        #Thread(target = achual_stuff).start()

