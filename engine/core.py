
from .state import *


class Core:

    win_con_inst = None
    ctx = None
    imgui = None
    imgui_io = None
    states = {}
    active_s = None
    queued_s = None

    @classmethod
    def init(cls):
        cls.win_conf_inst = mglw.create_window_config_instance(Window)
        cls.win_conf_inst.set_core(cls)
        cls.ctx = cls.win_conf_inst.ctx
        imgui.create_context()
        cls.imgui = ModernglWindowRenderer(cls.win_conf_inst.wnd)
        cls.imgui_io = imgui.get_io()

    @classmethod
    def add(cls, state: State):
        s = state()
        if s.state_id in cls.states.keys():
            return
        cls.states[s.state_id] = s

    @classmethod
    def remove(cls, state_id: any):
        if state_id in cls.states.keys():
            del cls.states[state_id]
        else:
            print("No state referring to ID: ", state_id)

    @classmethod
    def activate(cls, state_id: any):
        if state_id in cls.states.keys():
            cls.queued_s = cls.states[state_id]
        else:
            print("No state referring to ID: ", state_id)

    @classmethod
    def state_check(cls):
        if cls.queued_s:
            if cls.active_s:
                cls.active_s.exit()
            cls.active_s = cls.queued_s
            cls.active_s.enter()
            cls.queued_s = None

    @classmethod
    def run(cls):
        mglw.run_window_config_instance(cls.win_conf_inst)

    @classmethod
    def loop(cls):
        cls.state_check()
        cls.events()
        cls.process()
        cls.render()

    @classmethod
    def events(cls):
        if cls.active_s:
            cls.active_s.events()

    @classmethod
    def process(cls):
        if cls.active_s:
            cls.active_s.process()

    @classmethod
    def render(cls):
        cls.ctx.clear(0.1, 0.1, 0.1, 1.0)
        if cls.active_s:
            cls.active_s.render()
        imgui.new_frame()
        if cls.active_s:
            cls.active_s.render_ui()
        imgui.render()
        cls.imgui.render(imgui.get_draw_data())

    @classmethod
    def exit(cls):
        sys.exit()