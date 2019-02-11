import pygame, random, time, os, threading
from threading import Thread
from Tools import *

def visuals(PLAY,BAD):
    #Bace hand at 4,13
    #C1: 5,14
    #C3: 3,12
    #Attacking 
    #Hit 2,13
    global Bturn
    global Gturn
    global Turn
    global putin
    global SPELL
    global History

    Player = PLAY
    Bad = BAD
    
    Player['Strain'] += 1
    

    pygame.init()

    clock = pygame.time.Clock()
    PlayType = Player['Type']
    wep = str('redone'+Player["MainhandLooks"].replace(' ',''))

    Badtype = Bad['Type']
    BGwep = str('redone'+Bad["Mainhand"].replace(' ',''))
    
    gameDisplay = pygame.display.set_mode((200,200))
    DIR = os.getcwd().replace("NEWTEST",'')

    try:
        Img = pygame.image.load(str(DIR + "Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        Wep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        
        BImg = pygame.image.load(str(DIR + "Image Assets\\"+ Badtype+ '0.png')).convert_alpha()
        BWep = pygame.image.load(str(DIR + "\\Image Assets\\Items\\"+ BGwep+ '.png')).convert_alpha()
    except:
        try:
            wep = str('redonePlaceholder')
            Img = pygame.image.load(str(DIR + "Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
            Wep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
            
            BImg = pygame.image.load(str(DIR + "Image Assets\\"+ Badtype+ '0.png')).convert_alpha()
            BWep = pygame.image.load(str(DIR + "\\Image Assets\\Items\\"+ BGwep+ '.png')).convert_alpha()
        except:
            BGwep = str('redonePlaceholder')
            Img = pygame.image.load(str(DIR + "Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
            Wep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        
            BImg = pygame.image.load(str(DIR + "Image Assets\\"+ Badtype+ '0.png')).convert_alpha()
            BWep = pygame.image.load(str(DIR + "\\Image Assets\\Items\\"+ BGwep+ '.png')).convert_alpha()           
        #print("IS BROKE!")
        #BREAK_THIS_NOW
        
    try:
        Back = pygame.image.load(str(DIR + "Image Assets\\Background\\redoneBackgroundForest.png")).convert_alpha()
        Shot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\redoneNone.png")).convert_alpha()
        BShot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\redoneNone.png")).convert_alpha()
    except:
        print("IS BROKE!")
        BREAK_THIS_NOW


    display_width = Back.get_width()
    display_height = Back.get_height()

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Serberux')

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    textsurface = myfont.render("", 0, (255, 100, 100))
    gameDisplay.blit(textsurface,(200,50))


    M = False
    x = 0
    y = 0
    Spells = False
    SPELL = 'redoneNone'
    History = []

    achual_stuff(3,Player,Bad)
    while Turn != 4:
        events = pygame.event.get()       
        for event in events:
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    Spells = achual_stuff(4,Player,Bad,Spells)
                elif event.key == pygame.K_1:
                    Spells = achual_stuff(1,Player,Bad,Spells)
                elif event.key == pygame.K_2:
                    Spells = achual_stuff(2,Player,Bad,Spells)
                elif event.key == pygame.K_RETURN:
                    Spells = achual_stuff(3,Player,Bad)
                elif event.key == pygame.K_LEFT:
                    Player['AITYPE'] = 'Tactical'
                    Spells = achual_stuff('PAI',Player,Bad)
                elif event.key == pygame.K_DOWN:
                    pygame.quit()
                    quit()
            elif pygame.mouse.get_pressed()[0] == True:
                if (((pygame.mouse.get_pos()[0] > 310) and (pygame.mouse.get_pos()[0] < 350)) and ((pygame.mouse.get_pos()[1] > 115) and (pygame.mouse.get_pos()[1] < 150))):
                    #print(1)
                    Spells = achual_stuff(1,Player,Bad,Spells)
                elif (((pygame.mouse.get_pos()[0] > 370) and (pygame.mouse.get_pos()[0] < 410)) and ((pygame.mouse.get_pos()[1] > 115) and (pygame.mouse.get_pos()[1] < 150))):
                    #print(2)
                    Spells = achual_stuff(2,Player,Bad,Spells)
                elif (((pygame.mouse.get_pos()[0] > 430) and (pygame.mouse.get_pos()[0] < 470)) and ((pygame.mouse.get_pos()[1] > 115) and (pygame.mouse.get_pos()[1] < 150))):
                    #print(3)
                    Spells = achual_stuff(4,Player,Bad,Spells)
                elif (((pygame.mouse.get_pos()[0] > 340) and (pygame.mouse.get_pos()[0] < 425)) and ((pygame.mouse.get_pos()[1] > 155) and (pygame.mouse.get_pos()[1] < 200))):
                    #print("Done")
                    Spells = achual_stuff(3,Player,Bad)
            else:
                pass

        #0,1,2,3,4,?,A,M
        Goodpl = [[20,85],[25,90],[20,85],[15,80],[15,80],[170,110],[10,85]]
        Badpl = [[690,70],[695,65],[700,60],[695,65],[700,60],[530,90],[705,65]]
        
        gameDisplay.blit(Back, (0,0))
        
        gameDisplay.blit(Img, (0,20))
        gameDisplay.blit(Wep, (Goodpl[int(x)][0],Goodpl[int(x)][1]))
        
        gameDisplay.blit(pygame.transform.flip(BImg,True,False), (615,0))
        gameDisplay.blit(pygame.transform.flip(BWep,True,False), (Badpl[int(y)][0],Badpl[int(y)][1]))
        
        gameDisplay.blit(pygame.transform.flip(Shot,True,False), (600,100))
        gameDisplay.blit(BShot, (85,120))

        for a in range(4):
            try:
                textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-(1+a)]), 0, (0,0,0))
                gameDisplay.blit(textsurface,(215,(5+(a*25))))
            except:
                pass

        b = 0
        for a in range(len(Player['Aflictions'])):
            try:
                Affectimg = pygame.image.load(str(DIR + "Image Assets\\Effects\\redone"+Player['Aflictions'][a]+'.png')).convert_alpha()
                gameDisplay.blit(Affectimg, (205,(120+b*30)))
                b += 1
            except:
                pass
            

        b = 0
        for a in range(len(Bad['Aflictions'])):
            try:
                Affectimg = pygame.image.load(str(DIR + "Image Assets\\Effects\\redone"+Bad['Aflictions'][a]+'.png')).convert_alpha()
                gameDisplay.blit(Affectimg, (570,(120+b*30)))
                b += 1
            except:
                pass

        pygame.display.update()
        clock.tick(60)
        
        
        x += .04 
        if x > 4:
            x = 0
        y += .04 
        if y > 4:
            y = 0

        if M:
            #BREAK
            time.sleep(1)
            x = 0
            y = 0
            Bturn = ""
            Gturn = ""
            M = False
        #"""
        TYPES = ['PHit', 'PMiss', 'MHit', 'MMiss'] #,'Heal', 'Broke'
        #[Gtype,Btype,Bwep,x,y, Shottype]
        Bturnstuff = [['Hit.png','PAttack.png','PAttack.png',6,5,(BGwep + "blast.png")],['Miss.png','PAttack.png','PAttack.png',0,5,(BGwep + "blast.png")],['Hit.png','MAttack.png','.png',6,0,('redone' + SPELL + "blast.png")],['Miss.png','MAttack.png','.png',0,0,('redone' + SPELL + "blast.png")]]
        Gturnstuff = [['Hit.png','PAttack.png','PAttack.png',5,6,(wep + "blast.png")],['Miss.png','PAttack.png','PAttack.png',5,0,(wep + "blast.png")],['Hit.png','MAttack.png','.png',0,6,('redone' + SPELL + "blast.png")],['Miss.png','MAttack.png','.png',0,0,('redone' + SPELL + "blast.png")]]

        #When a summon is active it drains 1 strain per tern
        
        
        if Gturn != '':
            History.append(str('G'+Gturn))
            if Gturn not in TYPES:
                Gturn = ''
            for a in range(len(TYPES)):
                if TYPES[a] in Gturn:
                    Bwep = '.png'
                    BShottype = "redoneNone.png"
                    M = True
                    
                    BType = Gturnstuff[a][0]
                    GType = Gturnstuff[a][1]

                    Gwep = Gturnstuff[a][2]
                    Shottype = Gturnstuff[a][5]
                    
                    x = Gturnstuff[a][3]
                    y = Gturnstuff[a][4]

        if Bturn != '':
            History.append(str('B'+Bturn))
            if Bturn not in TYPES:
                Bturn = ''
            for a in range(len(TYPES)):
                if TYPES[a] in Bturn:
                    Gwep = '.png'
                    Shottype = "redoneNone.png"
                    M = True
                    
                    GType = Bturnstuff[a][0]
                    BType = Bturnstuff[a][1]

                    Bwep = Bturnstuff[a][2]
                    BShottype = Bturnstuff[a][5]
                    
                    x = Bturnstuff[a][3]
                    y = Bturnstuff[a][4]
                    
        if M != True:
            GType = str(int(x))+'.png'
            BType = str(int(x))+'.png'
            Gwep = ".png"
            Bwep = ".png"
            Shottype = "redoneNone.png"
            BShottype = "redoneNone.png"

        try:
            #wep = str('redone'+Player["Mainhand"].replace(' ',''))
            Img = pygame.image.load(str(DIR + "Image Assets\\"+PlayType+GType)).convert_alpha()
            Wep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()
            Shot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\"+ Shottype)).convert_alpha()
            
            BImg = pygame.image.load(str(DIR + "Image Assets\\"+Badtype+BType)).convert_alpha()
            BWep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ BGwep+ Bwep)).convert_alpha()
            BShot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\"+ BShottype)).convert_alpha()
        except:
            print("IS BROKE")
            BREAK_ME_NOW
            
    time.sleep(2)


def achual_stuff(putin,Play,Bad,more = False):
    global Bturn
    global Gturn
    global Turn
    global EXTRATEXT
    play = Play['Hp']
    playrole = Play['Dodge']
    bad = Bad['Hp']
    badrole = Bad['Dodge']
    dg = 0
    bdg = 0
    Fornow = {'Fire':'Ablaze','Stun':'Stuned','Weak':'Weakend','Regenerate':'Regenerating','Bleed':'Bleeding','NA':'','':''}
    #while (bad > 0) and (play >0) and (Turn != 4):
        #print("Tick A")
    #while len(EXTRATEXT) > 4:
    if bad <=0:
        EXTRATEXT.append('You Won!')
        Turn = 4
        return(False)
    elif play <= 0:
        EXTRATEXT.append('You Lost!')
        Turn = 4
        return(False)
    
    for a in range(6):
        try:
            EXTRATEXT.remove(EXTRATEXT[0])
        except:
            pass
    
    #print(events)
    #try:
    AFLICT(Bad,Play)
    AFLICT(Play,Bad)
    if Turn > 0:
        if putin == 'PAI':
            if Play['Strain']<= 0:
                Play['Aflictions'].append('StrainedB')
            Play['Dodge'] = Play['STDodge'] + (Play['Permeffects']['Dodge']*5)
            if Play['Hp'] < ((Play['MaxHp']+ (Play['Permeffects']['HpBoost']*4))/4):
                Play['Dodge'] = Play['STDodge'] + 20 + (Play['Permeffects']['Dodge']*5)
            Play['Resist'] = Play['Resistor'] + Play['Permeffects']['Resistance']
            #Bad
            EXTRATEXT.append(" ")
            EXTRATEXT.append("Your Turn")

            try:
                GAI = AI(Play,Bad)
            except:
                GAI = AI(Play,Bad)
                print("?")
            
            if GAI == 'Dodge':
                Play['Resist'] = 10000
                Play["Strain"] += 1
                if Play["Strain"] > Play["MaxStrain"]+Play['Permeffects']['Strainmax']:
                        Play["Strain"] = Play["MaxStrain"] + Play['Permeffects']['Strainmax']
                        
                EXTRATEXT.append(("You are blocking."))
                #Bturn = 'None'
                EXTRATEXT.append("Hit Enter to continue.")
                Gturn = 'Block'
            elif GAI == "Attack":
                Gturn = DAMAGE(Play,Bad,"P")
                Play["Strain"] -= 1
                if 'Hit' in Gturn:
                    words = ''
                    for a in Play['HitEffects']:
                        if a != 'NA':
                            if a in Fornow:
                                words = words + ' ' + Fornow[a]
                            else:
                                words = words + ' ' + a
                            Bad['Aflictions'].append(a)
                    if len(Play['HitEffects']) > 1:
                        EXTRATEXT.append('%s are%s' % (Bad['Name'],words))
                EXTRATEXT.append("Hit Enter to continue.")
            else:
                Gturn = Use_Spell(GAI,Play,Bad)
                #print(Bturn)
            Turn = -2
        else:
            
            if more != True:
                extra = '.'
                if Play['Strain']<= 0:
                    #print(Play['Strain'])
                    Play['Aflictions'].append('StrainedB')
                    extra = " : You are Strained."
                    Play['Strain'] = 0
                else:
                    extra = (' : %s/%s Strain' % (Play['Strain'],(Play['MaxStrain']+Play['Permeffects']['Strainmax'])))
                    
                Play['Dodge'] = Play['STDodge'] + (Play['Permeffects']['Dodge']*5)
                if Play['Hp'] < ((Play['MaxHp']+ (Play['Permeffects']['HpBoost']*4))/4):
                    Play['Dodge'] = Play['STDodge'] + 20 + (Play['Permeffects']['Dodge']*5)
                Play['Resist'] = Play['Resistor'] + Play['Permeffects']['Resistance']
                
                #Player
                EXTRATEXT.append("Your turn.")
                EXTRATEXT.append(("Hp: %s%s"% (play,extra)))
                EXTRATEXT.append(("%s damage delt." % (Bad['MaxHp']-Bad['Hp'])))
                EXTRATEXT.append("Attack(1),Block(2),Misc(3):")
                
                if int(putin) == 3:
                    #For updates
                    pass
                elif int(putin) == 4:
                    #Spells
                    for a in range(4):
                        EXTRATEXT.append(" ")
                    Notdone = True
                    a = 0
                    while Notdone:
                        fx = ''
                        for b in range(3):

                            try:
                                #print(type(Play['Spells'][a+b]))
                                if type(Play['Spells'][a+b]) != list:
                                    fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                else:
                                    fx = (fx + ' ' + str(Play['Spells'][a+b][6]) + '('+str(a+b+1)+')')
                            except:
                                Notdone = False
                        EXTRATEXT.append(fx)
                        a += 4
                    
                    EXTRATEXT.append("You can do:")
                    EXTRATEXT.append("Hit Enter go back.")
                    return(True)
                    
                elif int(putin) == 1:
                    for a in range(4):
                        EXTRATEXT.append(" ")
                    Gturn = DAMAGE(Play,Bad,"P")
                    Play["Strain"] -= 1
                    if 'Hit' in Gturn:
                        words = ''
                        for a in Play['HitEffects']:
                            if a != 'NA':
                                if a in Fornow:
                                    words = words + ' ' + Fornow[a]
                                else:
                                    words = words + ' ' + a
                                Bad['Aflictions'].append(a)
                        if len(Play['HitEffects']) > 1:
                            EXTRATEXT.append('%s are%s' % (Bad['Name'],words))
                    Turn = -2
                    EXTRATEXT.append("Hit Enter to continue.")
                    
                else:
                    Play['Resist'] = 10000
                    Play["Strain"] += 1
                    if Play["Strain"] > Play["MaxStrain"]+Play['Permeffects']['Strainmax']:
                        Play["Strain"] = Play["MaxStrain"] + Play['Permeffects']['Strainmax']
                    Gturn = 'Block'    
                        
                    Turn = -2
                    EXTRATEXT.append("Hit Enter to continue.")
                
            else:
                if int(putin) == 3:
                    pass
                elif int(putin) == 4:
                    #try:
                    Gturn = Use_Spell(Play['Spells'][2],Play,Bad)
                    Turn = -2
                    #except:
                    """
                    Notdone = True
                    a = 0
                    while Notdone:
                        fx = ''
                        for b in range(3):
                            try:
                                #print(type(Play['Spells'][a+b]))
                                if type(Play['Spells'][a+b]) != list:
                                    fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                else:
                                    fx = (fx + ' ' + str(Play['Spells'][a+b][6]) + '('+str(a+b+1)+')')
                            except:
                                Notdone = False
                        EXTRATEXT.append(fx)
                        a += 4
                    EXTRATEXT.append("You can do:")
                    return(True)
                    """
                        
                elif int(putin) == 1:
                    try:
                        Gturn = Use_Spell(Play['Spells'][0],Play,Bad)
                        Turn = -2
                    except:
                        Notdone = True
                        a = 0
                        while Notdone:
                            fx = ''
                            for b in range(3):

                                try:
                                    #print(type(Play['Spells'][a+b]))
                                    if type(Play['Spells'][a+b]) != list:
                                        fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                    else:
                                        fx = (fx + ' ' + str(Play['Spells'][a+b][6]) + '('+str(a+b+1)+')')
                                except:
                                    Notdone = False
                            EXTRATEXT.append(fx)
                            a += 4
                        EXTRATEXT.append("You can do:")
                        return(True)
                else:
                    try:
                        Gturn = Use_Spell(Play['Spells'][1],Play,Bad)
                        Turn = -2
                    except:
                        Notdone = True
                        a = 0
                        while Notdone:
                            fx = ''
                            for b in range(3):

                                try:
                                    if type(Play['Spells'][a+b]) != list:
                                        fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                    else:
                                        fx = (fx + ' ' + str(Play['Spells'][a+b][6]) + '('+str(a+b+1)+')')
                                except:
                                    Notdone = False
                            EXTRATEXT.append(fx)
                            a += 4
                        EXTRATEXT.append("You can do:")
                        return(True)
            #AFLICT(Play,Bad)

    else:
        if Bad['Strain']<= 0:
            Bad['Aflictions'].append('StrainedB')
        #AFLICT(Play,Bad)
        #AFLICT(Bad,Play)
        Bad['Dodge'] = Bad['STDodge']
        Bad['Resist'] = Bad['Resistor']
        #Bad
        EXTRATEXT.append(" ")
        EXTRATEXT.append("Enemy's Turn")

        try:
            BADAI = AI(Bad,Play)
        except:
            BADAI = AI(Bad,Play)
            print("?")
        
        if BADAI == 'Dodge':
            Bad['Resist'] = 10000
            Bad["Strain"] += 1
            if Bad["Strain"] > Bad["MaxStrain"]:
                Bad["Strain"] = Bad["MaxStrain"]
                    
            EXTRATEXT.append(("%s are blocking." % (Bad["Name"])))
            #Bturn = 'None'
            EXTRATEXT.append("Hit Enter to continue.")
            Bturn = 'Block'
        elif BADAI == "Attack":
            Bturn = DAMAGE(Bad,Play,"P")
            Bad["Strain"] -= 1
            if 'Hit' in Bturn:
                words = ''
                for a in Bad['HitEffects']:
                    if a != 'NA':
                        if a in Fornow:
                            words = words + ' ' + Fornow[a]
                        else:
                            words = words + ' ' + a
                        Play['Aflictions'].append(a)
                if len(Bad['HitEffects']) > 0:
                    EXTRATEXT.append('%s are%s' % (Play['Name'],words))
            EXTRATEXT.append("Hit Enter to continue.")
        else:
            Bturn = Use_Spell(BADAI,Bad,Play)
            #print(Bturn)
        Turn = Turn*-1
        #AFLICT(Bad,Play)
    
    #except:
    #    pass
    '''if bad <=0:
        EXTRATEXT.append('You Won!')
        Turn = 4
    elif play <= 0:
        EXTRATEXT.append('You Lost!')
        Turn = 4'''
    return(False)
    time.sleep(.05)


    


def AI(Owner,Target):
    Spells = load("Spells")
    #print(History)
    #End goal is that it learns.
    #required info
    #Owner['Dodge'] Owner['Hp'] Owner['MaxHp']
    #Owner['Spells'] *Owner['Aflictions']*
    #Owner['MaxStrain'] Owner['Strain']
    if ((Owner['MaxHp']+ (Owner['Permeffects']['HpBoost']*4))/random.randrange(5,7)) > Owner['Hp']:
        if random.randrange(0,2):
            return("Dodge")
        elif random.randrange(0,2):
            for spell in Owner['Spells']:
                #print(spell)
                try:
                    if Spells[spell][1] < 0:
                        return(spell)
                except:
                    if spell[1] < 0:
                        return(spell)
        else:
            if random.randrange(0,2):
                return("Attack")
            else:
                for spell in Owner['Spells']:
                    try:
                        if Spells[spell][1] >= 0:
                            return(spell)
                    except:
                        if spell[1] >= 0:
                            return(spell)
                        
    if Owner['AITYPE'] == 'Rush':
        if Owner['Strain'] > Owner['MaxStrain']/4:
            if random.randrange(0,2):
                return("Attack")
            else:
                for spell in Owner['Spells']:
                    try:
                        if Spells[spell][1] >= 0:
                            return(spell)
                    except:
                        if spell[1] >= 0:
                            return(spell)
                        
    elif Owner['AITYPE'] == 'Run':
        if Owner['Strain'] > Owner['MaxStrain']/4:
            if random.randrange(0,3):
                return("Attack")
            elif random.randrange(0,3):
                for spell in Owner['Spells']:
                    try:
                        if Spells[spell][1] >= 0:
                            return(spell)
                    except:
                        if spell[1] >= 0:
                            return(spell)
                        
    elif Owner['AITYPE'] == 'Tactical':
        #if 'GPHit' in History[len(History)]:
        #    pass
        #if 'GMHit' in History[len(History)]:
        #    pass
        try:
            lastmove = History[len(History)-1]
        except:
            lastmove = 'Block'
        #print(lastmove)
        #if Owner['Strain'] > int((Owner['MaxStrain']+Owner['Permeffects']['Strainmax'])/8):
        #    pass
        if ('Miss' in lastmove):
            if random.randrange(0,2):
                return("Attack")
            else:
                for spell in Owner['Spells']:
                    try:
                        if Spells[spell][1] >= 0:
                            return(spell)
                    except:
                        if spell[1] >= 0:
                            return(spell)
                        
        elif 'Heal' in lastmove:
            if random.randrange(0,2):
                return("Attack")
            else:
                for spell in Owner['Spells']:
                    try:
                        if Spells[spell][1] >= 0:
                            return(spell)
                    except:
                        if spell[1] >= 0:
                            return(spell)
                        
        elif 'Block' in lastmove:
            if Owner['Strain'] > (Owner['MaxStrain']+Owner['Permeffects']['Strainmax'])/4:
                if random.randrange(0,4):
                    return("Attack")
                elif random.randrange(0,4):
                    for spell in Owner['Spells']:
                        try:
                            if Spells[spell][1] >= 0:
                                return(spell)
                        except:
                            if spell[1] >= 0:
                                return(spell)
                        
    else:
        #Random
        if Owner['Strain'] > Owner['MaxStrain']/4:
            if random.randrange(0,2):
                return("Attack")
            elif random.randrange(0,2):
                for spell in Owner['Spells']:
                    try:
                        if Spells[spell][1] >= 0:
                            return(spell)
                    except:
                        if spell[1] >= 0:
                            return(spell)
                        
    
##        else:
##            if random.randrange(1,3) == 1:
##                return("Attack")
##            else:
##                for spell in Owner['Spells']:
##                    try:
##                        if Spells[spell][1] >= 0:
##                            return(spell)
##                    except:
##                        if spell[1] >= 0:
##                            return(spell)
##    else:
##        if random.randrange(1,3) == 1:
##            if random.randrange(1,3) == 1:
##                return("Attack")
##            else:
##                for spell in Owner['Spells']:
##                    try:
##                        if Spells[spell][1] >= 0:
##                            return(spell)
##                    except:
##                        if spell[1] >= 0:
##                            return(spell)
##                return("Attack")
        
    return("Dodge")



        

def Use_Spell(spell,Owner,Target):
    global SPELL
    global EXTRATEXT
    for a in range(4):
        EXTRATEXT.append(" ")
    Spells = load("Spells")
    try:
        spell = Spells[spell]
    except:
        #print(Owner)
        pass
    SPELL = spell[5]
    #print(SPELL)
    #['Def', Min, Max, [Target efects], [Owner efects],'Shottype']
    Fornow = {'Fire':'Ablaze','Stun':'Stuned','Weak':'Weakend','Regenerate':'Regenerating','Bleed':'Bleeding','NA':'','':''}
    if spell[2] > 0:
        dmg = random.randrange(spell[1],spell[2])+int((Owner['MaxStrain']+Owner['Permeffects']['Strainmax'])/4)
        turn = DAMAGE(Owner,Target,'M',dmg)
        if 'Miss' not in turn:
            #spell[4].remove('')
            #spell[4].remove('NA')
            words = ''
            #EXTRATEXT.append("%s are affected with %s" % (Target['Name'],spell[3][0]))
            for a in spell[3]:
                if a in Fornow:
                    if a == 'NA':
                        break
                    words = (words + ' ' + str(Fornow[a]))
                else:
                    words = words + ' ' + a
                Target['Aflictions'].append(a)
            if len(spell[3]) > 1:
                EXTRATEXT.append('%s are%s' % (Target['Name'],words))
                
        
    elif spell[2] <= 0:
        ran = abs(random.randrange(spell[1],spell[2]))+Owner['MaxStrain']-4+Owner['Permeffects']['Strainmax']
        EXTRATEXT.append("%s Healed for %s!" % (Owner["Name"],ran))
        Owner['Hp'] += ran
        if Owner['Hp'] > (Owner['MaxHp'] + (Owner['Permeffects']['HpBoost']*4)):
            Owner['Hp'] = (Owner['MaxHp'] + (Owner['Permeffects']['HpBoost']*4))
            EXTRATEXT.append("%s are at Max health!" % (Owner["Name"]))
        turn = "Heal"
    else:
        EXTRATEXT.append("Is broke.")
        turn = "Broke"
        
    Owner["Strain"] -= 2
    if Owner["Strain"] < 0:
        Owner["Strain"] = 0
        
        
    words = ''
    for a in spell[4]:
        if a in Fornow:
            #print(a)
            if a == 'NA':
                break
            #print(type(Fornow[a]))
            words = words + ' ' + str(Fornow[a])
        else:
            words = words + ' ' + a
        Owner['Aflictions'].append(a)
    if len(spell[4]) > 1:
        EXTRATEXT.append('%s are%s' % (Owner['Name'],words))
        
    EXTRATEXT.append("Hit Enter to continue.")
    return(turn)



def DAMAGE(Owner,Target,Type,dmg = 'NA'):
    global EXTRATEXT
    if Target['Dodge'] >= 101:
        Target['Dodge'] = 99
    if random.randrange((Target['Dodge']-40),101) <= 80:
        if dmg != "NA":
            dmg = dmg - Target['Resist'] - Target['Permeffects']['Resistance']
        else:
            xcv = int((Owner['MaxP']+ Owner['Permeffects']['Damage'])*(Owner['Strain']/(Owner['MaxStrain']-1 + Owner['Permeffects']['Strainmax'])))+2
            if xcv >= 1:
                dmg = random.randrange(0,xcv) - Target['Resist'] - Target['Permeffects']['Resistance']
            else:
                dmg = 1
        if dmg > 0:
            EXTRATEXT.append(("%s hit for %s dmg." % (Owner["Name"],dmg)))
            Target['Hp'] -= dmg
            return(str(Type+"Hit"))
        else:
            #print('asdf')
            if random.randrange(0,4) > 0:
                EXTRATEXT.append(("%s hit for %s dmg." % (Owner["Name"],1)))
                Target['Hp'] -= 1
                return(str(Type+"Hit"))
            else:
                EXTRATEXT.append(("%s missed." % (Owner["Name"])))
        
    else:
        print(Target['Dodge']-40)
        EXTRATEXT.append(("%s missed." % (Owner["Name"])))
    return(str(Type+"Miss"))
    
    
def AFLICT(Owner,Target):
    #print("Types: Fire,Stun,Blinded,Weak,Regenerate,Shealded,Hidden")
    #['Fire','Regenerate','Hidden','Stun','Blinded','Strained','Shealded','Weak','STRAINED']
    #Bad = {'Hp': 20,'Dodge': 50,'MaxHp':20,'Strain': 4,'MaxP': 6,'Resist':0,'Resistor':0}
    #print(Owner['Aflictions'])
    #print(Owner['Strain'])
    
    dmg = ['Fire','Bleed','StrainedB']
    heal = ['Regenerate']
    dodgeup = ['Hidden']
    stun = ['Stun','Strained']
    dodgedown = ['Blinded','StrainedB']
    resistancedown = ['StrainedB']
    resistanceup = ['Shealded','StrainedB']
    dmgup = []
    dmgdown = ['Weak','StrainedB']

    while len(Owner['Aflictions']) > 0:
        afl = Owner['Aflictions'][0]
        if afl in dmg:
            #dmg = 
            Owner['Hp'] -= random.randrange(1,int(Owner['LvL']/2)+2)
        if afl in heal:
            #dmg = random.randrange(1,int(Owner['LvL']/2)+2)
            Owner['Hp'] += random.randrange(1,int(Owner['LvL']/2)+2)
        if afl in dodgeup:
            Owner['Dodge'] = Owner['Dodge'] + random.randrange(1,int(Owner['LvL']/2)+10)
        if afl in dodgedown:
            Owner['Dodge'] = Owner['Dodge'] - random.randrange(1,int(Owner['LvL']/2)+10)
        if afl in dmgdown:
            Target['Resist'] = Target['Resist'] + random.randrange(1,int(Owner['LvL']/2)+2)
        if afl in dmgup:
            Target['Resist'] = Target['Resist'] - random.randrange(1,int(Owner['LvL']/2)+2)
        if afl in stun:
            Owner['Strain'] -= 2
        if afl in resistancedown:
            Owner['Resist'] = Owner['Resist'] - random.randrange(1,int(Owner['LvL']/2)+2)
        if afl in resistanceup:
            Owner['Resist'] = Owner['Resist'] + random.randrange(1,int(Owner['LvL']/2)+2)
        Owner['Aflictions'].remove(Owner['Aflictions'][0])
        




global Bturn
global Gturn
global Turn
Turn = 2
Bturn = ''
Gturn = ''
EXTRATEXT = ["Begin",'']
events = ''
putin = ''

def Demofight(Player,BadType):
    global Bturn
    global Gturn
    global Turn
    Turn = 2
    Bturn = ''
    Gturn = ''
    EXTRATEXT = ["Begin",'']
    events = ''
    putin = ''

    Level = random.randrange(Player['LvL']-2,Player['LvL']+2)
    Bad = BadBuild(BadType,Level)
    #btypes = ["BadCretan\\redoneC","BadWarrior\\redoneC","BadWiz\\redoneC"]
    #Badtype = btypes[random.randrange(0,len(btypes))]

    #WepTypes = ["redoneSword","redoneSteelSword","redoneRoyalSword","redoneFirewand","redoneIcewand"]
    #BGwep = WepTypes[random.randrange(0,len(WepTypes))]

    #Bad = {"Name": 'They','Type': Badtype,'Mainhand': BGwep,'Hp': 5,'Dodge': 50,'MaxHp':5,'MaxStrain': 4, 'Strain': 4,'STDodge': 50 ,'MaxP': 6,'Resist':0,'Spells':[]}
    #Player = 'LvL': 1,'Xp': 0 ,'HitEffects': [],'Permeffects':{'Resistance': 0,'HpBoost':0,'Damage':0 'Dodge':0, 'Strainmax':0},'Resistor':0,'Aflictions':[],'Loot': {},'Coin': 0,'Hp': 20,'Dodge': 50, 'Spells': [],'KnownSpells': [TempSpells('C','Heal'),TempSpells('C','Dmg'),TempSpells(),TempSpells(),TempSpells(),TempSpells()],'MaxHp':20, 'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 2,'Resist':0}
    visuals(Player,Bad)
    #Player['Xp'] = Player['Xp'] + random.randrange(20,201)

    
if __name__ == '__main__':
    btypes = ["BadCretan\\redoneC","BadWarrior\\redoneC","BadWiz\\redoneC"]
    Badtype = btypes[random.randrange(0,len(btypes))]

    WepTypes = ["redoneSword","redoneSteelSword","redoneRoyalSword","redoneFirewand","redoneIcewand"]
    BGwep = WepTypes[random.randrange(0,len(WepTypes))]

    Bad = {"Name": 'They','Type': Badtype,'Mainhand': BGwep,'Hp': 20,'Dodge': 50,'MaxHp':20,'MaxStrain': 4, 'Strain': 4,'STDodge': 50 ,'MaxP': 6,'Resist':0,'Spells':[]}
    Player = {"Name": 'You','Type': "Cretan\\redoneC",'Mainhand': "redoneSteelSword",'Loot': [],'Hp': 20,'MaxHp':20,'Dodge': 50, 'Spells': ["Firebolt",'Drink'],'MaxStrain': 4, 'Strain': 4,'STDodge': 50,'MaxP': 6,'Resist':0 }

    visuals(Player,Bad)

