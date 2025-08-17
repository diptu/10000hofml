from manim import *


class main(Scene):
    def construct(self):
        # -------- Paragraph --------
        para_text = (
            Paragraph(
                "So what next? We know we’re wrong, and by how much. Instead of being a reason to despair, "
                "we use this error to guide a second, better, guess at c.\n"
                "Look at that error again. We were short by 12.137. Because the formula for converting kilometres "
                "to miles is linear, miles = kilometres × c, we know that increasing c will increase the output.\n"
                "Let’s nudge c up from 0.5 to 0.6 and see what happens.\n"
                "With c now set to 0.6, we get miles = kilometres × c = 100 × 0.6 = 60. "
                "That’s better than the previous answer of 50. We’re clearly making progress!\n"
                "Now the error is a much smaller 2.137. It might even be an error we’re happy to live with.",
                alignment="LEFT",
                font_size=26,
                line_spacing=0.8,
            )
            .scale_to_fit_width(config.frame_width - 1)
            .to_edge(UP, buff=0.3)
        )

        self.play(Write(para_text), run_time=5)
        self.wait(0.5)

        # -------- Diagram --------
        circle = Circle(color=PURPLE, radius=1.4, stroke_width=6).move_to(ORIGIN)

        # Formula
        formula_text = VGroup(
            Text("miles =", font_size=36, color=BLUE),
            Text("kilometres ×", font_size=36, color=BLUE),
            Text("0.6", font_size=36, color=RED),
        ).arrange(RIGHT, buff=0.15)

        # Fit inside circle
        padding = 0.22
        max_w = circle.width * (1 - padding)
        max_h = circle.height * (1 - padding)
        scale_factor = min(max_w / formula_text.width, max_h / formula_text.height)
        if scale_factor < 1:
            formula_text.scale(scale_factor)
        formula_text.move_to(circle.get_center())

        # Labels and values
        km_label = (
            Text("kilometres", font_size=30).to_edge(LEFT, buff=1.2).shift(UP * 0.4)
        )
        km_value = Text("100", font_size=30, color=GREEN).next_to(
            km_label, DOWN, buff=0.1
        )

        calc_label = (
            Text("calculated miles", font_size=28)
            .to_edge(RIGHT, buff=1.2)
            .shift(UP * 0.6)
        )
        calc_value = Text("60", font_size=30, color=RED).next_to(
            calc_label, DOWN, buff=0.1
        )

        correct_label = (
            Text("correct miles", font_size=28)
            .to_edge(RIGHT, buff=1.2)
            .shift(DOWN * 0.5)
        )
        correct_value = Text("62.137", font_size=30, color=GREEN).next_to(
            correct_label, DOWN, buff=0.1
        )

        error_label = Text("error", font_size=26).shift(DOWN * 2 + RIGHT * 1.5)
        error_value = Text("2.137", font_size=28, color=ORANGE).next_to(
            error_label, DOWN, buff=0.1
        )

        # Arrows
        arrow_style = {
            "stroke_width": 8,
            "max_tip_length_to_length_ratio": 0.18,
            "color": BLUE,
        }
        arr_left = Arrow(km_label.get_right(), circle.get_left(), **arrow_style)
        arr_right_calc = Arrow(circle.get_right(), calc_label.get_left(), **arrow_style)
        arr_correct = Arrow(
            correct_label.get_left(), calc_label.get_left() + DOWN * 1.0, color=GREEN
        )
        arr_error = Arrow(
            error_label.get_top(), correct_label.get_bottom() + LEFT * 1.2, color=ORANGE
        )

        # Animations
        self.play(Create(circle))
        self.play(Write(formula_text))
        self.play(FadeIn(km_label), FadeIn(km_value))
        self.play(Create(arr_left))
        self.play(FadeIn(calc_label), FadeIn(calc_value))
        self.play(Create(arr_right_calc))
        self.play(FadeIn(correct_label), FadeIn(correct_value))
        self.play(Create(arr_correct))
        self.play(FadeIn(error_label), FadeIn(error_value))
        self.play(Create(arr_error))

        self.wait(2)
