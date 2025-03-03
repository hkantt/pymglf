
from .window import *


class State:

    """State Template"""

    def __init__(self, state_id: any):
        self.state_id = state_id

    def enter(self):
        """Called everytime the state is activated"""
        pass

    def events(self):
        """Identify events and take actions"""
        pass

    def process(self):
        """CPU based calculations occur here"""
        pass

    def render(self):
        """Main render function"""
        pass

    def render_ui(self):
        """Secondary render function"""
        pass

    def exit(self):
        """Called on the exiting state when a new state is queued for activation"""
        pass