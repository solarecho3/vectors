import manim


class EncodeText(manim.Scene):

    #
    def construct(self):
        quote = manim.Tex('Fall ', 'to ', 'thy ', 'prayers', '...').scale(1)

        # FADE IN: "Fall to the prayers..."
        # define the animations array as fadein
        animations = [
            manim.FadeIn(quote[0]),
            manim.FadeIn(quote[1]),
            manim.FadeIn(quote[2]),
            manim.FadeIn(quote[3]),
            manim.FadeIn(quote[4])
        ]
        # Fade in the animations array
        self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))
        self.wait(5)

        # FADE OUT: "Fall to the prayers..."
        animations = [
            manim.FadeOut(quote[0]),
            manim.FadeOut(quote[1]),
            manim.FadeOut(quote[2]),
            manim.FadeOut(quote[3]),
            manim.FadeOut(quote[4])
        ]
        self.play(manim.AnimationGroup(*animations))

        # FADE IN: "Fall_to_thy_prayers...\n"
        # expose all characters
        quote = manim.Tex('Fall', r' \_ ', 'to ', r'\_ ', 'thy ', r'\_ ', 'prayers ', '... ', r'\textbackslash n').scale(1)
        # define the animations for transformation
        animations = [
            manim.FadeIn(quote[0]),
            manim.FadeIn(quote[1]),
            manim.FadeIn(quote[2]),
            manim.FadeIn(quote[3]),
            manim.FadeIn(quote[4]),
            manim.FadeIn(quote[5]),
            manim.FadeIn(quote[6]),
            manim.FadeIn(quote[7]),
            manim.FadeIn(quote[8])
        ]
        self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))
        self.wait(3)

        # FADE OUT: "Fall_to_thy_prayers...\n"
        # define the next animations array as fadeout
        animations = [
            manim.FadeOut(quote[1]),
            manim.FadeOut(quote[2]),
            manim.FadeOut(quote[3]),
            manim.FadeOut(quote[4]),
            manim.FadeOut(quote[5]),
            manim.FadeOut(quote[6]),
            manim.FadeOut(quote[7]),
            manim.FadeOut(quote[8])
        ]
        # Fade out the animations array
        self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))

        # SCALE, SHIFT: "Fall"
        self.play(manim.ScaleInPlace(quote[0], 2))
        self.play(quote[0].animate.shift(manim.RIGHT*2.6))
        self.wait(3)

        # FADE OUT: "Fall"
        self.play(manim.Unwrite(quote[0]))

        # FADE IN: "18 39 50 50"
        quote = manim.Tex('18',',','39',',','50',',','50').scale(3)
        animations = [
            manim.Write(quote[0]),
            manim.Write(quote[1]),
            manim.Write(quote[2]),
            manim.Write(quote[3]),
            manim.Write(quote[4]),
            manim.Write(quote[5]),
            manim.Write(quote[6])
        ]
        self.play(manim.AnimationGroup(*animations, lag_ratio=0))
        self.wait(3)
        # FADE OUT: commas
        animations = [
            manim.FadeOut(quote[1]),
            manim.FadeOut(quote[3]),
            manim.FadeOut(quote[5])
        ]
        self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))
        # SPREAD OUT: "18   39   50   50"
        # self.play(quote[0].shift(manim.LEFT*2))
        # self.play(quote[2].shift(manim.LEFT))
        # self.play(quote[4].shift(manim.RIGHT))
        # self.play(quote[6].shift(manim.RIGHT*2))
        # self.play(quote[0].animate(run_time=.7).shift(manim.LEFT*2))
        # self.play(quote[2].animate(run_time=.7).shift(manim.LEFT*.5))
        # self.play(quote[6].animate(run_time=.7).shift(manim.RIGHT * 2))
        # self.play(quote[4].animate(run_time=.7).shift(manim.RIGHT * .5))
        animations = [
            quote[0].animate(run_time=.7).shift(manim.LEFT*2),
            quote[2].animate(run_time=.7).shift(manim.LEFT*.5),
            quote[6].animate(run_time=.7).shift(manim.RIGHT * 2),
            quote[4].animate(run_time=.7).shift(manim.RIGHT * .5)
        ]
        self.play(manim.AnimationGroup(*animations))

        # FADE IN: "F a l l "
        _quote1 = manim.Text("F").scale(1.7).next_to(quote[0], manim.DOWN*5)
        _quote2 = manim.Text("a").scale(1.7).next_to(quote[2], manim.DOWN*6)
        _quote3 = manim.Text("l").scale(1.7).next_to(quote[4], manim.DOWN*5)
        _quote4 = manim.Text("l").scale(1.7).next_to(quote[6], manim.DOWN*5)
        self.play(
            manim.ChangeSpeed(
                manim.FadeIn(_quote1),
                speedinfo={1:4}
            )
        )
        self.play(
            manim.ChangeSpeed(
                manim.FadeIn(_quote2),
                speedinfo={1:4}
            )
        )
        self.play(
            manim.ChangeSpeed(
                manim.FadeIn(_quote3),
                speedinfo={1:4}
            )
        )
        self.play(
            manim.ChangeSpeed(
                manim.FadeIn(_quote4),
                speedinfo={1:4}
            )
        )

        self.wait(1)
        animations = [
            manim.FadeOut(_quote1),
            manim.FadeOut(_quote2),
            manim.FadeOut(_quote3),
            manim.FadeOut(_quote4)
        ]

        self.play(manim.AnimationGroup(*animations))

        self.wait(3)
