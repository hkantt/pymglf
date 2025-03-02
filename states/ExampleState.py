
from engine import *


class ExampleState(CoreState):

    # An Example of an CoreState showcasing some functionality

    def __init__(self):
        # Using a simple string as an ID
        # ID should preferably assume string or integer values
        super().__init__("ExampleState")

    def enter(self):
        # Called when the state is activated
        
        # Change ImGui UI scale
        Core.imgui_io.font_global_scale = 2

        # Some values defined by the user
        self.keys_held = []
        self.keypresslog = ""
        self.keyreleaselog = ""
        self.mousepress = ""
        self.mouserelease = ""
    
    def exit(self):
        # Called while exiting the state
        # Resetting UI scale
        Core.imgui_io.font_global_scale = 1

    def events(self):
        self.keys_held = []
        self.mouse_held = []

        # Key Hold Events
        for key in Event.keys_held:
            self.keys_held.append(chr(key))
        
        # Another Key Hold Event Example
        if Event.keyset.SPACE in Event.keys_held:
            print("Holding Space")

        # Mouse Button Hold Events
        if Event.mouse.left in Event.mouse_held:
            self.mouse_held.append("Left")
        if Event.mouse.right in Event.mouse_held:
            self.mouse_held.append("Right")
        if Event.mouse.middle in Event.mouse_held:
            self.mouse_held.append("Middle")
                
        # Key Press/Release Events
        if Event.action == Event.keyset.ACTION_PRESS:
            self.keypresslog = chr(Event.key).capitalize() + " Pressed!\n" + self.keypresslog
        if Event.action == Event.keyset.ACTION_RELEASE:
            self.keyreleaselog = chr(Event.key).capitalize() + " Released!\n" + self.keyreleaselog

        # Another Key Press/Release Event Example
        if Event.action == Event.keyset.ACTION_PRESS:
            if Event.key == Event.keyset.H:
                print('Pressed H')
        if Event.action == Event.keyset.ACTION_RELEASE:
            if Event.key == Event.keyset.K:
                print("Released K")

        # Mouse Button Press/Release Events
        press = ""
        release = ""
        if Event.mouse_press:
            if Event.mouse_press == Event.mouse.left: press = "Left"
            if Event.mouse_press == Event.mouse.middle: press = "Middle"
            if Event.mouse_press == Event.mouse.right: press = "Right"
            self.mousepress = press + " Pressed!\n" + self.mousepress
        if Event.mouse_release:
            if Event.mouse_release == Event.mouse.left: release = "Left"
            if Event.mouse_release == Event.mouse.middle: release = "Middle"
            if Event.mouse_release == Event.mouse.right: release = "Right"
            self.mouserelease = release + " Released!\n" + self.mouserelease
        
    def process(self):
        # You may add any processing code here
        # Ex: Entity logic, algorithms, calculations
        pass

    def render(self):
        # Mainly used for OpenGL Functionality
        # Core.ctx is the moderngl context
        Core.ctx.clear(0.1, 0.1, 0.1, 1.0)

    def render_ui(self):
        # Mainly used for ImGui Functionality
        # However, may contain any other functionality as well
        # Remember that this function is called just after render()

        # Some ImGui Code

        imgui.begin("Debug")
        imgui.text("Cursor: " + str(Cursor.x) + ' ' + str(Cursor.y))
        imgui.text("Key Held: " + str(self.keys_held))
        imgui.text("Mouse Held: " + str(self.mouse_held))
        imgui.end()

        imgui.begin("Keylog")
        imgui.text(self.keypresslog)
        imgui.same_line()
        imgui.text("\t")
        imgui.same_line()
        imgui.text(self.keyreleaselog)
        imgui.end()

        imgui.begin("Mouselog")
        imgui.text(self.mousepress)
        imgui.same_line()
        imgui.text("\t")
        imgui.same_line()
        imgui.text(self.mouserelease)
        imgui.end()

# You may add or remove states anytime but it's recommended to 
# create a new state within the state's source file itself
# Then activate the state with Core.activate(state_id) later
Core.add(ExampleState)