import random
from names import *

#Savegame = open('Agame_Save','a')
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

'''
Example of a enemy
bad = {'Hp':20,"LvL": 1,'DmgType': 'Slash', "Atype": 'Light','MaxAttack': 5, "Dodge": 40,"MaxStrain": 4,"Specal": ['Na'], "Spells": ['Drink']}
#'''

def Playing(player,enemy):
    print()
    startresist = player['Resist']
    first = int(random.randrange(0,2))
    #Clone = player
    pstrain = 0
    estrain = 0
    pdodge = player['Dodge']
    edodge = enemy['Dodge']
    while (enemy['Hp'] > 0) and (player['Hp'] > 0):
        if first == 1:
            enemy['Dodge'] = edodge
            print ("It's the ENEMY's turn!")
            #Enemy Choise
            EC = enemy_ai(enemy)
            if 'DG' in EC:
                estrain = estrain -1
                if estrain > 0:
                    estrain = 0
                enemy['Dodge'] = 100
                print("You blocked the attack! ")
                
            elif 'PH' in EC:
                Attack(enemy,player,0,enemy['MaxAttack'],enemy['Specal'])
                
            else:
                print("%s uses a %s! " % (enemy['Name'],EC))
                estrain = estrain +1
                spel = Spells[EC]
                Attack(enemy,player,spel[0],spel[1],spel[2],spel[3])

            if estrain >= enemy['MaxStrain']:
                enemy['Aflictions'].append('Strained')
                print('%s Strained themselves.'% (enemy['Name']))
            Aflict(enemy,player)
            first = 0
            

        elif first == 0:
            player['Dodge'] = pdodge
            #Player Choise
            print ("It's YOUR turn!")
            print()
            print ('You have %s Hp.' % str(player['Hp']))
            print ("What do you wan't to do?")
            PC = str(input("Physical (1), Misc (2), or Dodge (3)? "))
            if '2' in PC:
                print ("Your options are %s." % str(player['Spells']))
                PC = str(input("")) #lower()

            if PC == '':
                PC = '3'
                
            if '3' in PC:
                pstrain = pstrain -1
                if pstrain > 0:
                    pstrain = 0
                player['Dodge'] = 100
                print("You Dodge!")
                
            elif '1' in PC:
                Attack(player,enemy,0,player['MaxAttack'],player['Specal'])
                
            else:
                try:
                    print("%s use a %s! " % (player['Name'],PC))
                    pstrain = pstrain +1
                    spel = Spells[PC]
                    Attack(player,enemy,spel[0],spel[1],spel[2],spel[3])
                except KeyError:
                    print('Misstyped.')
                    pstrain = pstrain -1
                    if pstrain > 0:
                        pstrain = 0
                    player['Dodge'] = 100
                    print("You Dodge!")

            if pstrain >= player['MaxStrain']:
                player['Aflictions'].append('Strained')
                print('You Strained yourself.')
            Aflict(player,enemy)
            first = 1
        input()
        print()
        
    if enemy['Hp'] <= 0:
        print ("You Won!")
        player['Resist'] = startresist
    else:
        print("You died.")
    input()
    print()
    print()
    print()
    #player = Clone


##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

#Ai's
    
'''
Wisard
Warior
'''
def enemy_ai(enemy):
    #print(enemy)
    healing = ['Drink','Heal','Grow','Patchup']
    dmgSpells = ['Gunshot','Firebolt','Icesike','Knockdown','Splinter','Backstab','Arrowfire','Volly']
    rn = int(random.randrange(2,4))
    if len(enemy['Spells']) > 2:
        if (enemy['Hp']) < enemy['HpMax']/rn:
            for a in enemy['Spells']:
                #print(a)
                if a in healing:
                    #print(a)
                    ran = random.randrange(0,3)
                    if ran == 2:
                        return str(a)
                    elif ran == 1:
                        return ('PH')
                    else:
                        return('DG')
        else:
            ran = random.randrange(0,5)
            if ran >= 3:
                for a in enemy['Spells']:
                    #print (a)
                    if a in dmgSpells:
                        ran = random.randrange(0,3)
                        if ran < 2:
                            return str(a)
            elif ran == 2:
                return('PH')
            else:
                return('DG')
    else:
        if enemy['Hp'] < enemy['HpMax']/rn:
            for a in enemy['Spells']:
                #print(a)
                if a in healing:
                    #print(a)
                    ran = random.randrange(0,3)
                    if ran == 2:
                        return str(a)
                    elif ran == 1:
                        return ('PH')
                    else:
                        return('DG')
        else:
            ran = random.randrange(0,5)
            if ran >= 3:
                return('PH')
            elif ran == 2:
                for a in enemy['Spells']:
                    #print (a)
                    if a in dmgSpells:
                        ran = random.randrange(0,3)
                        if ran < 2:
                            return str(a)
            else:
                return('DG')
    return('PH')


##########################################################################################################################
##########################################################################################################################
##########################################################################################################################


#Dmg Stuff
# # Things used : Dmgtype, Aflictions, Atype, LvL, Dodge, Hp, Resist Specal
'''
#WeponType Slash == Swords, Axes, Daggers
#WeponType Crushing == Maces, Hammers, Slings, Fists
#WeponType Pearce == Spears, Bows, Guns, Picaxes

#ArmorType None: Is weak to Slash
#ArmorType Light/Medium: Is weak to Pearce
#ArmorType Heavy: Is weak to Crushing

Dodge can go up by dodgeing
Aflictions are gained through fighting not beforehand (Unlike Blessings,Curses,and Deseces)
#'''

#Spells : Healing is negitive Dmg
#Spell templet: "Name": [mindmg,mxdmg,[effects],[selfinflicted]]
#  "Name": [0,2,['NA'],['NA']],
Spells = {"Run": [0,2,['NA'],['Run']],"Pet": [-2,0,['NA'],['Flip']],"Clot": [-4,-1,['NA'],['NA']],"Slash": [3,6,['Bleed'],['NA']],"Shield": [0,2,['NA'],['Shealded']],"Icespike": [2,7,['Weak'],['NA']],"Backstab": [0,10,['Bleed'],['Weak']],"Lightning": [4,9,['Stun'],['NA']],"Arrowfire": [0,5,['Bleed'],['NA']],"Leach": [2,6,['NA'],['Regenerate']],"Gunshot": [0,5,['Weak'],['NA']],"Volly": [0,10,['Bleed'],['NA']],"Firebolt": [3,7,['Fire'],['NA']],"Heal": [-6,0,['NA'],['NA']],"Meditate": [-5,0,['NA'],['Regenerate']], "Claw": [5,8,['Bleed'],['NA']],"Drink": [-6,0,['NA'],['Clumsy']],"NOPE": [100,200,['NA'],['Regenerate']]}

#Achual Stuff
def Attack(owner,target,mndmg,mxdmg,extra,selfinflicted = []):
    dmg = Reduction(owner,target,owner['DmgType'],random.randrange(mndmg,mxdmg))
    if dmg < 0:
        owner['Hp'] = owner['Hp']-dmg
    else:
        target['Hp'] = target['Hp']-dmg
        
    for a in extra:
        ran = random.randrange(0,4)
        #print(ran)
        if a != "NA":
            if (ran == 3) and (dmg != 0):
                if target['Name'] == 'You':
                    q = 'are'
                else:
                    q = 'is'
                print("%s %s affected with %s" % (target["Name"],q,a))
                target["Aflictions"].append(a)
            
    for a in selfinflicted:
        owner["Aflictions"].append(a)
        
    if owner["Aflictions"] == None:
        owner["Aflictions"] = ["NA"]


def Reduction(owner,target, HitType, dmg):
    if dmg >= 0:
        #Attacking
        Atype = target['Atype']
        ran = random.randrange(0,target['Dodge'])
        if owner['Name'] == 'You':
            mk = 'hit'
            mn = 'Miss'
        else:
            mk = 'hits'
            mn = 'Misses'
        if ran < 40:
            if HitType == 'Slash':
                if Atype == 'None':
                    dmg = dmg+int(target['LvL']/2)
            if HitType == 'Pearce':
                if (Atype == 'Light') or (Atype == 'Medium'):
                    dmg = dmg+int(target['LvL']/2)
            if HitType == 'Crushing':
                if Atype == 'Heavy':
                    dmg = dmg+int(target['LvL']/2)
            dmg = dmg - int(target['Resist']/2)
            if dmg > 0:
                print("%s %s for %s! " % (owner['Name'],mk,dmg))
            else:
                print("%s blocked the attack! " % (target['Name']))
                dmg = 0
        else:
            dmg = 0
            print("%s %s! " % (owner['Name'],mn))#,mk,mn
        return(dmg)
    
    elif dmg < 0:
        #Healing
        ran = random.randrange(0,target['Dodge'])
        if owner['Name'] == 'You':
            ml = 'heal'
            mn = 'Fail'
        else:
            ml = 'heals'
            mn = 'fails'
        if ran > 10:
            if dmg < 0:
                print("%s %s for %s! " % (owner['Name'],ml,abs(dmg)))
            else:
                print("%s %s!" % (owner['Name'],mn))
                dmg = 0
        else:
            dmg = 0
            print("%s %s! " % (owner['Name'],mn))#,mk,mn
        return(dmg)


def Aflict(owner,target):
    afl = owner["Aflictions"]
    #if afl == None:
    #    owner["Aflictions"] = ["NA"]
    #    afl = ['NA']
    # The Bad
    dmgtp = ['Poison','Bleed','Fire','Freeze','Fire2','Fire3']
    Dreturn = ['NA','NA','NA','NA','Fire','Fire2']
    
    stuntp = ['Stun','Tangled','Trapped','Confused','Trapped2']
    Sreturn = ['NA','NA','NA','NA','Trapped']

    dodgetp = ['Clumsy','Tripping','Blinded']
    DGreturn = ['NA','NA','NA']

    weaktp = ['Weak','Strained','Cursed']
    Wreturn = ['Strong','Strong','Strong']
    #The Good
    healtp = ['Regenerate','Grow','Invincible']
    Hreturn = ['NA','NA','Invincible']

    powertp = ['Strong','Embold','Powerfull','Shealded']
    Preturn = ['Weak','Weak','Weak','Weak']

    Gdodgetp = ['Sneaky','Hidden','Flying']
    Greturn = ['NA','NA','NA']
    
    Trading = ['Flip']
    Run = ['Run']

    addedstuff = ['NA']
    #print(afl)
    #print(owner["Aflictions"])
    for a in afl:
        #print(a)
        if a == 'NA':
            pass
        #Bad
        elif a in dmgtp:
            dmg = random.randrange(1,int(owner['LvL']/2)+2)
            owner['Hp'] = owner['Hp'] - dmg
            addedstuff.append(Dreturn[dmgtp.index(a)])
        elif a in stuntp:
            target['Dodge'] = target['Dodge'] + 100
            addedstuff.append(Sreturn[stuntp.index(a)])
            
        elif a in dodgetp:
            fail = random.randrange(1,int(owner['LvL'])+2)
            owner['Dodge'] = owner['Dodge'] - fail
            addedstuff.append(DGreturn[dodgetp.index(a)])
            
        elif a in weaktp:
            dmg = random.randrange(1,int(owner['LvL'])+2)
            target['Resist'] = target['Resist'] + dmg
            addedstuff.append(Wreturn[weaktp.index(a)])
        #Good
        elif a in healtp:
            dmg = random.randrange(1,int(owner['LvL']/2)+2)
            owner['Hp'] = owner['Hp'] + dmg
            addedstuff.append(Hreturn[healtp.index(a)])
            
        elif a in powertp:
            dmg = random.randrange(1,int(owner['LvL'])+2)
            target['Resist'] = target['Resist'] - dmg
            addedstuff.append(Preturn[powertp.index(a)])
            
        elif a in Gdodgetp:
            sucsess = random.randrange(1,int(owner['LvL'])+2)
            owner['Dodge'] = owner['Dodge'] + sucsess
            addedstuff.append(Greturn[Gdodgetp.index(a)])
            
        elif a in Trading:
            Playing(owner['Pet'],target)
        elif a in Run:
            Playing(owner,target)
        #Unkown
        else:
            print(a + ' is Unknown')
            dmg = random.randrange(1,int(owner['LvL']/2)+2)
            owner['Hp'] = owner['Hp'] - dmg
    owner["Aflictions"] = ['NA']

            
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

#bad = {'Name': 'Name','Hp':10,'HpMax':10,"LvL": 1,'DmgType': 'Slash', "Atype": 'Light','MaxAttack': 5, "Dodge": 40,'Resist': 0,"MaxStrain": 4,"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}

def Badguy_builder(plvl):
    dtypes = ['Slash','Crush','Pearce']
    atypes = ['None','Light','Medium','Heavy']
    Btype = random.randrange(0,5)
    if Btype == 0:
        #Warior
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(7,10)+plvl 
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(1,3)]
        bad['MaxAttack'] = random.randrange(5,8)+plvl
        bad['Dodge'] = 40
        bad['Resist'] = 0
        bad['MaxStrain'] = random.randrange(1,3)

    elif Btype == 1:
        #Bandit
        Band_spells = ['Drink','Backstab','Gunshot','Arrowfire']
        
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(7,10)+plvl
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(0,2)]
        bad['MaxAttack'] = random.randrange(3,5)+plvl
        bad['Dodge'] = 40
        bad['Resist'] = 0
        bad['MaxStrain'] = random.randrange(1,3)
        for a in range(2):
            bad['Spells'].append(random.randrange(0,len(Band_spells)))
            
    elif Btype == 2:
        #Wizad
        Band_spells = ['Drink','Firebolt','Icespike','Lightning']
        
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(5,7)+plvl
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(0,2)]
        bad['MaxAttack'] = random.randrange(3,5)+plvl
        bad['Dodge'] = 40
        bad['Resist'] = 0
        bad['MaxStrain'] = random.randrange(4,7)
        for a in range(3):
            bad['Spells'].append(random.randrange(0,len(Band_spells)))
            
    else:
        #Monster
        Band_spells = ['Claw','Leach']
        
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(7,13)+plvl
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(0,3)]
        bad['MaxAttack'] = random.randrange(5,7)+plvl
        bad['Dodge'] = random.randrange(40,60)
        bad['Resist'] = random.randrange(0,3)
        bad['MaxStrain'] = random.randrange(1,3)
        for a in range(1):
            bad['Spells'].append(random.randrange(0,len(Band_spells)))
    return(bad)

def Badguy_builder(plvl):
    dtypes = ['Slash','Crush','Pearce']
    atypes = ['None','Light','Medium','Heavy']
    Btype = random.randrange(0,5)
    if Btype == 0:
        #Warior
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(7,10)+plvl 
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(1,3)]
        bad['MaxAttack'] = random.randrange(5,8)+plvl
        bad['Dodge'] = 40
        bad['Resist'] = 0
        bad['MaxStrain'] = random.randrange(1,3)

    elif Btype == 1:
        #Bandit
        Band_spells = ['Drink','Backstab','Gunshot','Arrowfire']
        
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(7,10)+plvl
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(0,2)]
        bad['MaxAttack'] = random.randrange(3,5)+plvl
        bad['Dodge'] = 40
        bad['Resist'] = 0
        bad['MaxStrain'] = random.randrange(1,3)
        for a in range(2):
            bad['Spells'].append(random.randrange(0,len(Band_spells)))
            
    elif Btype == 2:
        #Wizad
        Band_spells = ['Drink','Firebolt','Icespike','Lightning']
        
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(5,7)+plvl
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(0,2)]
        bad['MaxAttack'] = random.randrange(3,5)+plvl
        bad['Dodge'] = 40
        bad['Resist'] = 0
        bad['MaxStrain'] = random.randrange(4,7)
        for a in range(3):
            bad['Spells'].append(random.randrange(0,len(Band_spells)))
            
    else:
        #Monster
        Band_spells = ['Claw','Leach']
        
        bad = {"Specal": ['NA'], "Spells": ['NA'],'Aflictions':['NA']}
        bad['Name'] = name()
        bad['HpMax'] = random.randrange(7,13)+plvl
        bad['Hp'] = bad['HpMax'] 
        bad['LvL'] = plvl
        bad['DmgType'] = dtypes[random.randrange(0,3)]
        bad['Atype'] = dtypes[random.randrange(0,3)]
        bad['MaxAttack'] = random.randrange(5,7)+plvl
        bad['Dodge'] = random.randrange(40,60)
        bad['Resist'] = random.randrange(0,3)
        bad['MaxStrain'] = random.randrange(1,3)
        for a in range(1):
            bad['Spells'].append(random.randrange(0,len(Band_spells)))
    return(bad)

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

'''
bad = {'Name': 'The Bandit','Hp':10,'HpMax':10,"LvL": 10,'DmgType': 'Slash', "Atype": 'Light','MaxAttack': 5, "Dodge": 40,'Resist': 0,"MaxStrain": 4,"Specal": ['NA'], "Spells": ['Firebolt','Drink'],'Aflictions':['NA']}
player = {'Name': 'You','Hp':10,'HpMax':10,"LvL": 1,'DmgType': 'Slash', "Atype": 'Light','MaxAttack': 5, "Dodge": 40,'Resist': 0,"MaxStrain": 4,"Specal": ['NA'], "Spells": ['Drink','Claw'],'Aflictions':['NA']}
Playing(bad)
#'''
