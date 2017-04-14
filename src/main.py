from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from GameFSM import MainMenuFSM
<<<<<<< HEAD
from rpcore import RenderPipeline

=======
##asd
>>>>>>> master

class Main(ShowBase):
    def __init__(self):
        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)
        self.render_pipeline.daytime_mgr.time = "12:30"
        loadPrcFile('config/Config.prc')
        base.disableMouse()
        render.setShaderAuto()
        menu = MainMenuFSM()
        menu.request('Main')

app = Main()
app.run()
