
from .config import *


class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    window_size = (1280, 720)
    aspect_ratio = None

    @classmethod
    def set_glv(cls, major: int, minor: int):
        cls.gl_version = (major, minor)

    @classmethod
    def set_size(cls, width: int, height: int):
        cls.window_size = (width, height)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.core = None

    def set_core(self, core):
        self.core = core

    def on_render(cls, time: float, frametime: float):
        if cls.core: cls.core.loop()

    def on_resize(self, width: int, height: int):
        self.ctx.viewport = (0, 0, width, height)
        if self.core:
            self.core.imgui_io.display_size = self.wnd.size
            self.core.imgui_io.display_framebuffer_scale = imgui_bundle.python_backends.compute_fb_scale(self.wnd.size, self.wnd.buffer_size)

    def on_key_event(self, key, action, modifiers):
        if self.core: self.core.imgui.key_event(key, action, modifiers)

    def on_mouse_position_event(self, x, y, dx, dy):
        if self.core: self.core.imgui.mouse_position_event(x, y, dx, dy)

    def on_mouse_drag_event(self, x, y, dx, dy):
        if self.core: self.core.imgui.mouse_drag_event(x, y, dx, dy)

    def on_mouse_scroll_event(self, x_offset, y_offset):
        if self.core: self.core.imgui.mouse_scroll_event(x_offset, y_offset)

    def on_mouse_press_event(self, x, y, button):
        if self.core: self.core.imgui.mouse_press_event(x, y, button)

    def on_mouse_release_event(self, x: int, y: int, button: int):
        if self.core: self.core.imgui.mouse_release_event(x, y, button)

    def on_unicode_char_entered(self, char):
        if self.core: self.core.imgui.unicode_char_entered(char)