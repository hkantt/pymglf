
# System libraries
import os
import sys
import math
import time
import json
import random
import pathlib
import ctypes
from tkinter import filedialog as tk_filedialog

# Other libraries
import numpy as np
import pyrr
import glfw
import moderngl as mgl
import imgui
from imgui.integrations.glfw import GlfwRenderer
import pygame.mixer as pgmix


# Paths
CWD = pathlib.Path().cwd()
DATA_DIR = CWD.joinpath("data")
TEX_DIR = DATA_DIR.joinpath("textures")
SND_DIR = DATA_DIR.joinpath("sounds")