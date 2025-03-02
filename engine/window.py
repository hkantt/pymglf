
from .config import *


class Cursor:

    # Access Mouse Coordinates

    x = 0
    y = 0


class EventMouseData:

    # Mouse Button Data

    left = 1
    right = 2
    middle = 3


class Event:

    # Event Manager
    # Refer ExampleState to understand how to use these attributes

    keyset = None
    key = None
    keys_held = []
    action = None
    modifiers = None
    mouse_press = None
    mouse_release = None
    mouse_held = []
    mouse = EventMouseData()

    @classmethod
    def refresh(cls):
        # Reset variables
        cls.key = None
        cls.action = None
        cls.modifiers = None
        cls.mouse_press = None
        cls.mouse_release = None


class Window(mglw.WindowConfig):

    # A modification of ModernGL Window's WindowConfig

    # Default settings
    gl_version = (3, 3)
    window_size = (1280, 720)
    title = "PyMGLF"
    aspect_ratio = None

    # Helper method (to be called before initializing Core):
    @classmethod
    def set_gl_ver(cls, major: int, minor: int):
        cls.gl_version = (major, minor)

    # Helper method (to be called before initializing Core):
    @classmethod
    def set_title(cls, title: str):
        cls.title = title

    # Helper method (to be called before initializing Core):
    @classmethod
    def set_size(cls, width: int, height: int):
        cls.window_size = (width, height)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.core = None
        self.event = None

    def _set_core(self, core):
        self.core = core

    def _set_event_manager(self, event_manager):
        self.event = event_manager

    # Run the Core's program loop
    def on_render(cls, time: float, frametime: float):
        if cls.core: cls.core.loop()

    # Update viewport
    def on_resize(self, width: int, height: int):
        self.ctx.viewport = (0, 0, width, height)
        if self.core:
            self.core.imgui_io.display_size = self.wnd.size
            self.core.imgui_io.display_framebuffer_scale = imgui_bundle.python_backends.compute_fb_scale(self.wnd.size, self.wnd.buffer_size)

    # Below: handle events and send information to Event

    def on_key_event(self, key, action, modifiers):
        if self.core: self.core.impl.key_event(key, action, modifiers)
        if self.event:
            self.event.key = key
            self.event.action = action
            self.event.modifiers = modifiers
            if action == self.event.keyset.ACTION_PRESS:
                if key not in self.event.keys_held:
                    self.event.keys_held.append(key)
            if action == self.event.keyset.ACTION_RELEASE:
                if key in self.event.keys_held:
                    self.event.keys_held.remove(key)

    def on_mouse_position_event(self, x, y, dx, dy):
        if self.core: self.core.impl.mouse_position_event(x, y, dx, dy)
        Cursor.x, Cursor.y = x, y

    def on_mouse_drag_event(self, x, y, dx, dy):
        if self.core: self.core.impl.mouse_drag_event(x, y, dx, dy)

    def on_mouse_scroll_event(self, x_offset, y_offset):
        if self.core: self.core.impl.mouse_scroll_event(x_offset, y_offset)

    def on_mouse_press_event(self, x, y, button):
        if self.core: self.core.impl.mouse_press_event(x, y, button)
        if self.event:
            self.event.mouse_press = button
            if button not in self.event.mouse_held:
                self.event.mouse_held.append(button)

    def on_mouse_release_event(self, x: int, y: int, button: int):
        if self.core: self.core.impl.mouse_release_event(x, y, button)
        if self.event:
            self.event.mouse_release = button
            if button in self.event.mouse_held:
                self.event.mouse_held.remove(button)

    def on_unicode_char_entered(self, char):
        if self.core: self.core.impl.unicode_char_entered(char)