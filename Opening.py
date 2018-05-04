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
        self.background = pygame.image.load(DIR+"\\Images\\Serberux Background.png").convert_alpha()
    def update(self,screen):
        self.Bars.draw(screen)
        screen.draw(self.background)
        
class Bar(pygame.sprite.Sprite):
     
    # -- Methods
    def __init__(self,maxpoints):
        #print(info)
        super().__init__()
 
        self.image = pygame.Surface((400, 40))
        self.image.fill([255,0,0])
        self.rect = self.image.get_rect()
        self.Max = maxpoints
        self.rect.x = 0
        
    def update(self,num):
        xm = (self.Max*num)*self.Max
        self.rect.x = 0 - xm
        pass
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
 
    pygame.display.set_caption("Serberux")

    active_sprite_list = pygame.sprite.Group()
 
    # Create the player
    #card = {'Color':'Red',"Cost":2,'Name':'Punch','Text':'Deal 1 Damage.'}
    #for a in range(len(hand)):
    #    deck[hand[a]]['pos'] = [250*a,0]
    player = Bar(20)
    active_sprite_list.add(player)
    q = BackgroundGame()
        
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not done:

        for a in active_sprite_list:
            a.update(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if pygame.mouse.get_pressed()[0] == True:
            #if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            Mx,My = pygame.mouse.get_pos()
            for a in active_sprite_list:
                if a.rect.collidepoint(Mx,My):
                    a.info['pos'] = [Mx-125,My-200]
                    a.update(True)
                    a.rect.x = Mx-125
                    a.rect.y = My-200
                    break
                
            

        #screen.fill(BLUE)
        active_sprite_list.draw(screen)
        q.update(screen)
        clock.tick(60)
        pygame.display.flip()
        
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
