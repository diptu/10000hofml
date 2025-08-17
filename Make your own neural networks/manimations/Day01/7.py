from manim import *


# Helper to keep formula snug inside the circle
def fit_group_inside(group: VGroup, circle: Circle, padding=0.22):
    max_w = circle.width * (1 - padding)
    max_h = circle.height * (1 - padding)
    scale_factor = min(max_w / group.width, max_h / group.height)
    if scale_factor < 1:
        group.scale(scale_factor)
    group.move_to(circle.get_center())
    return group


class main(Scene):
    """Page 2: nudge to c = 0.61 (smaller error)."""

    def construct(self):
        # Top paragraph
        para_top = (
            Paragraph(
                "0.6 was much better than 0.7, but let’s refine a bit more. "
                "Nudge c down slightly from 0.6 to 0.61 and try again.",
                alignment="LEFT",
                font_size=26,
                line_spacing=0.9,
            )
            .scale_to_fit_width(config.frame_width - 1.0)
            .to_edge(UP, buff=0.35)
        )
        self.play(Write(para_top), run_time=2.5)

        # Diagram (centered)
        circle = Circle(color=PURPLE, radius=1.3, stroke_width=6).move_to(
            ORIGIN + UP * 0.1
        )
        formula = VGroup(
            Text("miles =", font_size=34, color=BLUE),
            Text("kilometres ×", font_size=34, color=BLUE),
            Text("0.61", font_size=34, color=RED),
        ).arrange(RIGHT, buff=0.15)
        fit_group_inside(formula, circle)

        km_label = (
            Text("kilometres", font_size=28, slant=ITALIC)
            .to_edge(LEFT, buff=1.1)
            .shift(UP * 0.7)
        )
        km_val = Text("100", font_size=30, color=GREEN).next_to(
            km_label, DOWN, buff=0.1
        )

        calc_label = (
            Text("calculated miles", font_size=26, slant=ITALIC)
            .to_edge(RIGHT, buff=1.1)
            .shift(UP * 0.9)
        )
        calc_val = Text("61", font_size=30, color=RED).next_to(
            calc_label, DOWN, buff=0.1
        )

        correct_label = (
            Text("correct miles", font_size=26, slant=ITALIC)
            .to_edge(RIGHT, buff=1.1)
            .shift(DOWN * 0.3)
        )
        correct_val = Text("62.137", font_size=30, color=GREEN).next_to(
            correct_label, DOWN, buff=0.1
        )

        error_label = Text("error", font_size=24, slant=ITALIC).shift(
            DOWN * 1.7 + RIGHT * 1.2
        )
        error_val = Text("1.137", font_size=28, color=ORANGE).next_to(
            error_label, DOWN, buff=0.1
        )

        arrow_style = {
            "stroke_width": 8,
            "max_tip_length_to_length_ratio": 0.18,
            "color": BLUE,
        }
        a_l = Arrow(km_label.get_right(), circle.get_left(), **arrow_style)
        a_r = Arrow(circle.get_right(), calc_label.get_left(), **arrow_style)
        a_err = Arrow(
            error_label.get_top(), correct_label.get_bottom() + LEFT * 1.0, color=ORANGE
        )

        # Animate
        self.play(Create(circle))
        self.play(Write(formula))
        self.play(FadeIn(km_label), FadeIn(km_val))
        self.play(Create(a_l))
        self.play(FadeIn(calc_label), FadeIn(calc_val))
        self.play(Create(a_r))
        self.play(FadeIn(correct_label), FadeIn(correct_val))
        self.play(FadeIn(error_label), FadeIn(error_val), Create(a_err))

        # Closing paragraph at bottom (fits within frame)
        closing = (
            Paragraph(
                "Much better. Output is 61, only 1.137 from 62.137.\n"
                "Lesson: moderate the nudge size — if error shrinks, we’re moving closer to truth.",
                alignment="LEFT",
                font_size=24,
                line_spacing=0.95,
            )
            .scale_to_fit_width(config.frame_width - 1.0)
            .to_edge(DOWN, buff=0.35)
        )
        self.play(Write(closing), run_time=2.5)
        self.wait(1.5)
