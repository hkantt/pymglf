
from .state import *


class Core:
    
    # The Core
    # Integrates components of the framework under one hood
    # Acts as the global State Machine / State Handler

    # Reference to the ModernGL Window
    win_conf_inst = None

    # Reference to the ModernGL Context
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

    # Must be called only after setting up Window attributes
    @classmethod
    def init(cls):
        cls.win_conf_inst = mglw.create_window_config_instance(Window)
        cls.win_conf_inst._set_core(cls)
        cls.win_conf_inst._set_event_manager(Event)
        cls.ctx = cls.win_conf_inst.ctx
        imgui.create_context()
        cls.impl = ModernglWindowRenderer(cls.win_conf_inst.wnd)
        cls.imgui_io = imgui.get_io()

    # Creates a state instance and stores it for later use
    @classmethod
    def add(cls, state: CoreState):
        s = state()
        if s.state_id in cls.states.keys():
            return
        cls.states[s.state_id] = s

    # Deletes a state instance completely
    @classmethod
    def remove(cls, state_id: any):
        if state_id in cls.states.keys():
            del cls.states[state_id]
        else:
            print("No state referring to ID: ", state_id)

    # Queues a state for activation
    # Why queue states ?
    # Queueing the state ensures a smooth bug-free transition between states
    # State switching happens at a specified point in the loop always
    # State exit and entrance are properly handled while switching
    # Thus preventing missing variable errors and other mishaps
    @classmethod
    def activate(cls, state_id: any):
        if state_id in cls.states.keys():
            cls.queued_s = cls.states[state_id]
        else:
            print("No state referring to ID: ", state_id)

    # State switching code
    @classmethod
    def state_check(cls):
        if cls.queued_s:
            if cls.active_s:
                cls.active_s.exit()
            cls.active_s = cls.queued_s
            cls.active_s.enter()
            cls.queued_s = None

    # Run the moderngl window's WindowConfig instance
    @classmethod
    def run(cls):
        mglw.run_window_config_instance(cls.win_conf_inst)

    # Program Loop
    @classmethod
    def loop(cls):
        cls.state_check()
        cls.events()
        cls.process()
        cls.render()

    # Event handling
    @classmethod
    def events(cls):
        Event.keyset = cls.win_conf_inst.wnd.keys
        if cls.active_s:
            cls.active_s.events()

    # CPU based calculations
    @classmethod
    def process(cls):
        if cls.active_s:
            cls.active_s.process()

    # Overall render order
    @classmethod
    def render(cls):
        cls.ctx.clear(0.0, 0.0, 0.0, 1.0)
        if cls.active_s:
            cls.active_s.render()
        imgui.new_frame()
        if cls.active_s:
            cls.active_s.render_ui()
        imgui.render()
        cls.impl.render(imgui.get_draw_data())
        Event.refresh()

    @classmethod
    def exit(cls):
        sys.exit()