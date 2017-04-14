from direct.fsm.FSM import FSM
import ToonGlobals, ClothingGlobals
from PlayerToon import PlayerToon
from direct.gui.DirectGui import *
from NpcToon import NpcToon


class MainFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'MainFSM')
    
    def createEnv(self):
        self.env = loader.loadModel('phase_3.5/models/neighborhoods/toontown_central')
        self.env.reparentTo(render)
        
    def enterMain(self):
        self.localAvatar = PlayerToon()
        npc = NpcToon('npc', ToonGlobals.boyTorsoModelDict['s'], ToonGlobals.boyLegsModelDict['s'], ToonGlobals.boySmallTorsoAnimDict, ToonGlobals.boySmallLegsAnimDict, 's')
        self.createEnv()


class MainMenuFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'MainMenuFSM')
        self.frame = DirectFrame(frameColor=(0, 0, 0, 0), frameSize=(-1, 1, -1, 1), pos=(0, 0, 0))
        self.frame.enableEdit()
        self.playButton = DirectButton(text="Play", command=self.request, extraArgs=['PlayGame'], pos=(0, 0, -0.56), scale=0.1)
        self.playButton.reparentTo(self.frame)
        self.title = OnscreenText(text="Game Title", pos=(0, 0.56))
        self.title.reparentTo(self.frame)
        base.accept('f1', self.printDetails)
    
    def printDetails(self):
        print self.playButton.getPos()
        print self.playButton.getScale()
        print self.title.getPos()
        print self.title.getScale()
    
    def enterMain(self):
        self.playButton.show()
        self.title.show()
    
    def exitMain(self):
        self.playButton.hide()
        self.title.hide()
    
    def enterOptions(self):
        pass
    
    def exitOptions(self):
        pass
    
    def enterPlayGame(self):
        self.frame.destroy()
        self.playButton.destroy()
        self.title.destroy()
        mainFSM = MainFSM()
        mainFSM.request('Main')
        


class AvatarGuiFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'AvatarGuiFSM')

