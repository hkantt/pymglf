
from engine import *


class ExampleState(State):

    def __init__(self):
        super().__init__("ExampleState")

    def enter(self):
        Core.imgui_io.font_global_scale = 2

    def exit(self):
        Core.imgui_io.font_global_scale = 1

    def render_ui(self):
        imgui.begin("Debug")
        imgui.text(str(Cursor.x) + " " + str(Cursor.y))
        imgui.text(str(Event.bstate))
        imgui.text(str(Event.kstate))
        imgui.text(str(Cursor.xoffset) + " " + str(Cursor.yoffset))
        imgui.end()

Core.add(ExampleState)
Core.activate("ExampleState")