from manim import *
import numpy as np


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("What went wrong? — Moderate the Updates", font_size=50)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=2.0)

        # ---------- LEFT: Axes ----------
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=6.2,  # slightly larger for visual clarity
            y_length=4.8,
            axis_config={"include_numbers": True, "font_size": 28},
            tips=False,
        )
        x_label = Text("width (x)", font_size=28).next_to(axes.x_axis, DOWN, buff=0.28)
        y_label = Text("length", font_size=28).next_to(axes.y_axis, LEFT, buff=0.28)
        self.play(Create(axes), FadeIn(x_label, y_label), run_time=2.0)
        self.wait(0.6)

        # ---------- Lines (initial, refined after ex1, final after ex2) ----------
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

        # Labels placed near each line (keeping away from busy areas)
        tag_A0 = VGroup(
            Text("initial", font_size=28, color=GRAY_D),
            MathTex(r"y = (0.25)\,x", font_size=30, color=BLUE_E),
        ).arrange(DOWN, buff=0.04)
        tag_A0.move_to(axes.coords_to_point(1.5, A0 * 1.5)).shift(
            UP * 0.36 + RIGHT * 0.20
        )

        tag_A1 = VGroup(
            Text("refined", font_size=28, color=GRAY_D),
            MathTex(r"y = (0.3667)\,x", font_size=30, color=TEAL_D),
        ).arrange(DOWN, buff=0.04)
        tag_A1.move_to(axes.coords_to_point(1.9, A1 * 1.9)).shift(
            UP * 0.36 + RIGHT * 0.20
        )

        tag_A2 = VGroup(
            Text("final refinement", font_size=28, color=GRAY_D),
            MathTex(r"y = (2.90)\,x", font_size=30, color=MAROON_C),
        ).arrange(DOWN, buff=0.04)
        # place closer to the line before it shoots out of the frame
        tag_A2.move_to(axes.coords_to_point(1.15, A2 * 1.15)).shift(
            UP * 0.36 + RIGHT * 0.20
        )

        # Draw each line and label together (slow)
        self.play(Create(line_A0), FadeIn(tag_A0), run_time=2.0)
        self.wait(0.6)
        self.play(Create(line_A1), FadeIn(tag_A1), run_time=2.0)
        self.wait(0.6)
        self.play(Create(line_A2), FadeIn(tag_A2), run_time=2.0)
        self.wait(0.8)

        # ---------- Highlight the two training examples with circles ----------
        # Example 1: ladybird at (3, 1.0)   (green circle from earlier context)
        p_ex1 = axes.coords_to_point(3.0, 1.0)
        c_ex1 = Circle(radius=0.18, color=GREEN, stroke_width=6).move_to(p_ex1)
        self.play(Create(c_ex1), run_time=1.2)

        # Example 2: caterpillar at (1.0, 3.0) (red circle to match screenshot)
        p_ex2 = axes.coords_to_point(1.0, 3.0)
        c_ex2 = Circle(radius=0.20, color=RED, stroke_width=6).move_to(p_ex2)
        self.play(Create(c_ex2), run_time=1.2)
        self.wait(0.8)

        # ---------- RIGHT: Explanation panel (high contrast, more visible) ----------
        panel_box = RoundedRectangle(
            corner_radius=0.28,
            height=6.8,
            width=9.4,
            fill_color=BLACK,
            fill_opacity=0.18,  # subtle dark background for contrast
            stroke_color=WHITE,
            stroke_opacity=0.65,
        )
        panel_title = Text(
            "Uh-oh: we just matched the last example", font_size=40, weight=BOLD
        )

        # Body text (bigger + line spacing)
        body = MarkupText(
            "The second update pushed the line to fit the <b>last</b> point.\n"
            "That doesn’t neatly divide ladybirds and caterpillars.\n\n"
            "<b>Fix:</b> <i>moderate</i> the updates. Instead of taking the full change ΔA,\n"
            "use only a <b>fraction</b> of it — a learning-rate <b>η</b> with <b>0 &lt; η &lt; 1</b>.",
            font_size=36,
            line_spacing=1.18,
            justify=True,
        )

        eq1 = MathTex(r"\Delta A = \frac{E}{x}", font_size=46, color=YELLOW_E)
        eq2 = MathTex(
            r"A_{\text{new}} = A + \eta\,\Delta A\quad\text{with}\quad 0<\eta<1",
            font_size=46,
            color=TEAL_D,
        )

        panel_title.move_to(panel_box.get_top()).shift(DOWN * 0.52)
        content_stack = VGroup(body, eq1, eq2).arrange(
            DOWN, buff=0.36, aligned_edge=LEFT
        )
        content_stack.set_width(panel_box.width * 0.90)
        content_stack.move_to(panel_box.get_center()).shift(DOWN * 0.06)

        right_panel = VGroup(panel_box, panel_title, content_stack)

        # ---------- MASTER LAYOUT ----------
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
            c_ex1,
            c_ex2,
        )
        layout = VGroup(left_group, right_panel).arrange(
            RIGHT, buff=1.3, aligned_edge=UP
        )

        # Fit under title
        max_w = self.camera.frame_width * 0.94
        max_h = (self.camera.frame_height - title.height - 0.60) * 0.92
        layout.scale_to_fit_width(max_w)
        if layout.height > max_h:
            layout.scale_to_fit_height(max_h)
        layout.next_to(title, DOWN, buff=0.38)

        # Reveal panel slowly
        self.play(FadeIn(panel_box), FadeIn(panel_title), run_time=2.0)
        self.play(Write(body), run_time=2.6)
        self.play(Write(eq1), run_time=2.0)
        self.play(Write(eq2), run_time=2.0)
        self.wait(2.0)

        # Optional emphasis: fade older lines to gray, keep final bold
        fade_old = AnimationGroup(
            line_A0.animate.set_opacity(0.35),
            tag_A0.animate.set_opacity(0.35),
            line_A1.animate.set_opacity(0.35),
            tag_A1.animate.set_opacity(0.35),
            lag_ratio=0.1,
        )
        self.play(fade_old, run_time=1.6)
        self.wait(1.4)
