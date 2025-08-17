from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("All Three Lines — After Two Training Examples", font_size=50)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=2.0)

        # ---------- LEFT: Axes ----------
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=5.8,
            y_length=4.8,
            axis_config={"include_numbers": True, "font_size": 28},
            tips=False,
        )
        x_label = Text("width (x)", font_size=28).next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("length", font_size=28).next_to(axes.y_axis, LEFT, buff=0.25)
        self.play(Create(axes), FadeIn(x_label, y_label), run_time=2.0)
        self.wait(1.0)

        # ---------- Slopes ----------
        A0, A1, A2 = 0.25, 0.3667, 2.9
        line_A0 = axes.plot(
            lambda x: A0 * x, x_range=[0, 4], color=BLUE_E, stroke_width=5
        )
        line_A1 = axes.plot(
            lambda x: A1 * x, x_range=[0, 4], color=TEAL_D, stroke_width=6
        )
        line_A2 = axes.plot(
            lambda x: A2 * x, x_range=[0, 4], color=MAROON_C, stroke_width=7
        )

        # Tags (labels for each line)
        tag_A0 = MathTex(r"A=0.25", font_size=34, color=BLUE_E)
        tag_A1 = MathTex(r"A=0.3667", font_size=34, color=TEAL_D)
        tag_A2 = MathTex(r"A=2.9", font_size=34, color=MAROON_C)

        tag_A0.move_to(axes.coords_to_point(1.4, A0 * 1.4)).shift(
            UP * 0.32 + RIGHT * 0.18
        )
        tag_A1.move_to(axes.coords_to_point(1.7, A1 * 1.7)).shift(
            UP * 0.32 + RIGHT * 0.18
        )
        tag_A2.move_to(axes.coords_to_point(1.2, A2 * 1.2)).shift(
            UP * 0.32 + RIGHT * 0.18
        )

        # Animate each line + label together
        self.play(Create(line_A0), FadeIn(tag_A0), run_time=2.0)
        self.wait(1.0)
        self.play(Create(line_A1), FadeIn(tag_A1), run_time=2.0)
        self.wait(1.0)
        self.play(Create(line_A2), FadeIn(tag_A2), run_time=2.0)
        self.wait(1.0)

        # ---------- Training example points ----------
        # Example 1
        x1, true1, target1 = 3.0, 1.0, 1.1
        yhat1_A0 = A0 * x1
        dot_true1 = Dot(axes.coords_to_point(x1, true1), color=RED, radius=0.10)
        dot_target1 = Dot(axes.coords_to_point(x1, target1), color=BLUE, radius=0.10)
        dot_yhat1 = Dot(axes.coords_to_point(x1, yhat1_A0), color=YELLOW, radius=0.10)

        # Example 2
        x2, true2, target2 = 1.0, 3.0, 2.9
        yhat2_A1 = A1 * x2
        p_yhat2 = axes.coords_to_point(x2, yhat2_A1)
        p_target2 = axes.coords_to_point(x2, target2)
        dot_true2 = Dot(axes.coords_to_point(x2, true2), color=RED, radius=0.10)
        dot_target2 = Dot(p_target2, color=BLUE, radius=0.10)
        dot_yhat2 = Dot(p_yhat2, color=YELLOW, radius=0.10)

        self.play(
            FadeIn(dot_yhat1), FadeIn(dot_true1), FadeIn(dot_target1), run_time=1.5
        )
        self.wait(1.0)
        self.play(
            FadeIn(dot_yhat2), FadeIn(dot_true2), FadeIn(dot_target2), run_time=1.5
        )
        self.wait(1.0)

        # Error arrow for example 2
        err_arrow_2 = Arrow(
            p_yhat2,
            p_target2,
            color=GREEN,
            buff=0.02,
            max_tip_length_to_length_ratio=0.20,
            stroke_width=6,
        )
        err_text_2 = MathTex(
            r"E = y - \hat{y} = 2.9 - 0.3667 = 2.5333", font_size=38, color=GREEN
        )
        err_text_2.next_to(0.5 * (p_yhat2 + p_target2), RIGHT, buff=0.25)

        self.play(GrowArrow(err_arrow_2), run_time=2.0)
        self.play(FadeIn(err_text_2), run_time=2.0)
        self.wait(1.0)

        # ---------- RIGHT Panel ----------
        panel_box = RoundedRectangle(
            corner_radius=0.25,
            height=6.6,
            width=9.2,
            fill_opacity=0.15,
            fill_color=BLACK,
            stroke_opacity=0.65,
        )
        panel_title = Text(
            "Training Example 2 — Update Summary", font_size=40, weight=BOLD
        )
        panel_title.move_to(panel_box.get_top()).shift(DOWN * 0.50)

        body = MarkupText(
            "New example: <b>(x, y) = (1.0, 3.0)</b>.\n"
            "With slope <b>A = 0.3667</b>, prediction is "
            "<span foreground='yellow'><b>ŷ = 0.3667</b></span>.\n"
            "Target <b>y = 2.9</b>.\n"
            "Error: <span foreground='green'><b>E = 2.5333</b></span>.\n"
            "Update: <b>ΔA = 2.5333</b>, so "
            "<span foreground='red'><b>A<sub>new</sub> = 2.9</b></span>.",
            font_size=36,
            line_spacing=1.15,
            justify=True,
            font="Arial Bold",
        )
        body.set_width(panel_box.width * 0.92)

        eqs = VGroup(
            MathTex(
                r"A_0 = 0.25 \;\rightarrow\; A_1 = 0.3667 \;\rightarrow\; A_2 = 2.9",
                font_size=42,
                color=GRAY,
            ),
            MathTex(r"\hat{y} = A x", font_size=44, color=BLUE),
            MathTex(r"E = y - \hat{y}", font_size=44, color=GREEN),
            MathTex(r"\Delta A = \tfrac{E}{x}", font_size=46, color=YELLOW),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        panel_content = VGroup(body, eqs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        panel_group = VGroup(panel_box, panel_title, panel_content)
        panel_content.move_to(panel_box.get_center()).shift(DOWN * 0.08)

        # Position side-by-side
        left_group = VGroup(
            axes,
            x_label,
            y_label,
            line_A0,
            line_A1,
            line_A2,
            tag_A0,
            tag_A1,
            tag_A2,
            dot_yhat1,
            dot_true1,
            dot_target1,
            dot_yhat2,
            dot_true2,
            dot_target2,
            err_arrow_2,
            err_text_2,
        )
        content = VGroup(left_group, panel_group).arrange(
            RIGHT, buff=1.3, aligned_edge=UP
        )

        # Scale to fit frame
        max_w = self.camera.frame_width * 0.94
        max_h = (self.camera.frame_height - title.height - 0.60) * 0.92
        content.scale_to_fit_width(max_w)
        if content.height > max_h:
            content.scale_to_fit_height(max_h)
        content.next_to(title, DOWN, buff=0.36)

        # Animate panel
        self.play(FadeIn(panel_box), FadeIn(panel_title), run_time=2.0)
        self.play(Write(body), run_time=3.0)
        for eq in eqs:
            self.play(Write(eq), run_time=2.0)
            self.wait(0.8)
        self.wait(2.0)
