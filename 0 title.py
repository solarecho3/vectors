import manim

class Title(manim.Scene):
    def construct(self):
        title = manim.MarkupText("An exploration of language, data, and encoding.", font_size=20)
        self.play(manim.FadeIn(title))
        # self.play(manim.ApplyWave(title))
        self.wait(5)
        self.play(manim.FadeOut(title))

        title = manim.MarkupText("by solarecho3\n\nmusic inspired by Kenji Kawai\n\nCover art by DALL-E, OpenAI", font_size=20, justify=True)
        self.play(manim.FadeIn(title))
        # self.play(manim.ApplyWave(title))
        self.wait(5)
        self.play(manim.FadeOut(title))
