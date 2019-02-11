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

Places = []
for m in range(10):
    Room = {}
    Loots = ['RC','RR','RC','RR','RC','RC','RR','RE','MRE','RC','RR','RC','RR','RC','RC','RR','RE','MRE','MRL','MRE']
    Loot=[]
    for a in range(12):
        if coins(3):
            Loot.append(rand(Loots))
    

    Randoms = []
    Checks = ['Sneak', 'Attack','Coin']
    for a in range(len(Checks)):
        if coins(4):
            Randoms.append(rand(Checks))
        
    #Force =
    Fights = []
    Fight = ['Boss','W','B','T','C','WM', "SM"]
    for a in range(6):
        if coins(3):
            Fights.append(rand(Fight))
         
    Dmg = ["H","D","N","N","N","N"]
    if rand(Dmg)== 'H':
        Damage = random.randrange(-6,-1)
    elif rand(Dmg)== 'D':
        Damage = random.randrange(1,6)
    else:
        Damage = 0
        
    """
    areas = ['Attacking','Runing','Options','Honor','Loyalty']
    Change_area = []
    for a in areas:
        print(a)
        q = (input("Add or subtract (1 or -1)"))
        if q == '':
            break
        Change_area.append(int(q))
        
    Room = {'Print': Words, 'Connects':Connectors,'Loot':Loot,'Check':Randoms,'Force':Force,'Change':Change_area, 'Fights': Fights,'Dmg': Damage}
    
    print('L:',Loot)
    print('R:',Randoms)
    print("F:",Fights)
    print('D:',Damage)
    print()
    #"""
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
        Room[(str(m)+'Fall')] = {'Print': ["You fall through a hole in the floor.",'Move on(1)'], 'Connects':['End'],'Loot':[],'Check':[],'Force':[], 'Fights': [],'Dmg': 2}
    else:
        
        if 'Boss' in Fights:
            words.append('There is a boss here!')
            Connectors.append((str(m)+'Loot'))
            words.append('Next room(1), Loot the room(2)')
            Room[str(m)] = {'Print': words, 'Connects':Connectors,'Loot':[],'Check':Randoms,'Force':Force, 'Fights': Fights,'Dmg': 0}
            
        elif len(Fights) > 0:
            words.append('The room is garded!')
            Connectors.append((str(m)+'Loot'))
            words.append('Next room(1), Loot the room(2)')
            Room[str(m)] = {'Print': words, 'Connects':Connectors,'Loot':[],'Check':Randoms,'Force':Force, 'Fights': Fights,'Dmg': 0}
            
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
        Room[(str(m)+'Loot')] = {'Print': words, 'Connects':['End'],'Loot':Loot,'Check':[],'Force':[], 'Fights': [],'Dmg': Damage}
    
    Places.append(Room)    
            
for a in Places:
    print(a)

        
'''
Option to loot the room for Loot
Apon entering do the check if fail fall to new room,
  If sucsess deal Dmg start fight or loot room.
'''
"""
    x = 0
    z = 0
    y = 0
    w = 0
    c = 0

    for a in Room:
        #print(Room[str(a)]['Type'])
        if 'Boss' in Room[str(a)]['Type']:
            if 'Chest' in Room[str(a)]['Type']:
                z += 1
            elif 'Legondary' in Room[str(a)]['Type']:
                z += 1
            else:
                x += 1
        elif 'Chest' in Room[str(a)]['Type']:
            x += 1
        elif 'Legondary' in Room[str(a)]['Type']:
            z += 1
        elif 'Hord' in Room[str(a)]['Type']:
            x += 1
        elif 'Replenishing' in Room[str(a)]['Type']:
            y += 1
        elif 'Trapped' in Room[str(a)]['Type']:
            y += 1
        elif 'Posable' in Room[str(a)]['Type']:
            y += 1
        elif 'Garded' in Room[str(a)]['Type']:
            w += 1
        elif 'Loot' in Room[str(a)]['Type']:
            w += 1
        elif 'Connector' in Room[str(a)]['Type']:
            c +=1
        
    #print("L:",z)
    #print("E:",x)
    #print("R:",y)
    #print("C:",w)
    #print("Empty:",c)
    Places.append([z,x,y,w,c])

x = 0
z = 0
y = 0
w = 0
c = 0
for a in Places:
    z = z + a[0]
    x = x + a[1]
    y = y + a[2]
    w = w + a[3]
    c = c + a[4]
    
print("L:",z/1000)
print("E:",x/1000)
print("R:",y/1000)
print("C:",w/1000)
print("Empty:",c/1000)
print((z+x+c+w+y)/1000)
"""
