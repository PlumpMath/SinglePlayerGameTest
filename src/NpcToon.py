from Toon import Toon


class NpcToon(Toon):
    def __init__(self, charName, torsoModel, legsModel, torsoAnims, legsAnims, headType):
        Toon.__init__(self, charName, torsoModel, legsModel, torsoAnims, legsAnims, headType)