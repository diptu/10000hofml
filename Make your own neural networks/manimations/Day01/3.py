from manim import *


class main(Scene):
    def construct(self):
        # Title / intro text
        title_text = Text(
            "We know kilometres and miles have a linear relationship:\n"
            "miles = kilometres × c\n\n"
            "We don’t know c yet, but we have some real-world examples:",
            font_size=32,
            line_spacing=1.3,
        ).to_edge(UP)
        self.play(Write(title_text), run_time=3)

        # Table data
        table_data = [["Kilometres", "Miles"], ["0", "0"], ["100", "62.137"]]
        table = Table(
            table_data, include_outer_lines=True, h_buff=1.0, v_buff=0.4
        ).scale(0.8)
        table.next_to(title_text, DOWN, buff=0.8)

        self.play(Create(table), run_time=2)
        self.wait(1)

        # Guess section
        guess_title = Text(
            "Let’s guess c = 0.5 and see what happens for 100 km:", font_size=32
        ).next_to(table, DOWN, buff=1)
        guess_calc = Text(
            "miles = 100 × 0.5 = 50 miles", font_size=32, color=GREEN
        ).next_to(guess_title, DOWN)

        self.play(Write(guess_title), run_time=2)
        self.play(Write(guess_calc), run_time=2)
        self.wait(2)
