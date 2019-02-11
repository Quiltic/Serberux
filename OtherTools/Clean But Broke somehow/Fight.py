import pygame, random, time, os, threading
from threading import Thread
from Tools import *

def visuals(Player,Bad):
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

    pygame.init()

    clock = pygame.time.Clock()
    PlayType = Player['Type']
    wep = Player["Mainhand"]

    Badtype = Bad['Type']
    BGwep = Bad["Mainhand"]
    
    gameDisplay = pygame.display.set_mode((200,200))
    DIR = os.getcwd().replace("NEWTEST",'')
    #print(pygame.image.load(str(DIR+"Image Assets\\"+ PlayType+ '0.png')).convert_alpha())
    #Img = pygame.image.load(str("D:\\Python35-32\\Game\\Cretan\\"+ img+ '0.png')).convert_alpha()
    try:
        Img = pygame.image.load(str(DIR + "Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        Wep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        
        BImg = pygame.image.load(str(DIR + "Image Assets\\"+ Badtype+ '0.png')).convert_alpha()
        BWep = pygame.image.load(str(DIR + "\\Image Assets\\Items\\"+ BGwep+ '.png')).convert_alpha()
    except:
        print("IS BROKE!")
        BREAK_THIS_NOW
        
        #Img = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+ PlayType+ '0.png')).convert_alpha()
        #Wep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ wep+ '.png')).convert_alpha()
        
        #BImg = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+ Badtype+ '0.png')).convert_alpha()
        #BWep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ BGwep+ '.png')).convert_alpha()
        
    try:
        Back = pygame.image.load(str(DIR + "Image Assets\\Background\\redoneBackgroundD.png")).convert_alpha()
        Shot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\redoneNone.png")).convert_alpha()
        BShot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\redoneNone.png")).convert_alpha()
    except:
        print("IS BROKE!")
        BREAK_THIS_NOW
        
        #Back = pygame.image.load("E:\\Python35-32\\Game\\Image Assets\\Background\\redoneBackgroundD.png").convert_alpha()
        #Shot = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\ShotAssets\\redoneNone.png")).convert_alpha()
        #BShot = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\ShotAssets\\redoneNone.png")).convert_alpha()


    display_width = Back.get_width()
    display_height = Back.get_height()

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('player')

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render("", 0, (255, 100, 100))
    gameDisplay.blit(textsurface,(200,50))


    M = False
    x = 0
    y = 0
    Spells = False
    SPELL = 'redoneNone'

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
            else:
                pass

        """
        if Turn == -2:
            Turn = -1
            print('MNB')
            
        elif Turn <= 0:
            Turn = Turn - .25
            print('FACK')
        elif Turn  > 1:
            print("Crab")
            achual_stuff(3,Player,Bad)
            Turn = Turn - .5
        """
                
        """              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        """
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

        #matoc = 0
        #for a in range(len(EXTRATEXT)-1):
        #    matoc += 1
        #    if matoc > 3:
        #         break
        #"""
        for a in range(3):
            try:
                textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-(1+a)]), 0, (0,0,0))
                gameDisplay.blit(textsurface,(215,(10+(a*30))))
            except:
                pass
        """
        textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-1]), 0, (0,0,0))
        gameDisplay.blit(textsurface,(215,(10)))
        textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-2]), 0, (0,0,0))
        gameDisplay.blit(textsurface,(215,(40)))
        textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-3]), 0, (0,0,0))
        gameDisplay.blit(textsurface,(215,(70)))#+(a*(30))
        #"""
        
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

        #MAttack.png
        #(SPELL + "blast.png")
        #
        #
        if Gturn != '':
            
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
                    

        #"""
        """
        if "Miss" in Bturn:
            GType = 'Miss.png'
            Gwep = '.png'
            
            BType = 'PAttack.png'
            Bwep = 'PAttack.png'
            M = True
            
            x = 0
            y = 5
            BShottype = BGwep + "blast.png"
            Shottype = "redoneNone.png"
            
        elif "Hit" in Bturn:
            GType = 'Hit.png'
            Gwep = '.png'
            
            BType = 'PAttack.png'
            Bwep = 'PAttack.png'
            M = True
            x = 6
            y = 5
            BShottype = BGwep + "blast.png"
            Shottype = "redoneNone.png"
            
            
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
        #"""
        if M != True:
            GType = str(int(x))+'.png'
            BType = str(int(x))+'.png'
            Gwep = ".png"
            Bwep = ".png"
            Shottype = "redoneNone.png"
            BShottype = "redoneNone.png"

        try:
            Img = pygame.image.load(str(DIR + "Image Assets\\"+PlayType+GType)).convert_alpha()
            Wep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()
            Shot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\"+ Shottype)).convert_alpha()
            
            BImg = pygame.image.load(str(DIR + "Image Assets\\"+Badtype+BType)).convert_alpha()
            BWep = pygame.image.load(str(DIR + "Image Assets\\Items\\"+ BGwep+ Bwep)).convert_alpha()
            BShot = pygame.image.load(str(DIR + "Image Assets\\ShotAssets\\"+ BShottype)).convert_alpha()
        except:
            print("IS BROKE")
            BREAK_ME_NOW
            
            #Img = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+PlayType+GType)).convert_alpha()
            #Wep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ wep+ Gwep)).convert_alpha()
            #Shot = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\ShotAssets\\"+ Shottype)).convert_alpha()
            
            #BImg = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\"+Badtype+BType)).convert_alpha()
            #BWep = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\Items\\"+ BGwep+ Bwep)).convert_alpha()
            #BShot = pygame.image.load(str("E:\\Python35-32\\Game\\Image Assets\\ShotAssets\\"+ BShottype)).convert_alpha()

    #achual_stuff(3,Player,Bad)
    #textsurface = myfont.render(str(EXTRATEXT[len(EXTRATEXT)-(1)]), 0, (0,0,0))
    #gameDisplay.blit(textsurface,(215,(10+(a*30))))
    #pygame.display.update()
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
    #while (bad > 0) and (play >0) and (Turn != 4):
        #print("Tick A")
    #while len(EXTRATEXT) > 4:
    for a in range(6):
        try:
            EXTRATEXT.remove(EXTRATEXT[0])
        except:
            pass
    
    #print(events)
    try:
        if Turn > 0:
            if more != True:
                Play['Dodge'] = Play['STDodge']
                #Player
                EXTRATEXT.append("Your turn.")
                EXTRATEXT.append(("Hp: ", play))
                EXTRATEXT.append(((Bad['MaxHp']-Bad['Hp'])," damage delt."))
                #print("Your turn.")
                #print("Hp: ", play)
                EXTRATEXT.append("Attack(1),Dodge(2),Misc(3):")
                #inp = input("Attack(1), Dodge(2): ")

            
                if int(putin) == 3:
                    #For updates
                    pass
                elif int(putin) == 4:
                    #Spells
                    Notdone = True
                    a = 0
                    while Notdone:
                        fx = ''
                        for b in range(3):

                            try:
                                fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                #print(fx)
                            except:
                                Notdone = False
                        EXTRATEXT.append(fx)
                        a += 4
                    EXTRATEXT.append("You can do:")
                    return(True)
                    
                elif int(putin) == 1:
                    Gturn = DAMAGE(Play,Bad,"P")

                    """
                    if Bad['Dodge'] < random.randrange(0,11):
                        dmg = random.randrange(1,6)
                        EXTRATEXT.append(("You hit for %s dmg." % (dmg)))
                        Gturn = "PHit"
                        Bad['Hp'] = Bad['Hp'] -dmg
                        #Turn = Turn*-1
                        #time.sleep(1)
                    else:
                        EXTRATEXT.append("You Missed.")
                        Gturn = "PMiss"
                    """
                    Turn = -2
                    EXTRATEXT.append("Hit Enter to continue.")
                else:
                    Play['Dodge'] = 100
                    Turn = -2
                    EXTRATEXT.append("Hit Enter to continue.")
                
            else:
                if int(putin) == 3:
                    pass
                elif int(putin) == 4:
                    try:
                        Gturn = Use_Spell(Play['Spells'][2],Play,Bad)
                        Turn = -2
                    except:
                        Notdone = True
                        a = 0
                        while Notdone:
                            fx = ''
                            for b in range(3):

                                try:
                                    fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                    #print(fx)
                                except:
                                    Notdone = False
                            EXTRATEXT.append(fx)
                            a += 4
                        EXTRATEXT.append("You can do:")
                        return(True)
                        
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
                                    fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                    #print(fx)
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
                                    fx = (fx + ' ' + str(Play['Spells'][a+b]) + '('+str(a+b+1)+')')
                                    #print(fx)
                                except:
                                    Notdone = False
                            EXTRATEXT.append(fx)
                            a += 4
                        EXTRATEXT.append("You can do:")
                        return(True)

        else:

            Bad['Dodge'] = Bad['STDodge']
            #Bad
            EXTRATEXT.append(" ")
            EXTRATEXT.append("His Turn")

            try:
                BADAI = AI(Bad,Play)
            except:
                BADAI = AI(Bad,Play)
                print("?")
            
            if BADAI == 'Dodge':
                Bad['Dodge'] = 100
                EXTRATEXT.append(("%s missed." % (Bad["Name"])))
                Bturn = 'PMiss'
            elif BADAI == "Attack":
                Bturn = DAMAGE(Bad,Play,"P")
            else:
                Bturn = Use_Spell(BADAI,Bad,Play)
            Turn = Turn*-1
            EXTRATEXT.append("Hit Enter to continue.")
        
    except:
        pass
    if bad <=0:
        EXTRATEXT.append('You Won!')
        #print("You Won!")
        #time.sleep(3)
        Turn = 4
    elif play <= 0:
        EXTRATEXT.append('You Lost!')
        #print("You Lost!")
        Turn = 4
    return(False)
    time.sleep(.05)


    


def AI(Owner,Target):
    #End goal is that it learns.
    #required info
    #Owner['Dodge'] Owner['Hp'] Owner['MaxHp']
    #Owner['Spells'] *Owner['Aflictions']*
    #Owner['MaxStrain'] Owner['Strain']
    Spells = load("Spells")
    if (Owner['MaxHp']/random.randrange(3,6)) > Owner['Hp']:
        if random.randrange(1,3) == 1:
            return("Dodge")
        elif random.randrange(1,3) == 1:
            for spell in Owner['Spells']:
                if Spells[spell][1] < 0:
                    return(spell)
            
        else:
            if random.randrange(1,3) == 1:
                return("Attack")
            else:
                for spell in Owner['Spells']:
                    if Spells[spell][1] > 0:
                        return(spell)
    else:
        if random.randrange(1,3) == 1:
            if random.randrange(1,3) == 1:
                return("Attack")
            else:
                for spell in Owner['Spells']:
                    if Spells[spell][1] > 0:
                        return(spell)
                return("Attack")
        
    return("Dodge")



        

def Use_Spell(spell,Owner,Target):
    global SPELL
    global EXTRATEXT
    SPELL = spell
    Spells = load("Spells")
    spell = Spells[spell]
    #['Def', Max, Min, [Target efects], [Owner efects]]
    if spell[1] > 0:
        dmg = random.randrange(spell[1],spell[2])
        turn = DAMAGE(Owner,Target,'M',dmg)
        
    elif spell[1] < 0:
        ran = abs(random.randrange(spell[1],spell[2]))
        EXTRATEXT.append("%s Healed for %s!" % (Owner["Name"],ran))
        Owner['Hp'] += ran
        if Owner['Hp'] > Owner['MaxHp']:
            Owner['Hp'] = Owner['MaxHp']
            EXTRATEXT.append("%s is at Max health!" % (Owner["Name"],ran))
        turn = "Heal"
    else:
        EXTRATEXT.append("Is broke.")
        turn = "Broke"
        
    
    EXTRATEXT.append("Hit Enter to continue.")
    return(turn)



def DAMAGE(Owner,Target,Type,dmg = 'NA'):
    global EXTRATEXT
    if random.randrange(0,Target['Dodge']) < 40:
        if dmg != "NA":
            dmg = dmg - Target['Resist']
        else:
            dmg = random.randrange(0,Owner['MaxP']) - Target['Resist']
        if dmg > 0:
            EXTRATEXT.append(("%s hit for %s dmg." % (Owner["Name"],dmg)))
            Target['Hp'] -= dmg
            return(str(Type+"Hit"))
        else:
            EXTRATEXT.append(("%s missed." % (Owner["Name"])))
        
    else:
        EXTRATEXT.append(("%s missed." % (Owner["Name"])))
    return(str(Type+"Miss"))
    
    
def AFLICT(Owner):
    pass


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
    
    btypes = ["BadCretan\\redoneC","BadWarrior\\redoneC","BadWiz\\redoneC"]
    Badtype = btypes[random.randrange(0,len(btypes))]

    WepTypes = ["redoneSword","redoneSteelSword","redoneRoyalSword","redoneFirewand","redoneIcewand"]
    BGwep = WepTypes[random.randrange(0,len(WepTypes))]

    Bad = {'Type': Badtype,'Mainhand': BGwep,'Hp': 5,'Dodge': 50,'MaxHp':5,'STDodge': 50,'MaxStrain': 4, 'Strain': 4,'MaxP': 6,'Resist':0,'Spells':[]}
    visuals(Player,Bad)
    #print("Hello")

    
if __name__ == '__main__':
    btypes = ["BadCretan\\redoneC","BadWarrior\\redoneC","BadWiz\\redoneC"]
    Badtype = btypes[random.randrange(0,len(btypes))]

    WepTypes = ["redoneSword","redoneSteelSword","redoneRoyalSword","redoneFirewand","redoneIcewand"]
    BGwep = WepTypes[random.randrange(0,len(WepTypes))]

    Bad = {"Name": 'They','Type': Badtype,'Mainhand': BGwep,'Hp': 20,'Dodge': 50,'MaxHp':20,'MaxStrain': 4, 'Strain': 4,'STDodge': 50 ,'MaxP': 6,'Resist':0,'Spells':[]}
    Player = {"Name": 'You','Type': "Cretan\\redoneC",'Mainhand': "redoneSteelSword",'Loot': [],'Hp': 20,'MaxHp':20,'Dodge': 50, 'Spells': ["Firebolt",'Drink'],'MaxStrain': 4, 'Strain': 4,'STDodge': 50,'MaxP': 6,'Resist':0 }

    visuals(Player,Bad)
        #Thread(target = visuals).start()
        #print("Hello")
        #Thread(target = achual_stuff).start()

