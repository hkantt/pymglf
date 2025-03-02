
# System libraries
import sys
import math
import time
import random
import pathlib
import json

# Other libraries
import moderngl as mgl
from imgui_bundle import imgui
import imgui_bundle.python_backends
import moderngl_window as mglw
from moderngl_window.integrations.imgui_bundle import ModernglWindowRenderer


# Paths
CWD = pathlib.Path().cwd()
DATA_DIR = CWD.joinpath("data")
TEX_DIR = DATA_DIR.joinpath("textures")
SND_DIR = DATA_DIR.joinpath("sounds")