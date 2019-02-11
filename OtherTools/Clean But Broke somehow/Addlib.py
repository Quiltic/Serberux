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
