
from .window import *


class State:

    def __init__(self, state_id: any):
        self.state_id = state_id

    def enter(self):
        pass

    def events(self):
        pass

    def process(self):
        pass

    def render(self):
        pass

    def render_ui(self):
        pass

    def exit(self):
        pass