import ToonGlobals
import ClothingGlobals
from direct.actor.Actor import Actor
from direct.fsm.FSM import FSM
from direct.interval.ActorInterval import LerpAnimInterval

class Toon(Actor, FSM):
    def __init__(self, charName, torsoModel, legsModel, torsoAnims, legsAnims, headType):
        FSM.__init__(self, 'GameFSM-%s' % (charName))
        Actor.__init__(self, {'Torso': torsoModel,
                'Legs': legsModel},
                {'Torso': torsoAnims,
                'Legs': legsAnims})
        self.attach('Torso', 'Legs', 'joint_hips')
        self.attachHead(headType)
        
    def attachHead(self, headType):
        self.Head = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
        self.Head.find('**/muzzle-short-surprise').hide()
        self.Head.find('**/muzzle-short-sad').hide()
        self.Head.find('**/muzzle-short-smile').hide()
        self.Head.find('**/muzzle-short-angry').hide()
        self.Head.find('**/muzzle-short-laugh').hide()
        self.Head.find('**/head-short').show()
        self.Head.find('**/head-front-short').show()
        self.Head.find('**/eyes-short').show()
        self.Head.find('**/joint_pupilL_short').show()
        self.Head.find('**/joint_pupilR_short').show()
        self.Head.find('**/head-long').hide()
        self.Head.find('**/head-front-long').hide()
        self.Head.find('**/eyes-long').hide()
        self.Head.find('**/joint_pupilL_long').hide()
        self.Head.find('**/joint_pupilR_long').hide()
        self.Head.find('**/ears-short').show()
        self.Head.find('**/ears-long').hide()
        self.headType = 's'
        
        self.torso = ToonGlobals.boyTorsoModelDict['s']
        self.legs = ToonGlobals.boyLegsModelDict['s']
        self.torsoAnimDict = ToonGlobals.boyMediumTorsoAnimDict
        self.legsAnimDict = ToonGlobals.boySmallLegsAnimDict
        
        self.actorCamNode = render.attachNewNode('actorCamNode')
        self.actorCamNode.setPos(0, 0, 2.5)
        self.actorCamNode.reparentTo(self)
        
        self.Neck = self.find('**/def_head')
        self.Head.reparentTo(self.Neck)

        self.find('**/shoes').hide()
        self.find('**/boots_long').hide()
        self.find('**/boots_short').hide()

        self.setBlend(animBlend=True, frameBlend=True)
        
    def enterNeutral(self, playRate):
        self.lerpAnimation("neutral")
        
    def enterWalk(self, playRate):
        self.lerpAnimation("walk", playRate = playRate)
        
    def enterRun(self, playRate):
        self.lerpAnimation("run")
        
    def enterRunningJumpIdle(self, playRate):
        self.lerpAnimation("running-jump-idle", doLoop = False)
        
    def enterJumpIdle(self, playRate):
        self.lerpAnimation("jump-idle", doLoop = False)
        
    def enterBigJump(self, playRate):
        self.lerpAnimation("jump", doLoop = False)

    def lerpAnimation(self, nextAnim, playRate = 1.0, doLoop = True):
        LerpAnimInterval(self, 0.1, self.getCurrentAnim(), nextAnim).start()
        self.stop(self.getCurrentAnim())
        if doLoop:
            self.loop(nextAnim, playRate)
        else:
            self.play(nextAnim)