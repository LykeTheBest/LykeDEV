from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, AmbientLight, DirectionalLight, Vec4, WindowProperties
from direct.task import Task
from panda3d.core import KeyboardButton

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set window title
        properties = WindowProperties()
        properties.setTitle("4K PANDA - Lyke's Code Share")
        self.win.requestProperties(properties)

        # Load environment
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.1, 0.1, 0.1)
        self.environ.setPos(-8, 42, 0)

        # Load character model
        self.character = self.loader.loadModel("models/panda-model")
        self.character.reparentTo(self.render)
        self.character.setScale(0.005, 0.005, 0.005)
        self.character.setPos(0, 10, 0)

        # Add ambient lightning
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(0.3, 0.3, 0.3, 1))
        self.render.setLight(self.render.attachNewNode(ambientLight))

        # Add directional lightning
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection((1, 1, -1))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        self.render.setLight(self.render.attachNewNode(directionalLight))

        # Set camera control
        self.disableMouse()
        self.camera.setPos(0, -30, 10)
        self.camera.lookAt(self.character)

        # Set movement controls
        self.accept("arrow_left", self.move_character, ["left"])
        self.accept("arrow_right", self.move_character, ["right"])
        self.accept("arrow_up", self.move_character, ["up"])
        self.accept("arrow_down", self.move_character, ["down"])

    def move_character(self, direction):
        pos = self.character.getPos()
        if direction == "left":
            pos.x -= 1
        elif direction == "right":
            pos.x += 1
        elif direction == "up":
            pos.y += 1
        elif direction == "down":
            pos.y -= 1
        self.character.setPos(pos)
        self.camera.lookAt(self.character)

app = MyApp()
app.run()
