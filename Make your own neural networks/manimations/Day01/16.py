from manim import *


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("From a Guess to an Algorithm", font_size=44)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title))

        # ---------- Left: Axes & training data ----------
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 22},
            tips=False,
        )
        x_label = Text("Width (x)", font_size=22).next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("Length (y)", font_size=22).next_to(axes.y_axis, LEFT, buff=0.25)

        lady_pt = axes.coords_to_point(3.0, 1.0)
        cat_pt = axes.coords_to_point(1.0, 3.0)
        lady_dot = Dot(lady_pt, color=RED, radius=0.1)
        cat_dot = Dot(cat_pt, color=BLUE, radius=0.1)

        lady_lbl = (
            VGroup(
                Text("Ladybird", font_size=22, color=RED),
                MathTex("(3.0, 1.0)", font_size=22),
            )
            .arrange(DOWN, 0.08)
            .next_to(lady_dot, RIGHT, 0.2)
        )
        cat_lbl = (
            VGroup(
                Text("Caterpillar", font_size=22, color=BLUE),
                MathTex("(1.0, 3.0)", font_size=22),
            )
            .arrange(DOWN, 0.08)
            .next_to(cat_dot, LEFT, 0.2)
        )

        plot_group = VGroup(
            axes, x_label, y_label, lady_dot, cat_dot, lady_lbl, cat_lbl
        )

        # ---------- Right: Narration box ----------
        narr_box = RoundedRectangle(
            corner_radius=0.25,
            height=4.2,
            width=7.2,
            fill_opacity=0.08,
            stroke_opacity=0.3,
        )

        def narr(msg: str):
            t = MarkupText(msg, font_size=32, line_spacing=1.05, justify=True)
            t.set_width(narr_box.width * 0.94)
            t.move_to(narr_box.get_center())
            return t

        narr_text = narr(
            "Let’s start with a <b>random dividing line</b> to get moving.\n"
            "First, set up our plot with the training points."
        )
        right_group = VGroup(narr_box, narr_text)

        # ---------- Layout ----------
        content = VGroup(plot_group, right_group).arrange(RIGHT, buff=0.8)
        max_w = self.camera.frame_width * 0.92
        max_h = (self.camera.frame_height - title.height - 0.6) * 0.9
        content.scale_to_fit_width(max_w)
        if content.height > max_h:
            content.scale_to_fit_height(max_h)
        content.next_to(title, DOWN, buff=0.3)

        # ---------- Step 1 ----------
        self.play(Create(axes), FadeIn(x_label, y_label), run_time=1.2)
        self.play(FadeIn(narr_box), Write(narr_text, run_time=2.2))
        self.play(
            FadeIn(lady_dot, cat_dot, scale=0.9),
            Write(lady_lbl),
            Write(cat_lbl),
            run_time=1.4,
        )
        self.wait(2)

        # ---------- Step 2: Introduce general line ----------
        step2 = narr("We’ll describe the line with a simple equation:")
        self.play(Transform(narr_text, step2, run_time=1.8))
        y_eq_Ax = (
            MathTex("y = A x + B", font_size=40)
            .next_to(axes, UP, buff=0.2)
            .align_to(axes, LEFT)
        )
        self.play(Write(y_eq_Ax))
        self.wait(2)

        # ---------- Step 3: Simplify by dropping B ----------
        step3 = narr(
            "In full generality, a line is written as <b>(y = Ax + B)</b>.\n"
            "But for now, we’ll <b>ignore the intercept B</b> and keep it simple."
        )
        self.play(Transform(narr_text, step3, run_time=2.4))
        y_eq_simple = MathTex("y = A x", font_size=40).move_to(y_eq_Ax.get_center())
        self.play(Transform(y_eq_Ax, y_eq_simple))  # update the same text
        self.wait(3)

        # ---------- Step 4: A controls slope ----------
        step4 = narr("The slope is controlled by <b>A</b>. Let’s try <b>A = 0.25</b>.")
        self.play(Transform(narr_text, step4, run_time=1.8))
        self.wait(2)

        # ---------- Step 5: Draw y = 0.25x ----------
        m = 0.25
        trial_line = axes.plot(
            lambda x: m * x, x_range=[0, 4], color=YELLOW, stroke_width=6
        )
        mid_x = 2.0
        mid_point = axes.coords_to_point(mid_x, m * mid_x)
        line_label = MathTex("y = 0.25x", font_size=30, color=YELLOW).next_to(
            mid_point, UP + RIGHT, buff=0.15
        )

        step5 = narr("Now we draw the trial line: <b>y = 0.25x</b>.")
        self.play(Transform(narr_text, step5, run_time=1.6))
        self.play(
            AnimationGroup(
                Create(trial_line), FadeIn(line_label), lag_ratio=0.1, run_time=1.6
            )
        )
        self.wait(2)

        # ---------- Step 6 ----------
        step6 = narr(
            "Notice the problem: <b>both points are above the line</b>.\n"
            "So it doesn’t separate ladybirds from caterpillars."
        )
        self.play(Transform(narr_text, step6, run_time=2.2))
        not_good = Text("Not a good classifier", font_size=30, color=YELLOW).next_to(
            trial_line, DOWN, buff=0.2
        )
        self.play(FadeIn(not_good))
        self.wait(3)

        # ---------- Step 7 ----------
        step7 = narr(
            "Rather than eyeballing a better slope, we need a <b>repeatable recipe</b> "
            "to adjust the line — an <b>algorithm</b>."
        )
        self.play(Transform(narr_text, step7, run_time=2.4))
        self.wait(3)

        # ---------- Finish ----------
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
