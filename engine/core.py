
from .state import *


class Core:

    # ModernGL Context
    ctx = None

    # ImGui ModernGL implementation
    impl = None

    # Imgui IO
    imgui_io = None

    # States are stored here
    states = {}
    
    # The state being looped on
    active_s = None

    # The state queued for activation
    queued_s = None

    @classmethod
    def add(cls, state: State):
        """Creates a state instance and stores it for later use"""
        s = state()
        if s.state_id in cls.states.keys():
            return
        cls.states[s.state_id] = s

    @classmethod
    def remove(cls, state_id: any):
        """Deletes a state instance completely"""
        if state_id in cls.states.keys():
            del cls.states[state_id]
        else:
            print("No state referring to ID: ", state_id)

    @classmethod
    def activate(cls, state_id: any):
        """Queues a state for activation"""
        if state_id in cls.states.keys():
            cls.queued_s = cls.states[state_id]
        else:
            print("No state referring to ID: ", state_id)

    @classmethod
    def _framebuffer_callback(cls, window, width, height):
        cls.ctx.viewport = (0, 0, width, height)
        cls.imgui_io.display_size = (width, height)

    @classmethod
    def run(cls):
        cls.ctx = mgl.create_context()
        imgui.create_context()
        cls.impl = GlfwRenderer(Window._window)
        cls.imgui_io = imgui.get_io()
        glfw.set_framebuffer_size_callback(Window._window, cls._framebuffer_callback)
        Event.init(cls)
        while not glfw.window_should_close(Window._window):
            if cls.queued_s:
                if cls.active_s:
                    cls.active_s.exit()
                cls.active_s = cls.queued_s
                cls.active_s.enter()
                cls.queued_s = None
            cls.events()
            cls.process()
            cls.render()
        cls.terminate()

    @classmethod
    def events(cls):
        """Event handling"""
        if cls.active_s:
            cls.active_s.events()

    @classmethod
    def process(cls):
        """CPU based calculations"""
        if cls.active_s:
            cls.active_s.process()

    @classmethod
    def render(cls):
        """Overall render order"""
        cls.ctx.clear(0.1, 0.1, 0.1, 1.0)
        imgui.new_frame()
        if cls.active_s:
            cls.active_s.render()
            cls.active_s.render_ui()
        imgui.render()
        cls.impl.render(imgui.get_draw_data())
        Event.refresh()
        Window.refresh()
        cls.impl.process_inputs()

    @classmethod
    def terminate(cls):
        cls.impl.shutdown()
        Window.destroy()
        glfw.terminate()
        sys.exit()