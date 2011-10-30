import pygame, os, sys, menu

from states.ice1 import ice1State

class TitleMenu(menu.Menu):
    def __init__(self):
        #Load the resources for this state
        startSurface = pygame.image.load(os.path.join("images", "mainMenu", "start.bmp")).convert()
        startSurface.set_colorkey((255,255,255))
        startRolloverSurface = pygame.image.load(os.path.join("images", "mainMenu", "start_rollover.bmp")).convert()
        startRolloverSurface.set_colorkey((255,255,255))
        quitSurface = pygame.image.load(os.path.join("images", "mainMenu", "quit.bmp")).convert()
        quitSurface.set_colorkey((255,255,255))
        quitRolloverSurface = pygame.image.load(os.path.join("images", "mainMenu", "quit_rollover.bmp")).convert()
        quitRolloverSurface.set_colorkey((255,255,255))
        bgs = pygame.image.load(os.path.join("images", "mainMenu", "menu_bg.bmp")).convert()
        
        #Call menu initializer
        menu.Menu.__init__(self, width=1600, height=900, background=bgs)

        #Init the menu
        self.addEntry(text="Start", callback=self.newGame, image=startSurface, rolloverImage=startRolloverSurface)
        self.addEntry(text="Quit", callback=self.quitGame, image=quitSurface, rolloverImage=quitRolloverSurface)
        
    def newGame(self):
        self.setNextState(ice1State())

    def quitGame(self):
        sys.exit()

