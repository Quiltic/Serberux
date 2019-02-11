"""
This is basickly an adlib but randomly.
"""
import random

"""
Noun = ["A bandit",'A Wizard',"Something"]
Verb = ["flys",'jumps','dashes','kicks','flails',"begs","develops","retires","rules","bleaches","squashes","reports","wishes","marks","rhymes"]
Adverb = ["over",'under','through','next to',"behind"]
Adj = ["you",'a friend','the cart',"the mammoth","the giant"]
End = ['.','!?','!','?']
Connector = []

for a in range(10):
    Sentance = ("%s %s %s %s%s" % (Noun[random.randrange(0,len(Noun))],Verb[random.randrange(0,len(Verb))],Adverb[random.randrange(0,len(Adverb))],Adj[random.randrange(0,len(Adj))],End[random.randrange(0,len(End))]))
    print(Sentance)
#"""    


'''
# Ahead of you there is an overturned cart.
# There is a bridge with a little house on eather side.

#Types of conflict
#Begin = ['Bandits','Traped','Store','Unknown','Dungion']#'Pirites',


Start_Current = ["Wandering around you",'Ahead you','Around you, you']#'Before you there is'
Start_Past = ['Here once was'] #,"At one point there was"
#Start_Future = ["NOTHING!"]
Time = [Start_Current,Start_Current] #,'Future',Start_Past
Start_Sence = ['see','hear','see','smell']

BANDIT_THING_ADJ = ['a burning','a','a','a smoldering','a destroyed','a gostly','a bloody', 'a dusty']
BANDIT_PERS_ADJ = ['a burning','a','a','a sleaping', 'a dancing']
BANDIT_PERS = ["bandit"]
BANDIT_THING = ['pile of bones','dead horse','overturned cart', 'cart']

Bandit_Noun = [[BANDIT_PERS,BANDIT_PERS_ADJ],[BANDIT_THING,BANDIT_THING_ADJ]]

END_Current = ['.','!']
END_Past = ['','']

for a in range(10):
    A = Time[random.randrange(0,len(Time))]
    AB = Start_Sence[random.randrange(0,len(Start_Sence))]
    B = Bandit_Noun[random.randrange(0,len(Bandit_Noun))]
    print("%s %s %s %s%s" % (A[random.randrange(0,len(A))],AB,B[1][random.randrange(0,len(B[1]))],B[0][random.randrange(0,len(B[0]))],END_Current[random.randrange(0,len(END_Current))]))

#'''

#Events[new][newer] = {'Print': Words, 'Connects':Connectors,'Loot':Loot,'Check':Randoms,'Force':Force,'Change':Change_area, 'Fights': Fights,'Dmg': Damage}
            

'''
["Wandering around you",'Ahead you','Around you, you']#'Before you there is'
['Attacking','Runing','Options','Honor','Loyalty']
plots:
*Shop
Begger/theaf
Caravan Raid
Ambush
Gathering
Pet*/hunting
*Dungion
'''

def rand(thing):
    return(thing[random.randrange(0,len(thing))])

#plots = [Begger,Theaf,CaravanRaid,Ambush,GatheringPlant,GatheringItem,Hunt]

#Begger - upps/Lowers Honor Posable Common item
A1 = ["Wandering around you",'Ahead you','Before you, you']
B1 = ["see","see","smell"]
C1 = ['a crusty','a dusty','a rotten','a blind','a greying']
D1 = ['begger.']

A2 = ["He is",'She is']
B2 = ['along','begging along','sitting along']
C2 = ["the edge of"]
D2 = ['the road.','the forest.']

Chose = 'Go up and talk(1), avoid the begger(2), give a gold(3).'

#Begger["A"] = [[A1,B1,C1,D1],[A2,B2,C2,D2],Chose]


print(('%s %s %s %s') % (rand(A1),rand(B1),rand(C1),rand(D1)))
print(('%s %s %s %s') % (rand(A2),rand(B2),rand(C2),rand(D2)))
print(Chose)
print('')

#Talk
Btype = ['Good','Angry','Generous','Rude']
qya = rand(Btype)
if qya == 'Good':
    A1 = ["The begger"]
    B1 = ["looks up at you","does nothing",'stays still']
    C1 = ['in your presence.']
    D1 = ['']

    A2 = ["The beggers voice is"]
    B2 = ['raspy','quiet','rough','chirpy']
    C2 = ["when they speak."]
    D2 = ['']

    A3 = ['Begger:']
    B3 = ['Yes?','Hello.']
    C3 = ['']
    D3 = ['']
    
    Chose = 'Ask how they got here(1), leave(2), give a gold(3).'
    
if qya  == 'Angry':
    A1 = ["The begger"]
    B1 = ["looks up at you","does nothing",'stays still']
    C1 = ['in your presence.']
    D1 = ['']

    A2 = ["The beggers voice is"]
    B2 = ['raspy','quiet','rough']
    C2 = ["when they speak."]
    D2 = ['']

    A3 = ['Begger:']
    B3 = ["What do you wan't?",'Leave me be.']
    C3 = ['']
    D3 = ['']
    
    Chose = 'Ask how they got here(1), leave(2), give a gold(3).'

if qya == 'Generous':
    A1 = ["The begger"]
    B1 = ["looks up at you","does nothing",'stays still']
    C1 = ['in your presence.']
    D1 = ['']

    A2 = ["The beggers voice is"]
    B2 = ['raspy','quiet','rough','chirpy']
    C2 = ["when they speak."]
    D2 = ['']

    A3 = ['Begger:']
    B3 = ['Yes?','Hello.']
    C3 = ['']
    D3 = ['']
    
    Chose = 'Ask how they got here(1), leave(2), give a gold(3).'
    
if qya  == 'Rude':
    A1 = ["The begger"]
    B1 = ["looks up at you","does nothing",'stays still']
    C1 = ['in your presence.']
    D1 = ['']

    A2 = ["The beggers voice is"]
    B2 = ['raspy','quiet','rough']
    C2 = ["when they speak."]
    D2 = ['']

    A3 = ['Begger:']
    B3 = ["What do you wan't?",'Leave me be.']
    C3 = ['']
    D3 = ['']
    
    Chose = 'Ask how they got here(1), leave(2), give a gold(3).'


print(('%s %s %s %s') % (rand(A1),rand(B1),rand(C1),rand(D1)))
print(('%s %s %s %s') % (rand(A2),rand(B2),rand(C2),rand(D2)))
print(('%s %s %s %s') % (rand(A3),rand(B3),rand(C3),rand(D3)))
print(Chose)
print('')

#Ask

if qya == 'Good':
    A1 = ["Begger:"]
    B1 = ["I worked as a","I was born to be a"]
    C1 = ['cook at a','stable master at a','guard at a']
    D1 = ['bunkhouse.','mansion.','inn.']

    A2 = ["Begger:"]
    B2 = ['When I was fired for']
    C2 = ["drinking to much.",'sleeping to much.','using gladerock.']
    D2 = ['']

    A3 = ['Begger:']
    B3 = ['Do you have any coin to spare?']
    C3 = ['']
    D3 = ['']
    
    Chose = "Heal them(1), leave(2), give a gold(3)."
    
if qya  == 'Angry':
    A1 = ["Begger:"]
    B1 = ["I told you to leave!"]
    C1 = ['']
    D1 = ['']

    A2 = ["The begger"]
    B2 = ['lunges','pounces','scrabbles']
    C2 = ["for you."]
    D2 = ['']

    A3 = ['']
    B3 = ['']
    C3 = ['']
    D3 = ['']
    
    Chose = "Fight(1), run(2)."

if qya == 'Generous':
    A1 = ["Begger:"]
    B1 = ["I worked as a","I was born to be a"]
    C1 = ['cook at a','stable master at a','guard at a']
    D1 = ['bunkhouse.','mansion.','inn.']

    A2 = ["Begger:"]
    B2 = ['When I was fired for']
    C2 = ["drinking to much.",'sleeping to much.','using gladerock.']
    D2 = ['']

    A3 = ['Begger:']
    B3 = ['Do you have any coin to spare?']
    C3 = ['']
    D3 = ['']
    
    Chose = "Heal them(1), leave(2), give a gold(3)."
    
if qya  == 'Rude':
    A1 = ["Begger:"]
    B1 = ["I worked as a","I was born to be a"]
    C1 = ['cook at a','stable master at a','guard at a']
    D1 = ['bunkhouse.','mansion.','inn.']

    A2 = ["Begger:"]
    B2 = ['When I was fired for']
    C2 = ["turning your mother into a pig.",'turning your mother into a frog.']
    D2 = ['']

    A3 = ['Begger:']
    B3 = ['Do you have any coin to spare?']
    C3 = ['']
    D3 = ['']
    
    Chose = "Heal them(1), leave(2), give a gold(3)."

print(('%s %s %s %s') % (rand(A1),rand(B1),rand(C1),rand(D1)))
print(('%s %s %s %s') % (rand(A2),rand(B2),rand(C2),rand(D2)))
print(('%s %s %s %s') % (rand(A3),rand(B3),rand(C3),rand(D3)))
print(Chose)
print('')

#For game:
    #A-starting
    #B-plot
    #B2-dif plot
    #B3?-dif plot
    #
    #
    #

Nouns = ['Begger','Bandit','Beast']
noun = rand(Nouns)
A1 = ["Wandering around you",'Ahead you','Before you, you']
B1 = ["see","see","smell"]
C1 = ['a crusty','a dusty','a rotten','a blind','a greying']
D1 = [noun]

A2 = [(noun+' is')]
B2 = ['along','sleeping along','sitting along']
C2 = ["the edge of"]
D2 = ['the road.','the forest.']

Chose = 'Go up and talk(1), avoid the begger(2), give a gold(3).'

Events[new][newer] = {'Print': Words, 'Connects':Connectors,'Loot':Loot,'Check':Randoms,'Force':Force,'Change':Change_area, 'Fights': Fights,'Dmg': Damage}

