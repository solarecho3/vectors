import manim
import numpy
import random

class EncodeText(manim.Scene):

    #
    def construct(self):
        _quote = manim.Tex('\"', 'Fall ', 'to ', 'thy ', 'prayers', '...', '\"').scale(1)
        quote_name = manim.Tex("- William Shakespeare").shift([3.0,-1.0,0]).scale(.5)

        # FADE IN: "Fall to the prayers..."
        # define the animations array as fadein
        animations = [
            manim.FadeIn(_quote[0]),
            manim.FadeIn(_quote[1]),
            manim.FadeIn(_quote[2]),
            manim.FadeIn(_quote[3]),
            manim.FadeIn(_quote[4]),
            manim.FadeIn(_quote[5]),
            manim.FadeIn(_quote[6]),
            manim.FadeIn(quote_name)
        ]
        # Fade in the animations array
        self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))
        self.wait(9)

        # FADE OUT: "Fall to the prayers..."
        animations = [
            manim.FadeOut(_quote[0]),
            manim.FadeOut(_quote[1]),
            manim.FadeOut(_quote[2]),
            manim.FadeOut(_quote[3]),
            manim.FadeOut(_quote[4]),
            manim.FadeOut(_quote[5]),
            manim.FadeOut(_quote[6]),
            manim.FadeOut(quote_name),
        ]
        self.play(manim.AnimationGroup(*animations))