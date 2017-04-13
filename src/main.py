from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from GameFSM import MainMenuFSM


loadPrcFile("config/Config.prc")

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.disableMouse()
        menu = MainMenuFSM()
        menu.request('Main')
    
app = Main()
app.run()