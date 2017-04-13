from direct.fsm.FSM import FSM
import ToonGlobals, ClothingGlobals
from Toon import Toon
from characterController import characterController


class MainFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'MainFSM')
        
    def createPlayerChar(self):
        self.actor = Toon('player', ToonGlobals.boyTorsoModelDict['s'], ToonGlobals.boyLegsModelDict['s'], ToonGlobals.boyMediumTorsoAnimDict, ToonGlobals.boySmallLegsAnimDict, 's')
        self.player = characterController(self.actor)
        self.actor.reparentTo(render)
    
    def createEnv(self):
        self.env = loader.loadModel('phase_3.5/models/neighborhoods/toontown_central')
        self.env.reparentTo(render)
        
    def enterMain(self):
        self.createPlayerChar()
        self.createEnv()


class MainMenuFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'MainMenuFSM')
        self.frame = None
        self.playButton = None
        
    def enterMain(self):
        pass
    
    def exitMain(self):
        pass
    
    def enterOptions(self):
        pass
    
    def exitOptions(self):
        pass


class AvatarGuiFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'AvatarGuiFSM')

