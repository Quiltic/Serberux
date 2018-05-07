import pygame, os, math, random, time
    
DIR = os.getcwd()

class BackgroundGame(object):
    def __init__(self):
        #print(info)
        super().__init__()
        self.Bars = pygame.sprite.Group()
        self.PlayerSide = pygame.sprite.Group()
        self.EnemySide = pygame.sprite.Group()
         
        # Background image
        self.framework = pygame.image.load(DIR+"\\Serberux Background.png").convert_alpha()
    def update(self,screen,texts = {'A':['Oppse',(0,0,0)]}):
        #self.Bars.draw(screen)
        #texts {'A':[words,color],}
        pygame.font.init()
        CHANGEABLE = -1
        for a in ['A','B','C','D']:
            try:
                CHANGEABLE += 1
                valuefont = pygame.font.SysFont('Century', 40-len(texts[a][0]))
                textsurface = valuefont.render(texts[a][0], 0, texts[a][1])
                self.framework.blit(textsurface,(20+(CHANGEABLE*225),430))
            except:
                CHANGEABLE += 1
            
        screen.blit(self.framework,(0,0))


class Player(object):
    def __init__(self):
        #print(info)
        super().__init__()
        #               Cost, targetnum (0 player, 1 is bad), delay(ticks), tags, name
        self.spells = {'A':[2,1,1,['dmg','dmg'],'Bang'],'B':[3,0,60,['heal','heal'],'Crackel'],'C':[0,0,120,['stam','stam','stam','stam'],'Pop'],'D':[8,0,30,['sheild'],'Wall']}
        self.spellticks = {'A':0,'B':0,'C':0,'D':0}
        self.info = {'Hp':10,'MaxHp':10,'Stamina':10,'MaxStamina':10,'StaminaPerSec':1, 'Sheild': 0}
        self.tick = 0
        
        self.Bars = pygame.sprite.Group()

        self.Hpbar = Bar([self.info['MaxHp'],[255,0,0]],[14,491,'Left'])
        self.Stambar = Bar([self.info['MaxStamina'],[10,210,10]],[531,491,'Right'])

        
        self.Abar = Bar([self.spells['A'][2],[143,89,61]],[14,393,'Down'],(200,40))
        self.Bbar = Bar([self.spells['B'][2],[143,89,61]],[238,393,'Down'],(200,40))
        self.Cbar = Bar([self.spells['C'][2],[143,89,61]],[462,393,'Down'],(200,40))
        self.Dbar = Bar([self.spells['D'][2],[143,89,61]],[686,393,'Down'],(200,40))
        
        self.Bars.add(self.Hpbar)
        self.Bars.add(self.Stambar)
    
        self.Bars.add(self.Abar)
        self.Bars.add(self.Bbar)
        self.Bars.add(self.Cbar)
        self.Bars.add(self.Dbar)
    def update(self):
        #self.Bars.draw(screen)
        self.tick += 1
        for a in ['A','B','C','D']:
            if self.spellticks[a] != 0:
                self.spellticks[a] -= 1

        if self.tick >= 60:
            self.tick = 0
            self.info['Stamina'] += self.info['StaminaPerSec']

        if self.info['Hp'] > self.info['MaxHp']:
            self.info['Hp'] = self.info['MaxHp']
        elif self.info['Stamina'] > self.info['MaxStamina']:
            self.info['Stamina'] = self.info['MaxStamina']
            
        self.Hpbar.num = self.info['Hp']
        self.Stambar.num = self.info['Stamina']

        self.Abar.num = self.spellticks['A']
        self.Bbar.num = self.spellticks['B']
        self.Cbar.num = self.spellticks['C']
        self.Dbar.num = self.spellticks['D']
        
        self.Bars.update()

        return({'A':[self.spells['A'][len(self.spells['A'])-1],(self.spellticks['A'],self.spellticks['A'],self.spellticks['A'])],'B':[self.spells['B'][len(self.spells['B'])-1],(self.spellticks['B'],self.spellticks['B'],self.spellticks['B'])],'C':[self.spells['C'][len(self.spells['C'])-1],(self.spellticks['C'],self.spellticks['C'],self.spellticks['C'])],'D':[self.spells['D'][len(self.spells['D'])-1],(self.spellticks['D'],self.spellticks['D'],self.spellticks['D'])]})


    def DMGTHINGS(self,tag):
        if tag == 0:
            self.info['Sheild'] += 1
        else:
            if tag < 0:
                if self.info['Sheild'] > 0:
                    self.info['Sheild'] -= 1
                else:
                    self.info['Hp'] += tag
            else:
                self.info['Hp'] += tag

    def cleanup(self,let):
        returntags = [] 
        if self.info['Stamina'] >= self.spells[let][0]:
            self.info['Stamina'] -= self.spells[let][0]
            self.spellticks[let] = self.spells[let][2]
            for a in self.spells[let][3]:
                #0 is sheild, -1 is dmg, 1 is heal
                if a == 'dmg':
                    returntags.append([self.spells[let][1],-1])
                if a == 'heal':
                    returntags.append([self.spells[let][1],1])
                if a == 'sheild':
                    returntags.append([self.spells[let][1],0])
                if a == 'stam':
                    self.info['Stamina'] += 1
                    
        return(returntags)
            
    def A(self):
        
        if self.spellticks['A'] == 0:
            return(self.cleanup('A'))
        #print(self.Abar.rect.x,self.Abar.rect.y)
        return([])
        print('a')
    def B(self):
        if self.spellticks['B'] == 0:
            return(self.cleanup('B'))
        return([])
        print('b')
    def C(self):
        if self.spellticks['C'] == 0:
            return(self.cleanup('C'))
        return([])
        print('c')
    def D(self):
        if self.spellticks['D'] == 0:
           return(self.cleanup('D'))
        return([])
        print('d')
        


class Oponent(object):
    def __init__(self):
        #print(info)
        super().__init__()
        #               Cost, targetnum (0 player, 1 is bad), delay(ticks), tags, name
        self.spells = {'A':[2,0,1,['dmg','dmg'],'Bang'],'B':[3,1,60,['heal','heal'],'Crackel'],'C':[0,1,120,['stam','stam','stam','stam'],'Pop'],'D':[8,1,30,['sheild'],'Wall']}
        self.spellticks = {'A':0,'B':0,'C':0,'D':0}
        self.info = {'Hp':10,'MaxHp':10,'Stamina':10,'MaxStamina':10,'StaminaPerSec':1, 'Sheild': 0}
        self.tick = 0
        self.AiUsetig = random.randrange(30,241)
        self.AiUse = self.AiUsetig
        
        self.Bars = pygame.sprite.Group()

        #self.Hpbar = Bar([self.info['MaxHp'],[255,0,0]],[14,491,'Left'])
        #self.Stambar = Bar([self.info['MaxStamina'],[10,210,10]],[531,491,'Right'])
        
        #self.Bars.add(self.Hpbar)

    def update(self):
        q = []
        self.tick += 1
        for a in ['A','B','C','D']:
            if self.spellticks[a] != 0:
                self.spellticks[a] -= 1

        self.AiUse -= 1
        if self.AiUse <= 0:
            self.AiUse = self.AiUsetig
            c = [self.A,self.B,self.C,self.D]
            q = c[random.randrange(0,4)]()
            print(self.info['Hp'],q)
            
        
        if self.tick >= 60:
            self.tick = 0
            self.info['Stamina'] += self.info['StaminaPerSec']

        if self.info['Hp'] > self.info['MaxHp']:
            self.info['Hp'] = self.info['MaxHp']
        elif self.info['Stamina'] > self.info['MaxStamina']:
            self.info['Stamina'] = self.info['MaxStamina']

        
        return(q)
            
        #self.Hpbar.num = self.info['Hp']
        
        #self.Bars.update()

    def DMGTHINGS(self,tag):
        if tag == 0:
            self.info['Sheild'] += 1
        else:
            if tag < 0:
                if self.info['Sheild'] > 0:
                    self.info['Sheild'] -= 1
                else:
                    self.info['Hp'] += tag
            else:
                self.info['Hp'] += tag

    def cleanup(self,let):
        returntags = [] 
        if self.info['Stamina'] >= self.spells[let][0]:
            self.info['Stamina'] -= self.spells[let][0]
            self.spellticks[let] = self.spells[let][2]
            for a in self.spells[let][3]:
                #0 is sheild, -1 is dmg, 1 is heal
                if a == 'dmg':
                    returntags.append([self.spells[let][1],-1])
                if a == 'heal':
                    returntags.append([self.spells[let][1],1])
                if a == 'sheild':
                    returntags.append([self.spells[let][1],0])
                if a == 'stam':
                    self.info['Stamina'] += 1
                    
        return(returntags)
            
    def A(self):
        if self.spellticks['A'] == 0:
            return(self.cleanup('A'))
    def B(self):
        if self.spellticks['B'] == 0:
            return(self.cleanup('B'))

    def C(self):
        if self.spellticks['C'] == 0:
            return(self.cleanup('C'))

    def D(self):
        if self.spellticks['D'] == 0:
           return(self.cleanup('D'))



class Bar(pygame.sprite.Sprite):
     
    #
    def __init__(self,importantinfo,posinfo,size = (355, 40)):
        #print(info)
        super().__init__()
 
        self.image = pygame.Surface(size)
        self.image.fill(importantinfo[1])
        self.rect = self.image.get_rect()
        
        self.Max = importantinfo[0]
        self.rect.x = posinfo[0]
        self.rect.y = posinfo[1]
        #           Max, Color
        self.num = importantinfo[0]
        #           x,y, direction
        self.info = posinfo
        self.SIZE = size
        
    def update(self):
        if self.num > self.Max:
            self.num = self.Max
        elif self.num < 0:
            self.num = 0
        #print(self.num)

        #changes which way the bar works
        if self.info[2] == 'Left':
            #distance from 'home'
            xm = ((self.Max-self.num)/self.Max)*self.SIZE[0]
            self.rect.x = self.info[0] - xm
        elif self.info[2] == 'Right':
            xm = ((self.Max-self.num)/self.Max)*self.SIZE[0]
            self.rect.x = self.info[0] + xm

        elif self.info[2] == 'Down':
            xm = ((self.Max-self.num)/self.Max)*self.SIZE[1]
            self.rect.y = self.info[1] + xm
        elif self.info[2] == 'Up':
            xm = ((self.Max-self.num)/self.Max)*self.SIZE[1]
            self.rect.y = self.info[1] - xm
##        info = self.info
##        if self.info['clicked'] != clicked:
##            self.info['clicked'] = clicked
##            pygame.font.init()
##            valuefont = pygame.font.SysFont('Century', 48)
##            if len(info['Name']) > 10:
##                namefont = pygame.font.SysFont('Century', 24)
##            else:
##                namefont = pygame.font.SysFont('Century', 28)
##            textfont = pygame.font.SysFont('Century', 20)
##            
##            if info["Color"] == 'Red':
##                color_value = (85, 0, 13)
##            elif info["Color"] == 'Blue':
##                color_value = (41, 50, 156)
##            elif info["Color"] == 'Grey':
##                color_value = (54, 54, 54)
##            else:
##                color_value = (0, 0, 0)
##            
##
##            self.image = pygame.Surface((250, 400))
##            self.self_image = pygame.image.load(DIR+"\\Images\\"+info['Color']+' Card Front.png').convert_alpha()
##            self.image = self.self_image
##            textsurface = valuefont.render(str(info['Cost']), 0, color_value)#85 0 13
##            if info['Cost'] < 10:
##                self.image.blit(textsurface,(20,8))
##            else:
##                self.image.blit(textsurface,(6,8))
##
##            if len(info['Name']) > 10:
##                textsurface = namefont.render(str(info['Name']), 0, color_value)#85 0 13
##                self.image.blit(textsurface,(150-(len(info['Name'])*6),15))
##            else:
##                textsurface = namefont.render(str(info['Name']), 0, color_value)#85 0 13
##                self.image.blit(textsurface,(150-(len(info['Name'])*7),15))
##            
##
##            #for A in range(
##            if len(info['Text']) < 20:
##                textsurface = textfont.render(info['Text'], 0, color_value)#85 0 13
##                self.image.blit(textsurface,(25,250+(25*0)))
##            else:
##                info['Text'] = info['Text'] + '                         '
##                A = 0
##                c = 0
##                while A*20 < (len(info['Text'])):
##                    b = 0
##                    try:
##                        while (info['Text'][(20+(20*A)-b)] != ' ') and (info['Text'][(20+(20*A)-b)] != '.'):
##                            b+=1
##                        else:
##                            textsurface = textfont.render(info['Text'][(A*20)-c:20+(20*A)-b], 0, color_value)#85 0 13
##                            self.image.blit(textsurface,(25,250+(25*A)))
##                            #print(info['Text'][20+(20*A)-b])
##                            c = b
##                    except:
##                            b+=1
##                    #print(info['Text'][(A*20)-c])
##                    A+=1
##
##            
##            #patch_rect = (0, 0, 50, 65)
##            #self.image.blit(self.self_image, (0,0), patch_rect)
##     
##            # Set a referance to the image rect.
##            if not clicked:
##                self.image = pygame.transform.scale(self.image, (188, 300))
##            self.rect = self.image.get_rect()
##
##        self.rect.x = info['pos'][0]
##        self.rect.y = info['pos'][1]
        #    self.image.blit(self.self_image, (0,0), patch_rect)

##class Button(pygame.sprite.Sprite):
##     
##    # -- Methods
##    def __init__(self,maxpoints):
##        #print(info)
##        super().__init__()
## 
##        #
##        self.Max = maxpoints
##        self.rect.x = 
##        self.update(False)
##        
##    def update(self,num):
##        info = self.info
##        if self.info['clicked'] != clicked:
##            self.info['clicked'] = clicked
##            pygame.font.init()
##            valuefont = pygame.font.SysFont('Century', 48)
##            if len(info['Name']) > 10:
##                namefont = pygame.font.SysFont('Century', 24)
##            else:
##                namefont = pygame.font.SysFont('Century', 28)
##            textfont = pygame.font.SysFont('Century', 20)
##            
##            if info["Color"] == 'Red':
##                color_value = (85, 0, 13)
##            elif info["Color"] == 'Blue':
##                color_value = (41, 50, 156)
##            elif info["Color"] == 'Grey':
##                color_value = (54, 54, 54)
##            else:
##                color_value = (0, 0, 0)
##            
##
##            self.image = pygame.Surface((250, 400))
##            self.self_image = pygame.image.load(DIR+"\\Images\\"+info['Color']+' Card Front.png').convert_alpha()
##            self.image = self.self_image
##            textsurface = valuefont.render(str(info['Cost']), 0, color_value)#85 0 13
##            if info['Cost'] < 10:
##                self.image.blit(textsurface,(20,8))
##            else:
##                self.image.blit(textsurface,(6,8))
##
##            if len(info['Name']) > 10:
##                textsurface = namefont.render(str(info['Name']), 0, color_value)#85 0 13
##                self.image.blit(textsurface,(150-(len(info['Name'])*6),15))
##            else:
##                textsurface = namefont.render(str(info['Name']), 0, color_value)#85 0 13
##                self.image.blit(textsurface,(150-(len(info['Name'])*7),15))
##            
##
##            #for A in range(
##            if len(info['Text']) < 20:
##                textsurface = textfont.render(info['Text'], 0, color_value)#85 0 13
##                self.image.blit(textsurface,(25,250+(25*0)))
##            else:
##                info['Text'] = info['Text'] + '                         '
##                A = 0
##                c = 0
##                while A*20 < (len(info['Text'])):
##                    b = 0
##                    try:
##                        while (info['Text'][(20+(20*A)-b)] != ' ') and (info['Text'][(20+(20*A)-b)] != '.'):
##                            b+=1
##                        else:
##                            textsurface = textfont.render(info['Text'][(A*20)-c:20+(20*A)-b], 0, color_value)#85 0 13
##                            self.image.blit(textsurface,(25,250+(25*A)))
##                            #print(info['Text'][20+(20*A)-b])
##                            c = b
##                    except:
##                            b+=1
##                    #print(info['Text'][(A*20)-c])
##                    A+=1
##
##            
##            #patch_rect = (0, 0, 50, 65)
##            #self.image.blit(self.self_image, (0,0), patch_rect)
##     
##            # Set a referance to the image rect.
##            if not clicked:
##                self.image = pygame.transform.scale(self.image, (188, 300))
##            self.rect = self.image.get_rect()
##
##        self.rect.x = info['pos'][0]
##        self.rect.y = info['pos'][1]
##        #    self.image.blit(self.self_image, (0,0), patch_rect)

 
 
def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    #size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode((900,540))
    screen.fill((155,155,155))
 
    pygame.display.set_caption("Serberux")

    active_sprite_list = pygame.sprite.Group()
 
    # Create the player
    #card = {'Color':'Red',"Cost":2,'Name':'Punch','Text':'Deal 1 Damage.'}
    #for a in range(len(hand)):
    #    deck[hand[a]]['pos'] = [250*a,0]
    #Hpbar = Bar([10,[255,0,0]],[14,491,'Left'])
    #active_sprite_list.add(Hpbar)
    #Stambar = Bar([10,[10,230,10]],[531,491,'Right'])
    #active_sprite_list.add(Stambar)
    P = Player()
    B = Oponent()
    q = BackgroundGame()

        
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not done:
        screen.fill((155,155,155))
        #for a in active_sprite_list:
        #    a.update()
        ANSER = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                Mx,My = pygame.mouse.get_pos()
                print(Mx,My)
                if (My > 425) and (My < 480):
                    if (Mx >= 5) and (Mx < 220):
                        ANSER = P.A()
                    elif (Mx >= 230) and (Mx < 445):
                        ANSER = P.B()
                    elif (Mx >= 454) and (Mx < 670):
                        ANSER = P.C()
                    elif (Mx >= 680) and (Mx < 894):
                        ANSER = P.D()
                #Hpbar.num -= 1
                #Stambar.num += 1
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 3):
                pass
        for a in B.update():
            ANSER.append(a)
        entitylist = [P,B]
        for s in ANSER:
            entitylist[s[0]].DMGTHINGS(s[1])
                #Hpbar.num += 1
                #Stambar.num -= 1
        #if pygame.mouse.get_pressed()[0] == True:
        #    Hpbar.num -= 1
        #if pygame.mouse.get_pressed()[2] == True:
        #    Hpbar.num += 1
       
            #Mx,My = pygame.mouse.get_pos()
            #for a in active_sprite_list:
            #    if a.rect.collidepoint(Mx,My):
            #        a.info['pos'] = [Mx-125,My-200]
            #        a.update(True)
            #        a.rect.x = Mx-125
            #        a.rect.y = My-200
            #        break
                
        ppp = P.update()
    
        #screen.fill(BLUE)
        P.Bars.draw(screen)
        active_sprite_list.update()
        active_sprite_list.draw(screen)
        
        
        q.update(screen,ppp)
        clock.tick(60)
        pygame.display.flip()

        if B.info['Hp'] <= 0:
            done = True
            print('Winner!')
        
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
