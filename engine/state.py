
from .window import *


class CoreState:

    # Template of a Core State

    def __init__(self, state_id: any):
        self.state_id = state_id

    def enter(self):
        # Called everytime the state is activated
        pass

    def events(self):
        # Identify events and take actions
        pass

    def process(self):
        # CPU based calculations occur here
        pass

    def render(self):
        # Draw content
        pass

    def render_ui(self):
        # Drawn after everything in render()
        pass

    def exit(self):
        # Called on the exiting state when a new state is queued for activation
        pass