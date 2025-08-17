from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # --------- Title ---------
        title = Text("Classifying an Unknown Bug", font_size=40)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.0)

        # --------- Logical plot bounds ---------
        x_left, x_right = -5, 5
        y_bottom, y_top = -3, 3

        # Anchors for axes
        x0 = LEFT * 5.2 + DOWN * 2.6
        x_end = RIGHT * 5.0 + DOWN * 2.6
        y_end = LEFT * 5.2 + UP * 2.6

        # Axes
        x_axis = Line(x0, x_end, stroke_width=8)
        y_axis = Line(x0, y_end, stroke_width=8)
        self.play(Create(x_axis), Create(y_axis), run_time=0.8)

        # Axis labels
        x_label = (
            Text("width", font_size=30)
            .next_to(x_axis, DOWN, buff=0.25)
            .align_to(x_axis, RIGHT)
        )
        y_label = Text("length", font_size=30).next_to(y_axis, LEFT, buff=0.25)
        y_label.rotate(PI / 2)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.5)

        # --------- Helper to map (x, y) to scene ---------
        x_dir = x_end - x0
        y_dir = y_end - x0

        def to_scene(x, y):
            tx = (x - x_left) / (x_right - x_left)
            ty = (y - y_bottom) / (y_top - y_bottom)
            return x0 + tx * x_dir + ty * y_dir

        # --------- Separating line (y = 0.5x) ---------
        start_xy = (x_left, 0.5 * x_left)
        end_xy = (x_right, 0.5 * x_right)
        sep_line = Line(
            to_scene(*start_xy),
            to_scene(*end_xy),
            color=BLUE,
            stroke_width=10,
            z_index=2,
        )

        # --------- Highlight positive and negative regions ---------
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
        self.play(Create(sep_line), run_time=0.8)

        # --------- Unknown bug (orange ring above the line) ---------
        bug_x, bug_y = 1.6, 1.35
        unknown_bug = Circle(radius=0.12, color=ORANGE, stroke_width=7).move_to(
            to_scene(bug_x, bug_y)
        )
        self.play(Create(unknown_bug), run_time=0.6)

        # --------- Label + arrow pointing to the bug ---------
        label_text = Text("unknown bug", font_size=28)
        label_text.next_to(unknown_bug, UL, buff=0.6)
        arrow = CurvedArrow(
            start_point=label_text.get_right() + RIGHT * 0.05,
            end_point=unknown_bug.get_top(),
            angle=-PI / 4,
            color=GRAY_E,
            stroke_width=6,
        )
        self.play(Write(label_text), Create(arrow))

        # --------- Positive/Negative region labels ---------
        pos_label = Text("Positive region", font_size=26, color=GREEN).move_to(
            to_scene(2, 2)
        )
        neg_label = Text("Negative region", font_size=26, color=RED).move_to(
            to_scene(-2, -2)
        )
        self.play(FadeIn(pos_label), FadeIn(neg_label), run_time=0.8)

        # --------- Caption at the bottom ---------
        caption = Text(
            "A linear function can classify new bugs:\n"
            "This unknown bug lies in the positive region, so it’s a caterpillar.",
            font_size=26,
            line_spacing=0.9,
        ).set_z_index(5)
        caption_bg = BackgroundRectangle(caption, fill_opacity=0.85, buff=0.25)
        caption_group = VGroup(caption_bg, caption).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(caption_group, shift=UP), run_time=1.0)

        self.wait(2)
