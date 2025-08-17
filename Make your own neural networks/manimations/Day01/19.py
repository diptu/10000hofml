from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("Use E to Update A", font_size=48)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=1.2)

        # ---------- LEFT: Axes & plot ----------
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=5.8,  # kept compact to leave room for panel
            y_length=4.6,
            axis_config={"include_numbers": True, "font_size": 26},
            tips=False,
        )
        x_label = Text("width (x)", font_size=26).next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("length (y)", font_size=26).next_to(axes.y_axis, LEFT, buff=0.25)
        self.play(Create(axes), FadeIn(x_label, y_label), run_time=1.2)
        self.wait(0.2)

        # Parameters
        A = 0.25
        x0 = 3.0
        y_hat = A * x0  # 0.75
        y_target = 1.1
        E = y_target - y_hat  # 0.35
        dA = E / x0  # 0.116666...
        A_new = A + dA  # ~0.366666...
        # Rounded strings for labeling
        dA_str = f"{dA:.4f}"
        A_new_str = f"{A_new:.4f}"

        # Lines: y = Ax (current) and y = (A + ΔA)x (updated)
        line_A = axes.plot(
            lambda x: A * x, x_range=[0, 4], color=BLUE_E, stroke_width=5
        )
        line_Anew = axes.plot(
            lambda x: A_new * x, x_range=[0, 4], color=TEAL_D, stroke_width=7
        )
        self.play(Create(line_A), run_time=1.0)
        self.play(Create(line_Anew), run_time=1.0)
        self.wait(0.2)

        # Small line tags (kept compact and away from busy area)
        tag_A = MathTex(r"y = A x", font_size=30, color=BLUE_E)
        tag_A.move_to(axes.coords_to_point(1.5, A * 1.5)).shift(
            UP * 0.34 + RIGHT * 0.18
        )
        tag_Anew = MathTex(r"y = (A+\Delta A)\,x", font_size=30, color=TEAL_D)
        tag_Anew.move_to(axes.coords_to_point(2.0, A_new * 2.0)).shift(
            UP * 0.34 + RIGHT * 0.18
        )
        self.play(FadeIn(tag_A), FadeIn(tag_Anew), run_time=0.8)

        # ---------- Key points at x = 3 (dots only; no text labels inside plot) ----------
        p_pred = axes.coords_to_point(x0, y_hat)  # (3, 0.75)
        p_target = axes.coords_to_point(x0, y_target)  # (3, 1.1)
        p_lady = axes.coords_to_point(x0, 1.0)  # (3, 1.0) ladybird (context)

        dot_pred = Dot(p_pred, color=YELLOW, radius=0.10)
        dot_target = Dot(p_target, color=BLUE, radius=0.10)
        dot_lady = Dot(p_lady, color=RED, radius=0.10)
        self.play(FadeIn(dot_pred), FadeIn(dot_target), FadeIn(dot_lady), run_time=0.9)
        self.wait(0.1)

        # Error arrow & text (compact)
        err_arrow = Arrow(
            p_pred,
            p_target,
            color=GREEN,
            buff=0.02,
            max_tip_length_to_length_ratio=0.20,
            stroke_width=6,
        )
        err_text = MathTex(r"E = t - y = 1.1 - 0.75 = 0.35", font_size=38, color=GREEN)
        err_text.next_to(0.5 * (p_pred + p_target), RIGHT, buff=0.25)
        self.play(GrowArrow(err_arrow), run_time=1.0)
        self.play(FadeIn(err_text), run_time=0.9)
        self.wait(0.3)

        # ---------- RIGHT: Explanation panel (derivation + numerics) ----------
        panel_box = RoundedRectangle(
            corner_radius=0.25,
            height=7,
            width=16,
            fill_opacity=0.06,
            stroke_opacity=0.48,
        )
        panel_title = Text("Derivation & Update", font_size=38)
        panel_title.move_to(panel_box.get_top()).shift(DOWN * 0.52)

        # Body (larger font + spacing)
        body = MarkupText(
            "Error with updated notation:\n"
            "<b>E = t - y</b>, where <b>y = (A + ΔA) x</b> and <b>y = A x</b>.\n"
            "So, <b>E = (A + ΔA)x - A x = (ΔA)x</b>.",
            font_size=36,
            line_spacing=1.15,
            justify=True,
        )
        body.set_width(panel_box.width)

        eq_delta = MathTex(r"\Delta A = \frac{E}{x}", font_size=46, color=YELLOW_E)
        eq_delta_note = MathTex(
            r"E = 0.35,\quad x=3.0 \;\Rightarrow\; \Delta A = \frac{0.35}{3.0} \approx 0.1167",
            font_size=40,
        )

        eq_update = MathTex(
            r"A_{\text{new}} = A + \Delta A = 0.25 + 0.1167 \approx 0.3667",
            font_size=44,
            color=TEAL_D,
        )
        eq_check = MathTex(
            r"\text{Check at } x=3.0:\; \hat{y}_{\text{new}} = A_{\text{new}}\,x \approx 0.3667\times 3 = 1.1",
            font_size=40,
            color=BLUE_E,
        )

        # Stack inside the panel
        panel_content = VGroup(
            body, eq_delta, eq_delta_note, eq_update, eq_check
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        panel_group = VGroup(panel_box, panel_title, panel_content)
        panel_content.move_to(panel_box.get_center()).shift(DOWN * 0.10)

        # ---------- MASTER LAYOUT ----------
        left_group = VGroup(
            axes,
            x_label,
            y_label,
            line_A,
            line_Anew,
            tag_A,
            tag_Anew,
            dot_pred,
            dot_target,
            dot_lady,
            err_arrow,
            err_text,
        )

        content = VGroup(left_group, panel_group).arrange(
            RIGHT, buff=1.3, aligned_edge=UP
        )

        # Fit under title safely
        max_w = self.camera.frame_width * 0.94
        max_h = (self.camera.frame_height - title.height - 0.60) * 0.92
        content.scale_to_fit_width(max_w)
        if content.height > max_h:
            content.scale_to_fit_height(max_h)
        content.next_to(title, DOWN, buff=0.36)

        # ---------- Animate panel ----------
        self.play(FadeIn(panel_box), FadeIn(panel_title), run_time=0.9)
        self.play(Write(body), run_time=1.2)
        self.play(Write(eq_delta), run_time=0.9)
        self.play(Write(eq_delta_note), run_time=0.9)
        self.play(Write(eq_update), run_time=0.9)
        self.play(Write(eq_check), run_time=1.0)
        self.wait(1.6)
