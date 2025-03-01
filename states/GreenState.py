
from engine import *


class GreenState(State):

    def __init__(self):
        super().__init__("GreenState")

    def enter(self):
        Core.imgui_io.font_global_scale = 2
    
    def exit(self):
        Core.imgui_io.font_global_scale = 1

    def render(self):
        Core.ctx.clear(0.0, 1.0, 0.0, 1.0)

    def render_ui(self):
        imgui.begin("State Switcher")
        if imgui.button("Go to RedState"):
            Core.activate("RedState")
        imgui.end()


Core.add(GreenState)