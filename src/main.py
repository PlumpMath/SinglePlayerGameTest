from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from GameFSM import MainFSM


class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        loadPrcFile("config/Config.prc")
        menu = MainFSM()
        menu.request('Main')
    
app = Main()
app.run()