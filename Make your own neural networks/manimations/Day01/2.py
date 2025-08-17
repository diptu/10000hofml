from manim import *


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text(
            "Imagine a machine that converts kilometres to miles,\n like the following:",
            font_size=40,
        ).to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=2)

        # ---------- Diagram ----------
        # Circle (process)
        circle = Circle(color=PURPLE, radius=1.6, stroke_width=7).move_to(ORIGIN)
        calc_text = Text("calculate", font_size=42).move_to(
            circle.get_center() + UP * 0.15
        )
        qmarks = Text("???", font_size=42, color=GREEN).next_to(
            calc_text, DOWN, buff=0.2
        )

        # Labels (left/right)
        km_label = Text("kilometres", font_size=44, slant=ITALIC).to_edge(
            LEFT, buff=1.2
        )
        mi_label = Text("miles", font_size=44, slant=ITALIC).to_edge(RIGHT, buff=1.2)

        # Arrows (hand-drawn-ish style)
        arrow_style = dict(
            stroke_width=10,
            max_tip_length_to_length_ratio=0.18,
            color=BLUE,
        )
        arr_left = Arrow(
            km_label.get_right() + 0.1 * DOWN,
            circle.get_left() + 0.1 * DOWN,
            **arrow_style,
        )
        arr_right = Arrow(
            circle.get_right() + 0.1 * DOWN,
            mi_label.get_left() + 0.1 * DOWN,
            **arrow_style,
        )

        # Animate diagram
        self.play(Create(circle), run_time=1.0)
        self.play(Write(calc_text), run_time=0.6)
        self.play(Write(qmarks), run_time=0.6)
        self.play(
            FadeIn(km_label, shift=LEFT * 0.3),
            FadeIn(mi_label, shift=RIGHT * 0.3),
            run_time=0.6,
        )
        self.play(Create(arr_left), Create(arr_right), run_time=0.8)

        # ---------- Paragraph (below) ----------
        para = MarkupText(
            "Now imagine we don’t know the formula for converting between kilometres "
            "and miles. All we know is the relationship between the two is "
            "<b>linear</b>. That means if we double the number in miles, the same "
            "distance in kilometres is also doubled. That makes intuitive sense. "
            "The universe would be a strange place if that wasn’t true!",
            font_size=34,
            line_spacing=0.9,
        )
        # Position paragraph comfortably below the diagram
        para.width = config.frame_width * 0.9
        para.next_to(circle, DOWN, buff=0.9).to_edge(DOWN, buff=0.6)

        # Reveal paragraph
        self.play(FadeIn(para), run_time=2)
        self.wait(4)
