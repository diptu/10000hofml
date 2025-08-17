from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # ---------- Top explanation ----------
        top_para = Paragraph(
            "Remember, linear functions give straight lines when you plot their output "
            "against input. The adjustable parameter c changed the slope of that line. "
            "What happens if we place a straight line over that plot?",
            alignment="LEFT",
            font_size=48,
            line_spacing=1.1,
        ).scale_to_fit_width(config.frame_width * 0.95)
        top_para.to_edge(UP, buff=0.3)
        self.play(Write(top_para), run_time=2.5)

        # ---------- Title ----------
        title = Text("Widths and Lengths of Garden Bugs", font_size=40)
        title.next_to(top_para, DOWN, buff=0.4)
        self.play(Write(title), run_time=1.0)

        # ---------- Axes ----------
        x_axis = Line(LEFT * 5.2 + DOWN * 2.5, RIGHT * 5.2 + DOWN * 2.5, stroke_width=8)
        y_axis = Line(LEFT * 5.2 + DOWN * 2.5, LEFT * 5.2 + UP * 2.5, stroke_width=8)
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

        # ---------- Points ----------
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
            vg = VGroup()
            for p in points:
                c = Circle(radius=0.14, color=color, stroke_width=7).move_to(p)
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

        # ---------- Separating line (passing through caterpillars) ----------
        # pick one caterpillar point, e.g., (-2.2, 1.7, 0)
        anchor_point = np.array([-2.2, 1.7, 0])
        slope = 1.5  # adjust slope steepness
        line_length = 10

        # parametric line: y = m(x - x0) + y0
        x_vals = np.array([-5, 5])
        y_vals = slope * (x_vals - anchor_point[0]) + anchor_point[1]

        sep_line = Line(
            start=np.array([x_vals[0], y_vals[0], 0]),
            end=np.array([x_vals[1], y_vals[1], 0]),
            stroke_width=14,
            color=BLUE,
        )
        self.play(Create(sep_line), run_time=0.8)

        line_label = Text("separating line", font_size=30, slant=ITALIC)
        line_label.next_to(sep_line, LEFT, buff=0.3).shift(DOWN * 0.4)
        line_arrow = Arrow(
            line_label.get_right() + UP * 0.05,
            anchor_point,
            stroke_width=7,
            color=BLUE,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(Write(line_label), Create(line_arrow), run_time=0.7)

        lady_label = (
            Text("ladybirds", font_size=30, slant=ITALIC)
            .to_edge(RIGHT, buff=0.9)
            .shift(DOWN * 0.3)
        )
        cat_label = (
            Text("caterpillars", font_size=30, slant=ITALIC)
            .next_to(y_axis, RIGHT, buff=0.4)
            .shift(UP * 0.2)
        )
        self.play(FadeIn(cat_label), FadeIn(lady_label), run_time=0.5)

        # ---------- Bottom explanation ----------
        bottom_para = (
            Paragraph(
                "We can’t use the line here to convert numbers like before, but we can try to use it "
                "to separate different kinds of things. If the line divided caterpillars from ladybirds, "
                "we could classify an unknown bug from its measurements. This line doesn’t succeed yet—"
                "about half the caterpillars are on the same side as the ladybirds. "
                "Let’s try a different line by adjusting the slope and see what happens.",
                alignment="LEFT",
                font_size=48,
                line_spacing=1.1,
            )
            .scale_to_fit_width(config.frame_width * 0.95)
            .to_edge(DOWN, buff=0.3)
        )

        self.play(Write(bottom_para), run_time=3.0)
        self.wait(2)
