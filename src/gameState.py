

class GameState:
    def __init__(self):
        self.nextState = self
     
    def update(self):
        pass

    def draw(self, screen):
        pass

    def handleKey(self, event):
        pass
    
    def getNextState(self):
        return self.nextState
    
    def setNextState(self, state):
        self.nextState = state