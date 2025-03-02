
from states import *


# Configure the window
Window.set_gl_ver(3, 3)
Window.set_size(1280, 720)
Window.set_title("PyMGLF")

# Initialize Core
Core.init()

# Set an initial state
Core.activate("ExampleState")

# Run the core (Always call Core.run() last)
Core.run()