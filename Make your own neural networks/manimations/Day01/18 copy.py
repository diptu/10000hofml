from manim import *


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("Why aim above the ladybird?", font_size=42)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title))

        # ---------- LEFT: Plot ----------
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=6.2,
            y_length=6.2,
            axis_config={"include_numbers": True, "font_size": 22},
            tips=False,
        )
        x_label = Text("Width (x)", font_size=22).next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("Length (y)", font_size=22).next_to(axes.y_axis, LEFT, buff=0.25)

        # Key points at x = 3.0
        lady_pt = axes.coords_to_point(3.0, 1.0)  # actual ladybird point
        pred_pt = axes.coords_to_point(3.0, 0.75)  # current prediction
        target_pt = axes.coords_to_point(3.0, 1.1)  # desired target

        # Dots & labels
        lady_dot = Dot(lady_pt, color=RED, radius=0.095)
        lady_lbl = (
            VGroup(
                Text("Ladybird", font_size=22, color=RED),
                MathTex("(3.0, 1.0)", font_size=22),
            )
            .arrange(DOWN, buff=0.08)
            .next_to(lady_dot, RIGHT, buff=0.24)
        )

        pred_dot = Dot(pred_pt, color=YELLOW, radius=0.095)
        pred_lbl = MathTex("(3.0, 0.75)", font_size=28, color=YELLOW).next_to(
            pred_dot, LEFT, buff=0.20
        )

        target_dot = Dot(target_pt, color=BLUE, radius=0.095)
        target_lbl = MathTex("(3.0, 1.1)", font_size=28, color=BLUE).next_to(
            target_dot, LEFT, buff=0.20
        )

        # Error arrow (pred -> target)
        err_arrow = Arrow(
            pred_pt,
            target_pt,
            color=GREEN,
            buff=0.02,
            max_tip_length_to_length_ratio=0.2,
            stroke_width=5,
        )
        err_arrow.z_index = 10

        # ---------- LEFT column group ----------
        left_col = VGroup(
            axes,
            x_label,
            y_label,
            lady_dot,
            lady_lbl,
            pred_dot,
            pred_lbl,
            target_dot,
            target_lbl,
        )

        # ---------- RIGHT: Panels ----------
        # Equation/Target panel
        eq_box = RoundedRectangle(
            corner_radius=0.25,
            height=3.0,
            width=7.2,
            fill_opacity=0.06,
            stroke_opacity=0.3,
        )
        eq_title = (
            Text("Desired target & error", font_size=28)
            .move_to(eq_box.get_top())
            .shift(DOWN * 0.45)
        )

        eq_target = MathTex(
            r"y_{\text{target}} = 1.1 \text{ (at } x=3.0\text{)}",
            font_size=36,
            color=BLUE,
        )
        eq_pred = MathTex(r"\hat{y} = 0.75", font_size=36, color=YELLOW)
        eq_err = MathTex(r"E = 1.1 - 0.75 = 0.35", font_size=40, color=GREEN)
        eq_stack = VGroup(eq_target, eq_pred, eq_err).arrange(DOWN, buff=0.20)
        eq_stack.next_to(eq_title, DOWN, buff=0.35)
        eq_panel = VGroup(eq_box, eq_title, eq_stack)
        eq_stack.move_to(eq_box.get_center()).shift(DOWN * 0.10)

        # Narration panel
        narr_box = RoundedRectangle(
            corner_radius=0.25,
            height=3.6,
            width=7.2,
            fill_opacity=0.06,
            stroke_opacity=0.3,
        )

        def narr(msg: str):
            t = MarkupText(msg, font_size=40, line_spacing=1.05, justify=True)
            t.set_width(narr_box.width * 0.94)
            t.move_to(narr_box.get_center())
            return t

        narr_text = narr(
            "But we actually want the line <b>above</b> it.\n"
            "Why? → The line is a <b>separator</b> between ladybirds and caterpillars,\n"
            "not just a predictor.\n\n"
            "So, we aim for <b>y = 1.1</b> at <b>x = 3.0</b> — just slightly above 1.0.\n"
            "That makes the desired target = <b>1.1</b>.\n"
            "Error is then: <b>E = 1.1 − 0.75 = 0.35</b>.\n\n"
            "Next, let’s visualize what “prediction,” “desired target,” and “error” mean on the plot."
        )

        right_col = VGroup(eq_panel, narr_box, narr_text).arrange(
            DOWN, buff=0.50, center=False, aligned_edge=LEFT
        )
        narr_text.move_to(narr_box.get_center())

        # ---------- MASTER LAYOUT ----------
        content = VGroup(left_col, right_col).arrange(
            RIGHT, buff=0.8, center=False, aligned_edge=UP
        )
        max_w = self.camera.frame_width * 0.92
        max_h = (self.camera.frame_height - title.height - 0.6) * 0.90
        content.scale_to_fit_width(max_w)
        if content.height > max_h:
            content.scale_to_fit_height(max_h)
        content.next_to(title, DOWN, buff=0.30)

        # ---------- ANIMATE ----------
        self.play(Create(axes), FadeIn(x_label, y_label))
        self.play(FadeIn(lady_dot), Write(lady_lbl))
        self.play(FadeIn(pred_dot), FadeIn(pred_lbl))
        self.play(FadeIn(target_dot), FadeIn(target_lbl))

        self.play(FadeIn(eq_box), FadeIn(eq_title))
        self.play(Write(eq_target))
        self.play(Write(eq_pred))
        self.play(Write(eq_err))

        self.play(FadeIn(narr_box), Write(narr_text))
        self.wait(5)

        # ---------- Clean finish ----------
        self.play(*[FadeOut(m) for m in self.mobjects])
