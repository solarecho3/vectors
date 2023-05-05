import manim
import numpy
import random


class EncodeText(manim.Scene):

    def construct(self):
        # scene 2 begins here
        # bring back the doc2 as white text
        # show the computer selecting context starting points
        # show the computer building a contextual vector
        # show the vectors as a growing spreadsheet
        # transform the spreadsheet to 3d
        # stack multiple spreadsheets together like files or a stack of paper
        # show how each is connected to the next
        self.next_section()

        # CREATE: doc2 encoded document
        doc2_text = """[18 39 50 57 58 39 44 44 10 1 25 63 1 49 47 52 45 6 1 51 63 1 22 53 60 
        43 2 1 21 1 57 54 43 39 49 1 58 53 1 58 46 43 43 6 1 51 63 1 46 43 39 
        56 58 2 1 23 47 52 45 1 20 43 52 56 63 1 34 10 1 21 1 49 52 53 61 1 58
        46 43 43 1 52 53 58 6 1 53 50 42 1 51 39 52 8 1 18 39 50 50 1 58 53 1
        58 46 63 1 54 56 39 63 43 56 57 8 1 20 53 61 1 47 50 50 1 61 46 47 58
        43 1 46 39 47 56 57 1 40 43 41 53 51 43 1 39 1 44 53 53 50 1 39 52 42
        1 48 43 57 58 43 56 2 ]"""
        doc2 = manim.Code(
            code=doc2_text,
            background="window",
            language="md",
            line_no_from=46,
            style=manim.Code.styles_list[15],
            font_size=20
        )
        self.play(manim.Write(doc2))
        self.wait(3)