from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # --------- Title ---------
        title = Text("Widths and Lengths of Garden Bugs", font_size=40)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.0)

        # --------- "Hand-drawn" axes ---------
        x_left, x_right = -5, 5
        y_bottom, y_top = -3, 3

        x0 = LEFT * 5.2 + DOWN * 2.6  # axis origin (scene coords)
        x_end = RIGHT * 5.0 + DOWN * 2.6
        y_end = LEFT * 5.2 + UP * 2.6

        x_axis = Line(x0, x_end, stroke_width=8)
        y_axis = Line(x0, y_end, stroke_width=8)
        self.play(Create(x_axis), Create(y_axis), run_time=0.8)

        x_label = (
            Text("width", font_size=32)
            .next_to(x_axis, DOWN, buff=0.2)
            .align_to(x_axis, RIGHT)
        )
        y_label = (
            Text("length", font_size=32).next_to(y_axis, LEFT, buff=0.2).rotate(PI / 2)
        )
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.5)

        # --------- Helpers: map logical (x,y) -> scene position ---------
        x_dir = x_end - x0
        y_dir = y_end - x0

        def to_scene(x, y):
            tx = (x - x_left) / (x_right - x_left)
            ty = (y - y_bottom) / (y_top - y_bottom)
            return x0 + tx * x_dir + ty * y_dir

        # --------- Points ---------
        cat_points = np.array(
            [
                [-2.7, 1.4],
                [-2.2, 1.7],
                [-2.4, 1.2],
                [-1.9, 1.5],
                [-2.5, 1.9],
                [-2.1, 2.1],
                [-2.8, 1.8],
            ]
        )

        lady_points = np.array(
            [
                [2.7, -0.4],
                [2.3, -0.2],
                [3.0, -0.1],
                [2.6, -0.6],
                [3.1, -0.5],
                [2.4, -0.8],
            ]
        )

        def ring_dots(points, color):
            vg = VGroup()
            for x, y in points:
                c = Circle(radius=0.12, color=color, stroke_width=7).move_to(
                    to_scene(x, y)
                )
                vg.add(c)
            return vg

        caterpillars = ring_dots(cat_points, RED)
        ladybirds = ring_dots(lady_points, GREEN)

        self.play(
            LaggedStart(*[Create(c) for c in caterpillars], lag_ratio=0.08),
            run_time=1.0,
        )
        self.play(
            LaggedStart(*[Create(c) for c in ladybirds], lag_ratio=0.08), run_time=0.9
        )

        # --------- Separating line UNDER both clusters ---------
        start_xy = (-4.5, -2.6)  # far left, low y
        end_xy = (4.5, -2.4)  # far right, low y
        sep_line = Line(
            to_scene(*start_xy),
            to_scene(*end_xy),
            color=BLUE,
            stroke_width=14,
            z_index=1,
        )
        self.play(Create(sep_line), run_time=0.8)

        # Label + arrow pointing to the line
        line_label = Text("separating line", font_size=30, slant=ITALIC)
        label_pos = sep_line.point_from_proportion(0.3) + UP * 0.6
        line_label.move_to(label_pos)
        arrow = Arrow(
            start=line_label.get_bottom() + DOWN * 0.05,
            end=sep_line.point_from_proportion(0.35),
            stroke_width=7,
            color=BLUE,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(Write(line_label), GrowArrow(arrow), run_time=0.7)

        # --------- Bottom explanation ---------
        bottom_para = (
            Paragraph(
                "This time the line is even less useful! "
                "It doesn’t separate the two kinds of bugs at all.\n"
                "Let’s have another go:",
                alignment="CENTER",
                font_size=34,
                line_spacing=1.15,
            )
            .scale_to_fit_width(config.frame_width * 0.9)
            .to_edge(DOWN, buff=0.4)
        )

        self.play(Write(bottom_para), run_time=2.0)
        self.wait(2)
