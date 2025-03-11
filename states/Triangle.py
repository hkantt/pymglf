
from engine import *


class Triangle(State):

    def __init__(self):
        super().__init__("Triangle")

    def get_view_matrix(self):
        scale_matrix = pyrr.Matrix44.from_scale([self.camera_zoom, self.camera_zoom, 1.0])
        translation_matrix = pyrr.Matrix44.from_translation(-self.camera_pos)
        return translation_matrix @ scale_matrix

    def enter(self):
        # Scale imgui
        Core.imgui_io.font_global_scale = 2

        # Camera position and zoom level
        self.camera_pos = pyrr.Vector3([0, 0, 0])
        self.camera_zoom = 1.0

        # Triangle data
        self.vertices = np.array([
            -200, -116,  1.0, 1.0, 1.0,
            200, -116,   0.0, 1.0, 0.0,
            0, 232,      1.0, 1.0, 1.0
        ], dtype='f4')
        self.vbo = Core.ctx.buffer(self.vertices.tobytes())

        # Compile shader program
        self.prog = Core.ctx.program(
            vertex_shader = """
            #version 330 core
            in vec2 in_vert;
            in vec3 in_color;
            out vec3 fragColor;

            uniform mat4 transform;
            uniform mat4 projection;
            uniform mat4 view;

            void main()
            {
                gl_Position = projection * view * transform * vec4(in_vert, 0.0, 1.0);
                fragColor = in_color;
            }
            """,
            fragment_shader = """
            #version 330 core
            in vec3 fragColor;
            out vec4 outColor;

            uniform mat4 color_transform;

            void main()
            {
                outColor = color_transform * vec4(fragColor, 1.0);
            }
            """
        )

        # Orthogonal projection matrix for 2D pixel coords --> NDC
        self.ortho_projection = pyrr.Matrix44.orthogonal_projection(-Window.w // 2, Window.w // 2, -Window.h // 2, Window.h // 2, -1, 1)
        self.prog['projection'].write(self.ortho_projection.astype('f4').tobytes())
        
        # Camera view matrix
        self.prog['view'].write(self.get_view_matrix().astype('f4').tobytes())
        
        # Time periods for rotation matrices
        self.time_period = 1
        self.color_time_period = 1

        # Angles of rotation matrices
        self.angle = 0
        self.color_angle = 0

        # No. of revolutions completed
        self.rev = 0

        # Increase number of simultaneously usable channels and load sound
        pgmix.set_num_channels(128)
        self.rev_sound = pgmix.Sound(SND_DIR.joinpath("rev.wav"))

        # Triangle VAO
        self.vao = Core.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def exit(self):
        # Reset settings
        Core.imgui_io.font_global_scale = 1.0
        pgmix.set_num_channels(8)

    def events(self):
        # Move the camera
        if glfw.KEY_LEFT in Event.kstate:
            self.camera_pos.x -= 5.0
        if glfw.KEY_RIGHT in Event.kstate:
            self.camera_pos.x += 5.0
        if glfw.KEY_UP in Event.kstate:
            self.camera_pos.y += 5.0
        if glfw.KEY_DOWN in Event.kstate:
            self.camera_pos.y -= 5.0
        if Event.kstate:
            self.prog['view'].write(self.get_view_matrix().astype('f4').tobytes())

        # Zoom in and out
        if Cursor.yoffset > 0:
            self.camera_zoom *= 1.1
        elif Cursor.yoffset < 0:
            self.camera_zoom /= 1.1
        self.camera_zoom = max(0.1, min(self.camera_zoom, 5.0))
        if Cursor.yoffset:
            self.prog['view'].write(self.get_view_matrix().astype('f4').tobytes())

    def process(self):
        # Rotate the triangle and colors
        self.angle += (2 * np.pi / self.time_period) * Clock.dt
        self.color_angle += (2 * np.pi / self.color_time_period) * Clock.dt
        rotation_matrix = pyrr.Matrix44.from_z_rotation(self.angle)
        color_rotation_matrix = pyrr.Matrix44.from_z_rotation(self.color_angle)
        self.prog['transform'].write(rotation_matrix.astype('f4').tobytes())
        self.prog['color_transform'].write(color_rotation_matrix.astype('f4').tobytes())

        # Revolution Completion Sound
        if self.angle / (2 * np.pi) > self.rev:
            self.rev += 1
            self.rev_sound.play()

    def render(self):
        Core.ctx.clear(0.0, 0.0, 0.0, 1.0)
        # Render the triangle
        self.vao.render(mgl.TRIANGLES)

    def render_ui(self):
        # UI code for imgui
        imgui.begin("Triangle", flags=imgui.WINDOW_ALWAYS_AUTO_RESIZE)
        imgui.text("Time Period")
        _, self.time_period = imgui.slider_float("", self.time_period, 0.02, 2.0, format="%.2f")
        imgui.text("\nColor Time Period")
        _, self.color_time_period = imgui.slider_float(" ", self.color_time_period, 0.2, 2.0, format="%.2f")
        imgui.end()

Core.add(Triangle)