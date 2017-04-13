from Toon import Toon
from characterController import characterController
from followCam import FollowCam
import ToonGlobals
import ClothingGlobals


class PlayerToon():
    def __init__(self):
        self.actor = Toon('player', ToonGlobals.boyTorsoModelDict['s'], ToonGlobals.boyLegsModelDict['s'], ToonGlobals.boyMediumTorsoAnimDict, ToonGlobals.boySmallLegsAnimDict, 's')
        self.charController = characterController(self.actor)
        self.actor.reparentTo(render)
        self.followCam = FollowCam(base.cam, self.actor)