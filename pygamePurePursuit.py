import sys, pygame
pygame.init()

size = width, height = 500, 500

black = 0, 0, 0
yellow = 255,255,51 
pink = 255,192,203
green = 34,139,34
red = 255,0,0 

myfont10 = pygame.font.SysFont('Comic Sans MS', 10)
myfont15 =pygame.font.SysFont('Comic Sans MS', 15)
textPathTop = myfont10.render('(250,0)',False,black)
textPathButtom = myfont10.render('(250,500)',False,black)
textLH = myfont15.render('L = 80',(red[0]),False,black)
screen = pygame.display.set_mode(size)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    screen.fill(pink)
    pygame.draw.line(screen,black,[250,0],[250,500],1)
    screen.blit(textPathTop,(255,3))
    screen.blit(textPathButtom,(255,480))
    screen.blit(textLH,(10,10))
    pygame.display.flip()