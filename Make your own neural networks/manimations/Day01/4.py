from manim import *


class main(Scene):
    def construct(self):
        # -------- Paragraph (wrapped) --------
        para_text = (
            Paragraph(
                "Okay. That’s not bad at all given we chose c = 0.5 at random! "
                "But we know it’s not exactly right because our truth example number 2 "
                "tells us the answer should be 62.137.\n"
                "We’re wrong by 12.137. That’s the error, the difference between our "
                "calculated answer and the actual truth from our list of examples. That is,\n\n"
                "error = truth - calculated\n"
                "= 62.137 - 50\n"
                "= 12.137",
                alignment="LEFT",
                font_size=28,
                line_spacing=0.8,
            )
            .scale_to_fit_width(config.frame_width - 1)
            .to_edge(UP, buff=0.4)
        )
        self.play(Write(para_text), run_time=4)
        self.wait(0.5)

        # -------- Diagram --------
        circle = Circle(color=PURPLE, radius=1.4, stroke_width=6).move_to(ORIGIN)
        self.play(Create(circle))

        # Build the formula as a group
        formula_text = VGroup(
            Text("miles =", font_size=36, color=BLUE),
            Text("kilometres ×", font_size=36, color=BLUE),
            Text("0.5", font_size=36, color=RED),
        ).arrange(RIGHT, buff=0.15)

        # --- Fit the formula inside the circle ---
        padding = 0.22  # margin inside the circle
        max_w = circle.width * (1 - padding)
        max_h = circle.height * (1 - padding)
        scale_factor = min(max_w / formula_text.width, max_h / formula_text.height)
        if scale_factor < 1:
            formula_text.scale(scale_factor)

        formula_text.move_to(circle.get_center())
        self.play(Write(formula_text), run_time=0.8)

        # Left side (kilometres)
        km_label = (
            Text("kilometres", font_size=30).to_edge(LEFT, buff=1.2).shift(UP * 0.4)
        )
        km_value = Text("100", font_size=30, color=GREEN).next_to(
            km_label, DOWN, buff=0.1
        )
        self.play(FadeIn(km_label), FadeIn(km_value))

        # Right: calculated vs correct miles
        calc_label = (
            Text("calculated miles", font_size=28)
            .to_edge(RIGHT, buff=1.2)
            .shift(UP * 0.6)
        )
        calc_value = Text("50", font_size=30, color=RED).next_to(
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

        error_label = Text("error", font_size=26).shift(DOWN * 2 + RIGHT * 1.5)
        error_value = Text("12.137", font_size=28, color=ORANGE).next_to(
            error_label, DOWN, buff=0.1
        )
        arr_error = Arrow(
            error_label.get_top(), correct_label.get_bottom() + LEFT * 1.2, color=ORANGE
        )

        # Animations
        self.play(Create(arr_left))
        self.play(FadeIn(calc_label), FadeIn(calc_value))
        self.play(Create(arr_right_calc))
        self.play(FadeIn(correct_label), FadeIn(correct_value))
        self.play(Create(arr_correct))
        self.play(FadeIn(error_label), FadeIn(error_value))
        self.play(Create(arr_error))

        self.wait(2)
