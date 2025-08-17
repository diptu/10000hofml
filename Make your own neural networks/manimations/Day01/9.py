from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("Widths and Lengths of Garden Bugs", font_size=42)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.6)

        # ---------- Axes (hand-drawn vibe) ----------
        # We'll draw simple axes without ticks for a sketchy look
        x_axis = Line(LEFT * 5.2 + DOWN * 2.7, RIGHT * 5.2 + DOWN * 2.7, stroke_width=8)
        y_axis = Line(LEFT * 5.2 + DOWN * 2.7, LEFT * 5.2 + UP * 2.7, stroke_width=8)
        self.play(Create(x_axis), Create(y_axis), run_time=1.0)

        x_label = (
            Text("width", font_size=30)
            .next_to(x_axis, DOWN, buff=0.2)
            .align_to(x_axis, RIGHT)
        )
        y_label = (
            Text("length", font_size=30).next_to(y_axis, LEFT, buff=0.2).rotate(PI / 2)
        )
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.6)

        # ---------- Clusters ----------
        # Coordinates roughly placed to match the sketch:
        # Caterpillars: thin & long -> small width (left), larger length (upper)
        cat_points = np.array(
            [
                [-2.7, 1.4, 0],
                [-2.2, 1.7, 0],
                [-2.4, 1.2, 0],
                [-1.9, 1.5, 0],
                [-2.5, 1.9, 0],
                [-2.1, 2.1, 0],
                [-2.8, 1.8, 0],
            ]
        )
        # Ladybirds: wide & short -> larger width (right), smaller length (lower)
        lady_points = np.array(
            [
                [2.7, -0.4, 0],
                [2.3, -0.2, 0],
                [3.0, -0.1, 0],
                [2.6, -0.6, 0],
                [3.1, -0.5, 0],
                [2.4, -0.8, 0],
            ]
        )

        def ring_dots(points, color):
            dots = VGroup()
            for p in points:
                c = Circle(radius=0.12, color=color, stroke_width=7)
                c.move_to(p)
                dots.add(c)
            return dots

        caterpillars = ring_dots(cat_points, RED)
        ladybirds = ring_dots(lady_points, GREEN)

        self.play(
            LaggedStart(*[Create(c) for c in caterpillars], lag_ratio=0.08),
            run_time=1.2,
        )
        self.play(
            LaggedStart(*[Create(c) for c in ladybirds], lag_ratio=0.08), run_time=1.0
        )

        # ---------- Annotations ----------
        arrow_style = dict(
            stroke_width=8, max_tip_length_to_length_ratio=0.18, color=BLUE
        )

        cat_center = np.mean(cat_points, axis=0)
        lady_center = np.mean(lady_points, axis=0)

        cat_label = Text("caterpillars", font_size=28, slant=ITALIC)
        cat_label.next_to(y_axis, RIGHT, buff=0.4).shift(UP * 0.2)
        cat_arrow = Arrow(
            cat_label.get_bottom() + RIGHT * 0.2, cat_center + DOWN * 0.2, **arrow_style
        )

        lady_label = Text("ladybirds", font_size=28, slant=ITALIC)
        lady_label.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.2)
        lady_arrow = Arrow(
            lady_label.get_left() + UP * 0.1, lady_center + UP * 0.2, **arrow_style
        )

        self.play(Write(cat_label), Create(cat_arrow), run_time=0.8)
        self.play(Write(lady_label), Create(lady_arrow), run_time=0.8)

        # ---------- Caption ----------
        caption = Paragraph(
            "You can clearly see two groups. The caterpillars are thin and long, "
            "and the ladybirds are wide and short.",
            alignment="LEFT",
            font_size=26,
            line_spacing=0.9,
        ).scale_to_fit_width(config.frame_width - 1.0)
        caption.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(caption), run_time=1.0)
        self.wait(2)
