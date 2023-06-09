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
        self.wait(5)

        animations = [
            manim.FadeOut(quote_name),
            manim.FadeOut(_quote[0]),
            manim.FadeOut(_quote[6]),
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(2)

        # FADE OUT: "Fall to the prayers..."
        animations = [
            manim.FadeOut(_quote[1]),
            manim.FadeOut(_quote[2]),
            manim.FadeOut(_quote[3]),
            manim.FadeOut(_quote[4]),
            manim.FadeOut(_quote[5]),
        ]
        # self.play(manim.AnimationGroup(*animations))

        # FADE IN: "Fall_to_thy_prayers...\n"
        # expose all characters
        quote = manim.Tex('Fall', r'\_', 'to', r'\_', 'thy', r'\_', 'prayers', '...', r'\textbackslash n').scale(1)
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
        # self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))
        # delete the quotes from the list
        self.play(manim.FadeTransform(_quote[1:6], quote))
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
        self.play(quote[0].animate.shift(manim.RIGHT*2))
        self.wait(3)

        # FADE OUT: "Fall"
        self.play(manim.FadeOut(quote[0], shift=manim.DOWN))

        # FADE IN: Encoding table
        # FADE COLOR: Encoded text
        # FADE OUT: Encoding table
        t1 = manim.Table(
            [['F', 'a', 'l', 'l'],
             ['18', '39', '50', '50']],
            row_labels=[manim.Text("Letters"), manim.Text("Integers")],
            include_outer_lines=True
        )
        t1.add(t1.get_cell((1, 2), color='#3174f0'))
        t1.add(t1.get_cell((2, 2), color='#3174f0'))
        t1.add(t1.get_cell((1, 3), color='#e53125'))
        t1.add(t1.get_cell((2, 3), color='#e53125'))
        t1.add(t1.get_cell((1, 4), color='#fbb003'))
        t1.add(t1.get_cell((2, 4), color='#fbb003'))
        t1.add(t1.get_cell((1, 5), color='#fbb003'))
        t1.add(t1.get_cell((2, 5), color='#fbb003'))
        t1.get_entries(pos=(1, 2)).set_color('#3174f0')
        t1.get_entries(pos=(1, 3)).set_color('#e53125')
        t1.get_entries(pos=(1, 4)).set_color('#fbb003')
        t1.get_entries(pos=(1, 5)).set_color('#fbb003')
        t1.get_entries(pos=(2, 2)).set_color('#3174f0')
        t1.get_entries(pos=(2, 3)).set_color('#e53125')
        t1.get_entries(pos=(2, 4)).set_color('#fbb003')
        t1.get_entries(pos=(2, 5)).set_color('#fbb003')
        self.play(manim.Write(t1))
        self.wait(4)
        # self.play(manim.Unwrite(t1))

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
        quote[0].color = '#3174f0'
        quote[2].color = '#e53125'
        quote[4].color = '#fbb003'
        quote[6].color = '#fbb003'
        # self.play(manim.AnimationGroup(*animations, lag_ratio=0))
        # self.wait(3)

        self.play(manim.FadeTransform(t1, quote))
        # FADE OUT: commas
        animations = [
            manim.FadeOut(quote[1]),
            manim.FadeOut(quote[3]),
            manim.FadeOut(quote[5])
        ]
        self.play(manim.AnimationGroup(*animations, lag_ratio=0.2))
        # SPREAD OUT: "18   39   50   50"
        animations = [
            quote[0].animate(run_time=.7).shift(manim.LEFT*2),
            quote[2].animate(run_time=.7).shift(manim.LEFT*.5),
            quote[6].animate(run_time=.7).shift(manim.RIGHT * 2),
            quote[4].animate(run_time=.7).shift(manim.RIGHT * .5)
        ]
        self.play(manim.AnimationGroup(*animations))

        # FADE IN: "F a l l "
        _quote1 = manim.Text("F").scale(1.7).next_to(quote[0], manim.DOWN*5).set_color('#3174f0')
        _quote2 = manim.Text("a").scale(1.7).next_to(quote[2], manim.DOWN*6).set_color('#e53125')
        _quote3 = manim.Text("l").scale(1.7).next_to(quote[4], manim.DOWN*5).set_color('#fbb003')
        _quote4 = manim.Text("l").scale(1.7).next_to(quote[6], manim.DOWN*5).set_color('#fbb003')
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
        self.wait(3)

        # FADE OUT: " F a l l "
        animations = [
            manim.FadeOut(_quote1),
            manim.FadeOut(_quote2),
            manim.FadeOut(_quote3),
            manim.FadeOut(_quote4)
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(1)

        # draw brace and label
        brace1 = manim.BraceBetweenPoints([-5,-1,0], [5,-1,0], sharpness=0.7)
        brace1_txt = manim.Text('"encoded"').next_to(brace1, manim.DOWN*3)
        self.play(manim.GrowFromCenter(brace1))
        self.play(manim.FadeIn(brace1_txt))
        # randomly select a different index of the string to change color
        for i in range(50):
            colors = ['#3174f0','#e53125','#fbb003','#269a43']
            self.play(
                manim.ChangeSpeed(
                    manim.FadeToColor(
                        brace1_txt[numpy.random.randint(1,8)],
                        color=numpy.random.choice(colors)
                    ),
                    speedinfo={.01:50}
                )
            )
        # set final color scheme to match encoded integers
        brace1_txt[1].set_color('#3174f0')
        brace1_txt[2].set_color('#e53125')
        brace1_txt[3].set_color('#e53125')
        brace1_txt[4].set_color('#e53125')
        brace1_txt[5].set_color('#fbb003')
        brace1_txt[6].set_color('#fbb003')
        brace1_txt[7].set_color('#fbb003')
        self.wait(5)

        # FADE OUT: Brace and brace text
        animations = [
            manim.FadeOut(brace1),
            manim.FadeOut(brace1_txt)
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(3)

        # FADE COLOR: Encoded text fade to white, wait 3
        animations = [
            manim.FadeToColor(quote[0], color=manim.WHITE),
            manim.FadeToColor(quote[2], color=manim.WHITE),
            manim.FadeToColor(quote[4], color=manim.WHITE),
            manim.FadeToColor(quote[6], color=manim.WHITE),
        ]
        self.play(manim.AnimationGroup(*animations))
        # self.wait(1)

        # SPREAD IN: "18 39 50 50"
        # FADE IN: Commas
        animations = [
            quote[0].animate(run_time=.7).shift(manim.RIGHT * 2),
            quote[2].animate(run_time=.7).shift(manim.RIGHT * .5),
            quote[6].animate(run_time=.7).shift(manim.LEFT * 2),
            quote[4].animate(run_time=.7).shift(manim.LEFT * .5),
            manim.FadeIn(quote[1]),
            manim.FadeIn(quote[3]),
            manim.FadeIn(quote[5]),
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(3)

        # FADE IN: Brackets of the array
        bracket1 = manim.Tex("[", "]").scale(3)
        brace_2 = manim.BraceLabel(quote, "array", buff=.5)
        animations = [
            manim.FadeIn(bracket1[0], shift=manim.LEFT*5),
            manim.FadeIn(bracket1[1], shift=manim.RIGHT*5),
            bracket1[0].animate(run_time=.7).shift(manim.LEFT*3.7, manim.UP*.1),
            bracket1[1].animate(run_time=.7).shift(manim.RIGHT*3.7, manim.UP*.1),
            manim.FadeIn(brace_2)
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(3)

        # FADE TO COLOR: Encoded text back to color
        animations = [
            manim.FadeToColor(quote[0], color='#3174f0'),
            manim.FadeToColor(quote[2], color='#e53125'),
            manim.FadeToColor(quote[4], color='#fbb003'),
            manim.FadeToColor(quote[6], color='#fbb003')
        ]
        self.play(manim.AnimationGroup(*animations))

        # FADE OUT: Brace and brackets
        animations = [
            manim.FadeOut(bracket1[0]),
            manim.FadeOut(bracket1[1]),
            manim.FadeOut(brace_2),
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(1)

        # FADE AND SHRINK: Array into longer encoding
        # FADE IN: Encoded paragraph
        encoded_paragraph = manim.Text(
            "[18, 39, 50, 50, 1, 58, 53, 1, 58, 46, 63, 1, 54, 56, 39, 63, 43, 56, 57, 8, 8, 8, 0]",
            t2c={
                '[1:3]':'#3174f0',
                '[5:7]':'#e53125',
                '[9:11]':'#fbb003',
                '[13:15]': '#fbb003'
            }
        ).scale(.5)
        self.play(manim.ReplacementTransform(quote, encoded_paragraph))
        self.wait(7)
        self.play(manim.FadeToColor(encoded_paragraph, color=manim.WHITE))
        self.wait(3)
        self.play(manim.FadeOut(encoded_paragraph))
        self.wait(1)
        self.next_section()
        ###########################################
        #                                         #
        #       END SECTION ONE, ENCODING         #
        #                                         #
        ###########################################

        ###########################################
        #                                         #
        #       BEGIN SECTION TWO, CONTEXT        #
        #                                         #
        ###########################################

        # Fall to thy prayers. This statement is taken from the William Shakespeare
        # play Henry the Fifth, in which King Henry disavows the knight Sir John Falstaff.
        # Considered by itself, the statement to "Fall to thy prayers..." can be taken as an ominous
        # directive implying some sort of threat. We could imagine a despot
        # or tyrant telling his enemies to Fall to their prayers before he
        # slaughters them. It inspires this imagery because of the encoding
        # I apply to it based on my own experiences, preferences, and inclinations.
        # However, when taken in the context of the play Henry the Fifth,
        # we see Henry is essentially telling Falstaff to fall to his prayers
        # because he has been disowned. He should fall to his prayers because
        # we, the audience, know Falstaff to be an avid sinner. Henry is sealing
        # Falstaff's fate and thus, his desolation. We derive this encoding from
        # Shakespeare's body of work, including other plays. The body of Shakespeare's
        # plays in which either Henry the Fifth or John Falstaff appear provides
        # the context we require to understand Henry's directive.
        # We expanded our context from the statement alone, to the statement in relation
        # to Henry and Falstaff's other interactions of which we are aware.
        # This is how human language is encoded. So, how does a computer which
        # processes digital signals understand the difference between the encoding
        # I applied to the statement, and the encoding Shakespeare intended.
        # In fact, as an aside, how can we even be sure we completely understand
        # the encoding Shakespeare intended? The answer is context.
        #
        # So, how would you, dear listener, seek to understand this statement?
        # You would probably read the play, watch a stage performance, or read
        # a critical essay. In fact, you'd be best served to do all three, thus
        # expanding your context and building the encoding required to decode
        # the intent behind this sentence. The computer is no different. We must
        # find a way to allow the computer to understand this statement, but
        # critically, in context with other statements. In fact, we can leverage
        # the power of current computing to build a large contextual understanding.
        #
        # First, we have to transform the text which humans can read, into numbers
        # which the computer can use. Humans use a complex and poorly-understood
        # combination of logic, emotion, and memory to build context, and each of us
        # applies our own gradient of these mental properties. What exactly that
        # combination of properties that forms a mental state is varies from person
        # to person. The computer, however, performs sets of instructions which
        # usually involve either moving signals around between components, or doing
        # calculations. So how does an inorganic machine gain context to interpret
        # the encoding of human speech? Well, we only have one option: we have to
        # compute the relationships between the components of human speech mathematically.
        #
        # First, we begin by exposing the invisible symbols the computer uses to make
        # the text legible to us. For instance, the last two characters, a backslash and the
        # letter "n", are essentially an instruction to the computer to start a new line when
        # it encounters this combination. Now, let's isolate just one word, "Fall".
        #
        # Next, we transform the symbols that comprise human language into
        # numbers, a process also called encoding. Interestingly, this version of encoding
        # is slightly different from the encoding we described earlier, but you probably
        # knew what I meant because of the context. For numbers, we use integers, which
        # implies only zeros after the decimal place, known in math as whole numbers.
        # Next, we choose unique integers to represent our letters. The numbers we choose
        # can be arbitrary, or we can be clever and choose numbers which are attractive
        # computationally, but let's ignore that for now. In this case, we've chosen the integers
        # 18, 39, and 50. Now that we've converted our letters to numbers, we can say they
        # have a basic encoding. In order to carry these numbers through sets of computations,
        # we place them into a computer data structure called an array, which can be thought of
        # as a 1-dimensional matrix, a vector, or simply a named collection of values stored in
        # contiguous computer memory. Now, let's place our encoded letters back into the context
        # of the sentence, Fall to thy prayers. Note the last 4 values: 8, 8, 8, 0. We've also
        # included the encoded version of a period, and the newline character. We do this
        # because punctuation in human language is a form of encoding that describes how
        # we should interpret the text. A comma might separate statements syntactically or
        # signal a vocal pause if the text is meant to be read aloud.
        #
        # Now, let's view the original human-legible text, encoded into english letters.
        # There's our word, "Fall", in the context of the play. Now, let's encode these three
        # lines, including all the punctuation and hidden characters like newlines and spaces,
        # into integers. If you were to deeply consider the integer-encoded text in this way
        # you might realize that our original simple encoding won't unlock the computer's
        # ability to interpret the speech because our encoding lacks spatial awareness.
        # It lacks context. Each letter appears in other places, in other words.
        # The letter "l" appears 7 times. The computer doesn't inherently understand the
        # difference between the appearance of the letter "l" in the word "fall", to the
        # letter "l" in the name Falstaff. Each of these letters, and indeed each instance
        # of each letter must carry its own encoding.

        # "in Shakespeare words rarely carry a single meaning,
        # ~ Elizabeathen plays sought the deepest meaningful dialogue ~

        # create a code class to imitate a document
        # FADE IN: document
        doc1_text = """Falstaff: My king, my Jove! I speak to thee, my heart!

King Henry V: I know thee not, old man. Fall to thy prayers.
How ill white hairs become a fool and jester!
        """
        doc1 = manim.Code(
            code=doc1_text,
            background="window",
            language="md",
            line_no_from=46,
            style=manim.Code.styles_list[15]
        )
        self.play(manim.Write(doc1))
        self.wait(3)
        self.play(manim.Indicate(doc1[2][2][40:44], color=manim.WHITE, scale_factor=3))
        animations = [
            manim.FadeToColor(doc1[2][2][40], color='#3174f0'),
            manim.FadeToColor(doc1[2][2][41], color='#e53125'),
            manim.FadeToColor(doc1[2][2][42:44], color='#fbb003')
        ]
        self.play(manim.AnimationGroup(*animations))
        self.wait(5)

        # TRANSFORM: doc1 to encoded document
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
        # color our encoded string 18 39 50 50
        doc2[2][3][48:51].set_color(color='#3174f0')
        doc2[2][3][51:54].set_color(color='#e53125')
        doc2[2][3][54:60].set_color(color='#fbb003')
        self.play(manim.ReplacementTransform(doc1, doc2))
        self.wait(3)

        # now the encoded letters are part of a set
        # they have spatial meaning, because there
        # exists some probability distribution
        # function that describes the likelihood
        # each token occurs in a certain place
        # in the document
        # doc2[2][3][57:60].set_color(color='#269a43')
        # self.play(manim.ReplacementTransform(doc1, doc2))
        # self.wait(3)

        doc2_text_ptr = [[],[],[
            ['[18 39 50 57 58 39 44 44 10 1 25 63 1 49 47 52 45 6 1 51 63 1 22 53 60 '],
            ['43 2 1 21 1 57 54 43 39 49 1 58 53 1 58 46 43 43 6 1 51 63 1 46 43 39 '],
            ['56 58 2 1 23 47 52 45 1 20 43 52 56 63 1 34 10 1 21 1 49 52 53 61 1 58 '],
            ['46 43 43 1 52 53 58 6 1 53 50 42 1 51 39 52 8 1 18 39 50 50 1 58 53 1 '],
            ['58 46 63 1 54 56 39 63 43 56 57 8 1 20 53 61 1 47 50 50 1 61 46 47 58 '],
            ['43 1 46 39 47 56 57 1 40 43 41 53 51 43 1 39 1 44 53 53 50 1 39 52 42 '],
            ['1 48 43 57 58 43 56 2 ]']
        ]]
        # for loop through doc2_text and randomly color "50"
        # "each occurrence of the letter 'l' begins to take on its own encoding"
        # set a last_item pointer
        last_item = ''
        # iterate through the range of nested lists in doc2_text_ptr
        for j in range(len(doc2_text_ptr[2])):
            # enumerate the pointer list
            for idx,item in enumerate(doc2_text_ptr[2][j][0]):
                # if the current and last tokens are 5,0
                if last_item != " " and item == " " and item != "[" and item != "]":
                    # set the corresponding index in doc2 to a random hex color
                    colors = ['#3174f0', '#e53125', '#fbb003', '#269a43', '#9c27b0', '#607d8b', '#ffcb6b']
                    random_color = numpy.random.choice(colors, replace=False)
                    self.play(manim.Write(doc2[2][j][idx - 2:idx].set_color(color=random_color), run_time=.025))
                last_item = item
        doc2[2][6][0].set_color(color=random_color)

        self.wait(7)
        # self.play(manim.Uncreate(doc2))
        # self.wait(1)

        # scene 2 begins here
        # bring back the doc2 as white text
        # show the computer selecting context starting points
        # show the computer building a contextual vector
        # show the vectors as a growing spreadsheet
        # transform the spreadsheet to 3d
        # stack multiple spreadsheets together like files or a stack of paper
        # show how each is connected to the next

        # DRAW IN: bounding box while:
        # DRAW IN: selected array
        r1 = manim.Rectangle(width=3.35, height=0.3, color='#ff5370').shift(manim.LEFT * .85 + manim.UP * .135)
        t0 = manim.DecimalTable(
            [[52, 45, 1, 20, 43, 52, 56, 63]],
            row_labels=[manim.MathTex('block_1')],
            include_outer_lines=True
        ).next_to(doc2, manim.DOWN * 3).scale(.7)
        animations = [
            manim.Write(r1),
            manim.FadeIn(t0),
        ]
        t0.get_horizontal_lines().set_color(manim.RED)
        t0.get_vertical_lines().set_color(manim.RED)
        self.play(manim.AnimationGroup(*animations))
        self.wait(5)

        # MOVE UP: selected array while:
        # FADE UP AND OUT: doc2 encoded document
        # the selected array is the block, with block size 8
        animations = [
            manim.FadeOut(doc2, shift=manim.UP),
            manim.FadeOut(r1, shift=manim.UP),
            t0.animate.move_to(manim.ORIGIN)
        ]
        self.play(manim.AnimationGroup(*animations))
        self.play(manim.FadeToColor(t0, manim.WHITE))
        self.wait(3)
