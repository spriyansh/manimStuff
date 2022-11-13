################################################
# Author: spriyansh29@gmail.com ################
################################################
################ Description of Animation ######
# Simple logo for MANIM ########################
################################################

# Import the library
from manim import *

class header_manim(Scene):

    # Constructor for SLR plot
    def construct(self):

        # Make text Mobject
        head = Text('MANIM').scale(3)
        head2 = Text("Mathematical Animation Engine", 
                     t2c={'[0:1]':YELLOW, 
                          '[13:17]':YELLOW},
                     disable_ligatures=True).next_to(head, DOWN)
        
        # Add
        self.add(head, head2)

        # Play the animation
        self.play(
            Create(head, run_time=1),
            Create(head2 , run_time=1)
        )

        # Add wait time for animation
        self.wait(1)
