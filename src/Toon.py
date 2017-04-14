import ToonGlobals
import ClothingGlobals
from direct.actor.Actor import Actor
from direct.fsm.FSM import FSM
from direct.interval.ActorInterval import LerpAnimInterval
from panda3d.core import Material

class Toon(Actor, FSM):
    def __init__(self, charName, torsoModel, legsModel, torsoAnims, legsAnims, headType):
        FSM.__init__(self, 'GameFSM-%s' % (charName))
        Actor.__init__(self, {'Torso': torsoModel,
                'Legs': legsModel},
                {'Torso': torsoAnims,
                'Legs': legsAnims})
        self.attach('Torso', 'Legs', 'joint_hips')
        self.attachHead(headType)
        self.charName = charName
        self.gloveMaterial = Material()
        self.gloveMaterial.setDiffuse((0, 0, 0, 1))
        self.gloveMaterial.clearEmission()
        self.gloveMaterial.clearSpecular()
        self.gloveMaterial.setShininess(0)
        self.setMaterial(self.gloveMaterial)
        self.setBlend(animBlend=True, frameBlend=True)
        
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
        
        self.headMaterial = Material()
        self.headMaterial.setDiffuse((0, 0, 1, 1))
        self.headMaterial.clearEmission()
        self.headMaterial.clearSpecular()
        self.headMaterial.setShininess(0)
        self.Head.setMaterial(self.headMaterial)
        
        
        self.Neck = self.find('**/def_head')
        self.Head.reparentTo(self.Neck)

        self.find('**/shoes').hide()
        self.find('**/boots_long').hide()
        self.find('**/boots_short').hide()
        
    def enterNeutral(self, playRate, doLoop=True):
        self.lerpAnimation("neutral", playRate, doLoop)
        
    def enterWalk(self, playRate, doLoop=True):
        self.lerpAnimation("walk", playRate, doLoop)
        
    def enterRun(self, playRate, doLoop=True):
        self.lerpAnimation("run", playRate, doLoop)
        
    def enterRunningJumpIdle(self, playRate, doLoop=True):
        self.lerpAnimation("running-jump-idle", playRate, doLoop)
        
    def enterJumpIdle(self, playRate, doLoop=True):
        self.lerpAnimation("jump-idle", playRate, doLoop)
        
    def enterBigJump(self, playRate, doLoop=True):
        self.lerpAnimation("jump", playRate, doLoop)

    def lerpAnimation(self, nextAnim, playRate, doLoop = True):
        print playRate
        if self.getCurrentAnim() != nextAnim:
            LerpAnimInterval(self, 0.1, self.getCurrentAnim(), nextAnim).start()
            self.stop(self.getCurrentAnim())
        if doLoop:
            self.loop(nextAnim, playRate)
        else:
            self.play(nextAnim)
