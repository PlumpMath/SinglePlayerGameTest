from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from GameFSM import MainMenuFSM
from rpcore import RenderPipeline


class Main(ShowBase):
    def __init__(self):
        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)
        self.render_pipeline.daytime_mgr.time = "12:30"
        base.render_pipeline = self.render_pipeline
        loadPrcFile('config/Config.prc')
        base.disableMouse()
        render.setShaderAuto()
        menu = MainMenuFSM()
        menu.request('Main')

app = Main()
app.run()
