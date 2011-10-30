'''
Created on Feb 15, 2010

@author: dkelley
'''

#classes, etc
import sys, pygame

#helper functions!
import titleMenu

scaled_w = 1280
scaled_h = 720

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((scaled_w,scaled_h))
render_surface = pygame.Surface((1600,900))
pygame.display.set_caption("Ice Game by Robert Hasegawa and David Kelley, Copyright 2011")

#Load the main menu as the first active/visible/keyfocus state
gameState = titleMenu.TitleMenu()

#Enter the main loop
while True:
    #limit to 30fps
    clock.tick(60)

    #handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        gameState.handleKey(event)

    #update active states
    gameState.update()

    #render visible states    
    gameState.draw(render_surface)
    
    #scale the screen
    pygame.transform.scale(render_surface, (scaled_w, scaled_h), screen)

    #update the screen
    pygame.display.flip()
    
    #get the next state to work with (usually the same state as previous)
    gameState = gameState.getNextState()

