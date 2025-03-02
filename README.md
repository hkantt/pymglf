# PyMGLF
Python ModernGL Framework v1.0 <br>
In development since: 1st March, 2025
![Image](https://github.com/user-attachments/assets/c84288bf-ecc1-401b-b288-d42472a9d061)

## About
This is an attempt to create a structured framework for development 
of applications of any complexity within Python. This framework uses
ModernGL as an interface between Python and the GPU and ModernGL Window
for window management, event handling and resource management. ImGui
support has been provided.
<br><br>
Below we mention few important points regarding which this framework
is being developed:
<br>
#### 1. Hybrid control over the application's functioning:
   This framework aims to provide a lot of abstraction for speeding up
   2D and 3D graphics development while retaining fine-grained control over
   OpenGL via ModernGL.
#### 2. An organized development environment:
   This framework utilizes a state-based architecture to minimize headache
   caused by spaghetti code. It aims to allow beginners to make complex apps
   with minimal chances of mismanagement by the use of states, based on
   modular programming.
#### 3. Easier collaboration:
   This framework implements states in such a way that it becomes possible to simply send
   a single state file to a team member and let them run it with minimal tweaking. Thus,
   turning each state file into a mini program, runnable by PyMGLF. Communication among
   states is possible as well.
#### 4. Accessibility and AI:
   This framework aims to retain a Pythonic approach to programming. Thus, it becomes very
   easy for beginners to get started with OpenGL with PyMGLF. Python has a good support
   for AI development, thus opening doors for implementing AI into graphics in the future.
#### 5. A thought about performance:
   Python is often compared with other faster compiled languages such as C, C++ and C#.
   However, a language's performance depends on how it is used. In this framework, Python
   acts as an instructor to the GPU, giving orders, but not performing them on its own.

## Installation
PyMGLF shall be cloned/downloaded as zip and extracted as it is. This is NOT a Python library.<br>
Once downloaded, the application can be run simply through running main.py with a Python 3.11+ interpreter.<br>
The following dependencies are required to run PyMGLF:
1. ModernGL: ```pip install moderngl```
2. ModernGL Window: ```pip install moderngl-window```
3. ImGui Bundle: ```pip install imgui-bundle```

## Licensing
PyMGLF is open-source and can be used for private/commercial purposes given that you include the LICENSE in your project.
