from Toon import Toon
import ToonGlobals


class NpcToon(Toon):
    def __init__(self, charName, torsoModel, legsModel, torsoAnims, legsAnims, headType):
        Toon.__init__(self, charName, torsoModel, legsModel, torsoAnims, legsAnims, headType)
        self.reparentTo(render)
        self.request('Neutral', 1.0, True)
