from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # --------- Title ---------
        title = Text("Widths and Lengths of Garden Bugs", font_size=40)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.0)

        # --------- Axes ---------
        x_left, x_right = -5, 5
        y_bottom, y_top = -3, 3

        x0 = LEFT * 5.2 + DOWN * 2.6
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

        # --------- Helpers ---------
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
            return VGroup(
                *[
                    Circle(radius=0.12, color=color, stroke_width=7).move_to(
                        to_scene(x, y)
                    )
                    for x, y in points
                ]
            )

        caterpillars = ring_dots(cat_points, RED)
        ladybirds = ring_dots(lady_points, GREEN)

        self.play(LaggedStart(*[Create(c) for c in caterpillars], lag_ratio=0.08))
        self.play(LaggedStart(*[Create(c) for c in ladybirds], lag_ratio=0.08))

        # --------- Separating line (y = 0.5x) ---------
        start_xy = (-5, -2.5)
        end_xy = (5, 2.5)

        sep_line = Line(
            to_scene(*start_xy),
            to_scene(*end_xy),
            color=BLUE,
            stroke_width=10,
            z_index=2,
        )
        self.play(Create(sep_line), run_time=0.8)

        # --------- Shaded regions ---------
        # Split along line (use top half as green, bottom half red)
        green_poly = Polygon(
            to_scene(x_left, y_top),
            to_scene(x_right, y_top),
            to_scene(x_right, 0.5 * x_right),
            to_scene(x_left, 0.5 * x_left),
            fill_color=GREEN,
            fill_opacity=0.2,
            stroke_width=0,
            z_index=0,
        )

        red_poly = Polygon(
            to_scene(x_left, y_bottom),
            to_scene(x_right, y_bottom),
            to_scene(x_right, 0.5 * x_right),
            to_scene(x_left, 0.5 * x_left),
            fill_color=RED,
            fill_opacity=0.2,
            stroke_width=0,
            z_index=0,
        )

        self.play(FadeIn(green_poly), FadeIn(red_poly), run_time=1.0)

        # --------- Label for line ---------
        line_label = Text("separating line", font_size=28, slant=ITALIC)
        label_pos = sep_line.point_from_proportion(0.6) + UP * 0.6
        line_label.move_to(label_pos)

        arrow = Arrow(
            start=line_label.get_bottom() + DOWN * 0.05,
            end=sep_line.point_from_proportion(0.55),
            stroke_width=7,
            color=BLUE,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(Write(line_label), GrowArrow(arrow))

        # --------- Labels for positive/negative side ---------
        pos_label = Text("Positive side", font_size=28, color=GREEN).move_to(
            to_scene(2, 2)  # above the line
        )
        neg_label = Text("Negative side", font_size=28, color=RED).move_to(
            to_scene(-2, -2)  # below the line
        )
        self.play(FadeIn(pos_label), FadeIn(neg_label), run_time=0.8)

        # --------- Bottom paragraph (conclusion) ---------
        conclusion = Text(
            "According to this line we can clearly identify that\n"
            "caterpillars fall on the positive side of the line,\n"
            "and ladybirds fall on the negative side of the line.\n",
            font_size=28,
        ).set_z_index(5)

        # Optional: add background for readability
        conclusion_bg = BackgroundRectangle(conclusion, fill_opacity=0.85, buff=0.25)
        conclusion_group = VGroup(conclusion_bg, conclusion).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(conclusion_group, shift=UP), run_time=1.2)

        self.wait(3)
