'''
TO DO:
- Implement single image load sprites, preferable pre-cache all images and make available in a dict
- Fix keyboard whackyness in jet01.py key handling (if you press left/right really quick it gets stuck scrolling
- Implement pre/post sprite callbacks (pause, resume being the major callbacks)
- Allow .lev file to specify a time when random enemies may appear (for how long do random enemies appear, how many appear, which types may appear, etc?)
- Come up with way more enemies, weapons, etc, add music/sound effects, improve graphics, yah yah yah
'''

import pygame, gameState, os
from sprites import player
        
class ice1State(gameState.GameState):
    def __init__(self, level="ice1-1.lev"):
        gameState.GameState.__init__(self)
        
        self.playerSprite = player.sprite()
             
    def update(self):
        #update time and generate stuff from script
        oldtime = self.time
        self.time += self.settingsDict["scrollspeed"]
        for t in range(oldtime, self.time):
            if self.spawnDict.has_key(str(t)):
                for (sprite, y, x, pre, post) in self.spawnDict[str(t)]:
                    s = sprite.sprite(self, self.spriteGroups, y, x, pre, post)
                    for group in s.getGroups():
                        self.spriteGroups[group].add(s)        
        
        #scroll the background offsets
        self.bgOffset += self.settingsDict["scrollspeed"]
        if self.bgOffset >= 768:
            self.currentBg = self.nextBg
            self.nextBg += 1
            self.bgOffset = 0
            if self.nextBg >= len(self.bgOrderArray):
                self.nextBg = 0

        #now update other stuff
        for group in self.spriteGroups.itervalues():
            group.update()


    def draw(self, screen):
        #background first
        if self.bgOffset > 0:
            bg2 = self.bgDict[self.bgOrderArray[self.nextBg]]
            subRect = (0, bg2.get_rect()[3] - self.bgOffset, bg2.get_rect()[2], self.bgOffset)
            screen.blit(bg2, (0,0), subRect)

        bg1 = self.bgDict[self.bgOrderArray[self.currentBg]]
        subRect = (0, 0, bg1.get_rect()[2], bg1.get_rect()[3] - self.bgOffset)
        screen.blit(bg1, (0,self.bgOffset), subRect)

        #now the rest of the sprites
        for group in self.spriteGroups.itervalues():
            if group == self.spriteGroups["me"]:
                if group.sprite.dead == 0:
                    group.draw(screen) #Allow jet01 to draw itself
                else:
                    group.clear(screen, screen)
            else:
                group.draw(screen)


    def handleKey(self, event):
        if event.type == pygame.KEYDOWN:
            key = event.dict["key"]
            if key == pygame.K_ESCAPE:
                pass #bring up pause menu?
            else:
                self.playerSprite.keyDown(key)

        if event.type == pygame.KEYUP:
            key = event.dict["key"]
            self.playerSprite.keyUp(key)


    