
from .libs import *


class Window:

    _window = None
    gl_major = 3
    gl_minor = 3

    @classmethod
    def set_opengl_version(cls, major: int, minor: int):
        cls.gl_major = major
        cls.gl_minor = minor

    @classmethod
    def create(cls, width: int, height: int, title: str):
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, cls.gl_major)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, cls.gl_minor)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        cls._window = glfw.create_window(width, height, title, None, None)
        glfw.make_context_current(cls._window)
        glfw.swap_interval(1)

    @classmethod
    def refresh(cls):
        glfw.swap_buffers(cls._window)
        glfw.poll_events()

    @classmethod
    def destroy(cls):
        glfw.destroy_window(cls._window)


class Cursor:

    x = 0
    y = 0
    xoffset = 0
    yoffset = 0


class Event:

    core = None
    key = None
    scancode = None
    action = None
    mods = None
    button = None
    kstate = []
    bstate = []

    @classmethod
    def init(cls, core):
        cls.core = core
        glfw.set_key_callback(Window._window, cls._key_callback)
        glfw.set_cursor_pos_callback(Window._window, cls._cursor_callback)
        glfw.set_mouse_button_callback(Window._window, cls._mouse_button_callback)
        glfw.set_scroll_callback(Window._window, cls._scroll_callback)

    @classmethod
    def _cursor_callback(cls, window, xpos, ypos):
        Cursor.x, Cursor.y = xpos, ypos

    @classmethod
    def _mouse_button_callback(cls, window, button, action, mods):
        cls.button = button
        cls.action = action
        cls.mods = mods

        if action == glfw.PRESS:
            if button not in cls.bstate:
                cls.bstate.append(button)
            cls.core.imgui_io.mouse_down[button] = True
        if action == glfw.RELEASE:
            if button in cls.bstate:
                cls.bstate.remove(button)
            cls.core.imgui_io.mouse_down[button] = False

        cls.core.imgui_io.key_ctrl = mods & glfw.MOD_CONTROL
        cls.core.imgui_io.key_shift = mods & glfw.MOD_SHIFT
        cls.core.imgui_io.key_alt = mods & glfw.MOD_ALT
        cls.core.imgui_io.key_super = mods & glfw.MOD_SUPER

    @classmethod
    def _scroll_callback(cls, window, xoffset, yoffset):
        cls.core.imgui_io.mouse_wheel += yoffset
        Cursor.xoffset = xoffset
        Cursor.yoffset = yoffset

    @classmethod
    def _key_callback(cls, window, key, scancode, action, mods):
        cls.key = key
        cls.scancode = scancode
        cls.action = action
        cls.mods = mods
        
        if action == glfw.PRESS:
            if key not in cls.kstate:
                cls.kstate.append(key)
            cls.core.imgui_io.keys_down[key] = True
        if action == glfw.RELEASE:
            if key in cls.kstate:
                cls.kstate.remove(key)
            cls.core.imgui_io.keys_down[key] = False

        cls.core.imgui_io.key_ctrl = mods & glfw.MOD_CONTROL
        cls.core.imgui_io.key_shift = mods & glfw.MOD_SHIFT
        cls.core.imgui_io.key_alt = mods & glfw.MOD_ALT
        cls.core.imgui_io.key_super = mods & glfw.MOD_SUPER

    @classmethod
    def refresh(cls):
        cls.key = None
        cls.scancode = None
        cls.action = None
        cls.mods = None
        cls.button = None
        Cursor.xoffset = 0
        Cursor.yoffset = 0