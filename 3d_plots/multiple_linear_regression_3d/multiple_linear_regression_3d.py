#############################################################
# Author: spriyansh29@gmail.com #############################
#############################################################
################ Description of Animation ###################
# A multiple regression 3-d plot with dots and a line #######
# Concept Explained: Multiple Linear Regression #############
#############################################################

# Import the library
from manim import *
import numpy as np

# Set the background colour
config.background_color = WHITE

# Create Class for Simple Linear Regression
class MLR(ThreeDScene):

    # Constructor for SLR plot
    def construct(self):

        # Make axes mobject
        ax = (
            ThreeDAxes(
                # 3b1b Manim's Isssue
                x_length=5, y_length=5, z_length=5,
                # Set the range for both axis
                x_range=[0, 10, 2],
                y_range=[0, 10, 2],
                z_range=[0, 10, 2],
                color=BLACK,
                x_axis_config={
                    "color": BLACK,  # Line color
                    "stroke_width": 2,  # Width of line
                    "include_numbers": True,
                },
                y_axis_config={
                    "color": BLACK,  # Line color
                    "stroke_width": 2,  # Width of line
                    "include_numbers": True,
                },
                z_axis_config={
                    "color": BLACK,  # Line color
                    "stroke_width": 2,  # Width of line
                    "include_numbers": True,
                }
                # Add Coordinates with color
            )
            .add_coordinates()
            .set_color(BLACK)
        )

        # Add dot mobjects
        origin = Dot(point=np.array([0, 0, 0]), radius=0.08, color=RED)
        
        dot1 = Dot(point=np.array([-5, -2.1, 2]), radius=0.08, color=BLUE)
        dot2 = Dot(point=np.array([-4, -1.7, 0]), radius=0.08, color=BLUE)
        dot3 = Dot(point=np.array([-3, -1, 0]), radius=0.08, color=BLUE)
        dot4 = Dot(point=np.array([-2, -0.8, 0]), radius=0.08, color=BLUE)
        dot5 = Dot(point=np.array([-1, 2, 0]), radius=0.08, color=BLUE)
        dot6 = Dot(point=np.array([0, -0.2, 0]), radius=0.08, color=BLUE)
        dot7 = Dot(point=np.array([1, 1.6, 0]), radius=0.08, color=BLUE)
        dot8 = Dot(point=np.array([2, 2.1, 0]), radius=0.08, color=BLUE)

        # Add Labels with black color
        x_label = ax.get_x_axis_label("Predictor(x1_{i})").set_color(BLACK)
        y_label = ax.get_y_axis_label("Response(y_{i})").set_color(BLACK)
        z_label = ax.get_z_axis_label("Predictor(x2_{i})").set_color(BLACK)

        # Add grid system for easier editing
        # Should be removed in production
        for x in range(-10, 10): # Range of x
            for y in range(-10, 10): # Range of y
             # Add dot objects
                 self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
                 

        # Line of best fit
        func_graph_cube = ax.plot(lambda x1: x, x_range=[0, 5], color=RED_B)
        
        # Area
        area = ax.get_area(
            func_graph_cube ,
            x_range=(PI / 2, 3 * PI / 2),
            z_range= (PI / 2, 3 * PI / 2),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )

        # Add the mobject with axes
        self.add(ax, func_graph_cube, area)
        
        # Begin
        self.begin_ambient_camera_rotation(rate=0.3)

        # Play the animation
        self.play(
            # Add axes
            Create(ax, run_time=3, reverse_rate_function=False),
            # Add Line of best fit
            Create(func_graph_cube, run_time=3),
            # Add dots
            Create(origin),# Only while editing, remove in production
            Create(dot1),
            Create(dot2),
            Create(dot3),
            Create(dot4),
            Create(dot5),
            Create(dot6),
            Create(dot7),
            Create(dot8),
            
            # Add labels
            Create(x_label),
            Create(y_label),
            Create(z_label),
            Create(area)
        )
        
        self.move_camera(phi =60 * DEGREES)
        self.move_camera(theta = -45 * DEGREES)
        
        self.stop_ambient_camera_rotation()

        # Add wait time for animation
        self.wait(1)
