# PyMGLF (Integration Example)

## About
This is an attempt to create a structured framework for development 
of applications of any complexity within Python. This framework uses
ModernGL as an interface between Python and the GPU and GLFW for
window management and event handling. ImGui support has been provided.

## Installation
PyMGLF shall be cloned/downloaded and extracted as it is. This is NOT a Python library.<br>
Once downloaded, the application can be run through main.py with a Python 3.11+ interpreter.<br>
The following dependencies are required to run PyMGLF:
1. ModernGL: ```pip install moderngl```
2. GLFW: ```pip install glfw```
3. ImGui (with GLFW integrations): ```pip install imgui[glfw]```
4. Pyrr: ```pip install pyrr```
5. Pygame-CE (For audio playback): ```pip install pygame-ce```

## Credits
This project uses [moderngl](https://github.com/moderngl/moderngl), which is licensed under the MIT License.
Copyright (c) 2017-2024 Szabolcs Dombi, Einar Forselv<br>
This project uses [glfw](https://github.com/FlorianRhiem/pyGLFW), which is licensed under the MIT License.
Copyright (c) 2013-2019 Florian Rhiem<br>
This project uses [pyimgui](https://github.com/pyimgui/pyimgui), which is licensed under the BSD 3-Clause "New" or "Revised" License.
Copyright (c) 2016, Michał Jaworski<br>


## Licensing
PyMGLF is open-source and can be used for private/commercial purposes given that you include the LICENSE in your project.
