from manim import *


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("Plugging In x = 3.0", font_size=44)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title))

        # ---------- LEFT COLUMN: Plot ----------
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

        lady_pt = axes.coords_to_point(3.0, 1.0)
        lady_dot = Dot(lady_pt, color=RED, radius=0.095)
        lady_lbl = (
            VGroup(
                Text("Ladybird", font_size=22, color=RED),
                MathTex("(3.0, 1.0)", font_size=22),
            )
            .arrange(DOWN, buff=0.08)
            .next_to(lady_dot, RIGHT, buff=0.22)
        )
        left_col = VGroup(axes, x_label, y_label, lady_dot, lady_lbl)

        # ---------- Right Column ----------
        eq_box = RoundedRectangle(
            corner_radius=0.25,
            height=2.6,
            width=7.2,
            fill_opacity=0.06,
            stroke_opacity=0.3,
        )
        eq_title = (
            Text("Compute with A = 0.25, x = 3.0", font_size=30)
            .move_to(eq_box.get_top())
            .shift(DOWN * 0.45)
        )
        eq_yAx = MathTex("y = A x", font_size=40)
        eq_vals = MathTex("A = 0.25 \\quad , \\quad x = 3.0", font_size=36)
        eq_calc = MathTex("y = 0.25 \\times 3.0 = 0.75", font_size=40)

        eq_stack = VGroup(eq_yAx, eq_vals, eq_calc).arrange(DOWN, buff=0.20)
        eq_stack.next_to(eq_title, DOWN, buff=0.35)
        eq_panel = VGroup(eq_box, eq_title, eq_stack)
        eq_stack.move_to(eq_box.get_center()).shift(DOWN * 0.15)

        narr_box = RoundedRectangle(
            corner_radius=0.25,
            height=2.6,
            width=7.2,
            fill_opacity=0.06,
            stroke_opacity=0.3,
        )

        def narr(msg: str):
            t = MarkupText(msg, font_size=30, line_spacing=1.05, justify=True)
            t.set_width(narr_box.width * 0.94)
            t.move_to(narr_box.get_center())
            return t

        narr1 = narr(
            "Use the trial line <b>y = A x</b> with <b>A = 0.25</b> and plug in <b>x = 3.0</b>."
        )
        right_col = VGroup(eq_panel, narr_box, narr1).arrange(
            DOWN, buff=0.40, center=False, aligned_edge=LEFT
        )
        narr1.move_to(narr_box.get_center())

        # ---------- Layout ----------
        content = VGroup(left_col, right_col).arrange(
            RIGHT, buff=0.8, center=False, aligned_edge=UP
        )
        content.scale_to_fit_width(self.camera.frame_width * 0.92)
        content.next_to(title, DOWN, buff=0.30)

        # ---------- Animate ----------
        self.play(Create(axes), FadeIn(x_label, y_label))
        self.play(FadeIn(lady_dot), Write(lady_lbl))
        self.play(FadeIn(eq_box), FadeIn(eq_title))
        self.play(Write(eq_yAx), Write(eq_vals), Write(eq_calc))
        self.play(FadeIn(narr_box), Write(narr1))

        # Trial line A = 0.25
        trial_line = axes.plot(
            lambda x: 0.25 * x, x_range=[0, 4], color=YELLOW, stroke_width=6
        )
        self.play(Create(trial_line))

        # Predicted point (3, 0.75)
        pred_pt = axes.coords_to_point(3.0, 0.75)
        pred_dot = Dot(pred_pt, color=YELLOW, radius=0.095)
        pred_lbl = MathTex("(3.0, 0.75)", font_size=30, color=YELLOW).next_to(
            pred_dot, LEFT, buff=0.22
        )
        self.play(FadeIn(pred_dot), FadeIn(pred_lbl))

        # Error arrow
        err_arrow = Arrow(pred_pt, lady_pt, color=GREEN, buff=0.02, stroke_width=5)
        err_text = MathTex(
            "error = 1.0 - 0.75 = 0.25", font_size=32, color=GREEN
        ).next_to(err_arrow, RIGHT)
        self.play(GrowArrow(err_arrow), FadeIn(err_text))

        # ---------- Narration update ----------
        narr2 = narr("The prediction (<b>0.75</b>) is below what we want.")
        self.play(Transform(narr1, narr2))
        self.wait(1.2)

        # ---------- Draw line through ladybird ----------
        narr3 = narr("If y = 1.0, the line would pass through the ladybird point.")
        self.play(Transform(narr1, narr3))

        # New line: slope A = 1/3 (passes through (3,1))
        ladybird_line = axes.plot(
            lambda x: (1 / 3) * x, x_range=[0, 4], color=BLUE, stroke_width=6
        )
        self.play(Create(ladybird_line))
        self.wait(1.5)

        # ---------- End cleanly ----------
        self.play(*[FadeOut(m) for m in self.mobjects])
