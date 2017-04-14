from panda3d.core import CollisionTraverser, BitMask32
from direct.controls.ControlManager import ControlManager
from direct.controls.GravityWalker import GravityWalker
from direct.task.TaskManagerGlobal import taskMgr
from direct.showbase.InputStateGlobal import inputState
from direct.interval.IntervalGlobal import ActorInterval


class characterController():
    def __init__(self, actor):
        self.actor = actor
        
        self.wallBitmask = BitMask32.bit(1)
        self.floorBitmask = BitMask32.bit(1)

        base.cTrav = CollisionTraverser()
        self.walkControls = GravityWalker(legacyLifter=True)
        self.walkControls.setWallBitMask(self.wallBitmask)
        self.walkControls.setFloorBitMask(self.floorBitmask)
                        #Forward, Jump, Backwards, Left/Right
        self.walkControls.setWalkSpeed(24.0, 30.0, 8.0, 80.0)
        self.walkControls.initializeCollisions(base.cTrav, self.actor, floorOffset=0.025, reach=4.0)
        self.walkControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.walkControls.enableAvatarControls()
        self.actor.physControls = self.walkControls
        
        self.keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
 
        self.setWatchKey('arrow_up', 'forward', 'forward')
        self.setWatchKey('control-arrow_up', 'forward', 'forward')
        self.setWatchKey('alt-arrow_up', 'forward', 'forward')
        self.setWatchKey('shift-arrow_up', 'forward', 'forward')
        self.setWatchKey('arrow_down', 'reverse', 'backward')
        self.setWatchKey('control-arrow_down', 'reverse', 'backward')
        self.setWatchKey('alt-arrow_down', 'reverse', 'backward')
        self.setWatchKey('shift-arrow_down', 'reverse', 'backward')
        self.setWatchKey('arrow_left', 'turnLeft', 'left')
        self.setWatchKey('control-arrow_left', 'turnLeft', 'left')
        self.setWatchKey('alt-arrow_left', 'turnLeft', 'left')
        self.setWatchKey('shift-arrow_left', 'turnLeft', 'left')
        self.setWatchKey('arrow_right', 'turnRight', 'right')
        self.setWatchKey('control-arrow_right', 'turnRight', 'right')
        self.setWatchKey('alt-arrow_right', 'turnRight', 'right')
        self.setWatchKey('shift-arrow_right', 'turnRight', 'right')
        self.setWatchKey('control', 'jump', 'control')
 
        self.animState = ''
        
        base.taskMgr.add(self.handleMovement, 'controlManager')
        
        base.accept('f1', self.toggleCollisions)

    def getAirborneHeight(self):
        return 3.2375 + 0.025000000000000001
    
    def setWatchKey(self, key, inputFunc, keyMapName):
        def watchKey(active=True):
            if active == True:
                inputState.set(inputFunc, True)
                self.keyMap[keyMapName] = 1
            else:
                inputState.set(inputFunc, False)
                self.keyMap[keyMapName] = 0
        base.accept(key, watchKey, [True])
        base.accept(key+'-up', watchKey, [False])
                
    def setMovementAnimation(self, loopName, playRate=1):
        if 'jump' in loopName:
            loopName = 'JumpIdle'
            self.animState = 'jump'
        elif loopName == 'run':
            loopName = 'Run'
            self.animState = 'run'
        elif loopName == 'walk':
            loopName = 'Walk'
            if playRate == -1:
                self.animState = 'backwardswalk'
            else:
                self.animState = 'forwardswalk'
        elif loopName == 'neutral':
            loopName = 'Neutral'
            self.animState = 'neutral'
        else:
            self.movingJumping = False
            self.movingForward = False
            self.movingNeutral = False
            self.movingRotation = False
            self.movingBackward = False
        if loopName == 'jump-idle':
            loopName = 'JumpIdle'
            self.animState = 'jumpidle'
        elif loopName == 'running-jump-idle':
            loopName = 'RunningJumpIdle'
            self.animState = 'runningjumpidle'
        self.actor.request(loopName, playRate)
        
    def handleMovement(self, task):
        if self.keyMap['control'] == 1:
            if self.keyMap['forward'] == 1 or self.keyMap['backward'] == 1 or self.keyMap['left'] == 1 or self.keyMap['right'] == 1:
                if self.animState != 'jump':
                    if self.actor.physControls.isAirborne:
                        self.setMovementAnimation('running-jump-idle')
                    else:
                        if self.keyMap['forward'] == 1:
                            if self.animState != 'run':
                                self.setMovementAnimation('run')
                        elif self.keyMap['backward'] == 1:
                            if self.animState != 'backwardswalk':
                                self.setMovementAnimation('walk', -1)
                        elif self.keyMap['left'] == 1 or self.keyMap['right'] == 1:
                            if self.animState != 'forwardswalk':
                                self.setMovementAnimation('walk')
                else:
                    if not self.actor.physControls.isAirborne:
                        if self.keyMap['forward'] == 1:
                            if self.animState != 'run':
                                self.setMovementAnimation('run')
                        elif self.keyMap['backward'] == 1:
                            if self.animState != 'backwardswalk':
                                self.setMovementAnimation('walk', -1)
                        elif self.keyMap['left'] == 1 or self.keyMap['right'] == 1:
                            if self.animState != 'forwardswalk':
                                self.setMovementAnimation('walk')
            else:
                if self.actor.physControls.isAirborne:
                    if self.animState != 'jumpidle':
                        self.setMovementAnimation('jump-idle')
                else:
                    if self.animState != 'runningjumpidle':
                        self.setMovementAnimation('neutral')
        elif self.keyMap['forward'] == 1:
            if self.animState != 'run':
                if not self.actor.physControls.isAirborne:
                    self.setMovementAnimation('run')
        elif self.keyMap['backward'] == 1:
            if self.animState != 'backwardswalk':
                if not self.actor.physControls.isAirborne:
                    self.setMovementAnimation('walk', -1)
        elif self.keyMap['left'] == 1 or self.keyMap['right'] == 1:
            if self.animState != 'forwardswalk':
                if not self.actor.physControls.isAirborne:
                    self.setMovementAnimation('walk')
        else:
            if self.animState != 'neutral':
                if not self.actor.physControls.isAirborne:
                    self.setMovementAnimation('neutral')
        return task.cont
    
    def collisionsOn(self):
        self.actor.physControls.setCollisionsActive(True)
        self.actor.physControls.isAirborne = True
        
    def collisionsOff(self):
        self.actor.physControls.setCollisionsActive(False)
        self.actor.physControls.isAirborne = True
        
    def toggleCollisions(self):
        print 'collisions toggled'
        if self.actor.physControls.getCollisionsActive():
            self.actor.physControls.setCollisionsActive(False)
            self.actor.physControls.isAirborne = True
        else:
            self.actor.physControls.setCollisionsActive(True)
            self.actor.physControls.isAirborne = True
    