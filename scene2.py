import manim
# import numpy
import random


class EncodeText(manim.Scene):

    def construct(self):
        # DRAW IN: bounding box while:
        # DRAW IN: selected array
        # r1 = manim.Rectangle(width=3.35, height=0.3, color='#ff5370').shift(manim.LEFT * .85 + manim.UP * .135)
        t0 = manim.DecimalTable(
            [[52, 45, 1, 20, 43, 52, 56, 63]],
            row_labels=[manim.MathTex('block_0')],
            include_outer_lines=True
        ).scale(.7)
        animations = [
            # manim.Write(r1),
            manim.FadeIn(t0),
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(5)

        '''
        Now, we repeat our process of selecting a random starting point
        and building an array of 
        '''

        _templist = []
        for i in range(3):
            _templist.append(
                manim.DecimalTable(
                    # [[52, 45, 1, 20, 43, 52, 56, 63]],
                    [[random.randint(0,68) for i in range(8)]],
                    row_labels=[manim.MathTex(f'block_{i+1}')],
                    include_outer_lines=True,
                ).scale(.7)
            )
            _templist[i].width = t0.width

        for idx,item in enumerate(_templist):
            _i = idx+1
            self.play(manim.Write(item.shift(manim.DOWN * _i)))

        self.wait(5)