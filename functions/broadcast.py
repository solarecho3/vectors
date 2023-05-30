from manim import *
import numpy
# from manim.utils.color import Colors
class C(Scene):
    def construct(self):
        colors = ['#3174f0', '#e53125', '#fbb003', '#269a43', '#9c27b0', '#607d8b', '#ffcb6b']

        random_color1 = numpy.random.choice(colors, replace=False)
        mob1 = Circle(radius=5, color=random_color1)

        random_color2 = numpy.random.choice(colors, replace=False)
        mob2 = Circle(radius=5, color=random_color2)

        random_color3 = numpy.random.choice(colors, replace=False)
        mob3 = Circle(radius=5, color=random_color3)

        random_color4 = numpy.random.choice(colors, replace=False)
        mob4 = Circle(radius=5, color=random_color4)

        random_color5 = numpy.random.choice(colors, replace=False)
        mob5 = Circle(radius=5, color=random_color5)

        random_color6 = numpy.random.choice(colors, replace=False)
        mob6 = Circle(radius=5, color=random_color6)

        random_color7 = numpy.random.choice(colors, replace=False)
        mob7 = Circle(radius=5, color=random_color7)

        random_color8 = numpy.random.choice(colors, replace=False)
        mob8 = Circle(radius=5, color=random_color8)

        random_color9 = numpy.random.choice(colors, replace=False)
        mob9 = Circle(radius=5, color=random_color9)

        animations = [
            Broadcast(mob1, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob2, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob3, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob4, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob5, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob6, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob7, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob8, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
            Broadcast(mob9, n_mobs=numpy.random.randint(5,10), run_time=numpy.random.randint(6,12)),
        ]

        self.play(AnimationGroup(*animations))
