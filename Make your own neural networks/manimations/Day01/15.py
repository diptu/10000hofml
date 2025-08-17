from manim import *


class main(Scene):
    def construct(self):
        # ---------- Title ----------
        title = Text("Bug Detectives: Learn by Doing", font_size=44)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title))

        # ---------- Left: Axes & points ----------
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 22},
            tips=False,
        )
        x_label = Text("Width", font_size=22).next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("Length", font_size=22).next_to(axes.y_axis, LEFT, buff=0.25)

        lady_pt = axes.coords_to_point(3.0, 1.0)
        cat_pt = axes.coords_to_point(1.0, 3.0)
        lady_dot = Dot(lady_pt, color=RED, radius=0.09)
        cat_dot = Dot(cat_pt, color=BLUE, radius=0.09)

        lady_lbl = (
            VGroup(
                Text("Ladybird", font_size=22, color=RED),
                MathTex("(3.0, 1.0)", font_size=22),
            )
            .arrange(DOWN, buff=0.08)
            .next_to(lady_dot, RIGHT, buff=0.2)
        )

        cat_lbl = (
            VGroup(
                Text("Caterpillar", font_size=22, color=BLUE),
                MathTex("(1.0, 3.0)", font_size=22),
            )
            .arrange(DOWN, buff=0.08)
            .next_to(cat_dot, LEFT, buff=0.2)
        )

        plot_group = VGroup(
            axes, x_label, y_label, lady_dot, cat_dot, lady_lbl, cat_lbl
        )

        # ---------- Right: Narration box ----------
        narr_box = RoundedRectangle(
            corner_radius=0.25,
            height=4.0,
            width=7.0,  # Bigger box
            fill_opacity=0.08,
            stroke_opacity=0.3,
        )

        def make_text(msg: str):
            t = MarkupText(msg, font_size=64, line_spacing=1.1, justify=True)
            t.set_width(narr_box.width * 0.9)  # Fit nicely inside
            t.move_to(narr_box.get_center())
            return t

        narr_text = make_text(
            "Imagine we’re bug detectives with a simple tool — a straight line on a "
            "chart of <b>width</b> and <b>length</b>. Our mission is to tilt that line just right "
            "so it separates <b>ladybirds</b> from <b>caterpillars</b>."
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

        # ---------- Animate ----------
        self.play(Create(axes), FadeIn(x_label, y_label))
        self.play(FadeIn(narr_box), Write(narr_text, run_time=4))
        self.wait(3)

        # Step 2
        step2 = make_text(
            "Instead of starting with heavy math, we <b>learn by doing</b>."
        )
        self.play(Transform(narr_text, step2, run_time=3))
        self.wait(3)

        # Training examples
        self.play(FadeIn(lady_dot, cat_dot, scale=0.9))
        step3 = make_text("We gather a couple of trusted examples:")
        self.play(Transform(narr_text, step3, run_time=3))
        self.play(Write(lady_lbl), Write(cat_lbl))
        self.wait(3)

        # Step 4
        step4 = make_text(
            "One bug is short and wide <b>(3.0, 1.0)</b> — a <b>ladybird</b>.\n"
            "Another is long and thin <b>(1.0, 3.0)</b> — a <b>caterpillar</b>."
        )
        self.play(Transform(narr_text, step4, run_time=4))
        self.wait(3)

        # Step 5
        step5 = make_text(
            "These examples are our <b>truths</b> — the data we use to teach the classifier.\n"
            "In machine learning, we call them <b>training data</b>."
        )
        self.play(Transform(narr_text, step5, run_time=4))
        self.wait(3)

        # Step 6
        step6 = make_text(
            "When we plot them, the story becomes clear: one bug in one corner, "
            "the other in the opposite."
        )
        self.play(Transform(narr_text, step6, run_time=4))
        self.wait(4)

        outro = (
            Text(
                "The picture tells the story before the line is even drawn.",
                font_size=26,
            )
            .next_to(axes, DOWN, buff=0.25)
            .align_to(axes, LEFT)
        )
        self.play(FadeIn(outro, run_time=3))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])
