import random
# the characters, the setting, the plot, the conflict, and the resolution.
#Charicters:
MainCaricter = 'You'
#First 3 are main charicters, Last is the BadGuy
Charicter_list = []
#Twist: Good caricter is bad

def Charictermaker():
    Roles = ['Theaf','Landlord','SellSword','Guildleader','Stablemaster','Ruler','Preast','Mayor','Begger','Woodsman','Hunter','Innkeeper','Bartender','Knight','Blacksmith','Mage']
    Alignments = ['LawfullGood','NeutralGood','ChaoticGood','LawfullNeutral','Neutral','ChaoticNeutral','LawfullEvil','NutralEvil','ChaoticEvil'] 
    #Stuff = ['Debt','Wanted','Cursed','Boss','Blessed']
    # = Alignments[random.randrange(0,len(Alignments))] 
    Classes = ['T','B','W','C']
    Personality_Traits = ['Calm','Heartless','Kind','Passonate','Rude','Insecure','Treacherous','Deadly','Nieave']
    #How they know player
    Relations = ['Colege','Boss','Player is a Customer','Random Chance']
    #What they want from Player
    Wants = ['Gold','An Item','Love','Death','Info']
    PrimaryTrait = Personality_Traits[random.randrange(0,len(Personality_Traits))]
    Personality_Traits.remove(PrimaryTrait)
    Caricter = {'Role':Roles[random.randrange(0,len(Roles))],'Align': Alignments[random.randrange(0,len(Alignments))],'Relations': Relations[random.randrange(0,len(Relations))],'Wants': Wants[random.randrange(0,len(Wants))],'PrimaryTrait': PrimaryTrait,'SecondaryTrait': Personality_Traits[random.randrange(0,len(Personality_Traits))],'Class': Classes[random.randrange(0,len(Classes))],}
    return(Caricter)

for a in range(10):
    print(Charictermaker())

