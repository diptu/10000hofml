from manim import *


class main(Scene):
    def construct(self):
        # Title
        title = Text("Key idea: learn by shrinking the error", font_size=44).to_edge(
            UP, buff=0.6
        )
        self.play(Write(title), run_time=1.8)

        # Bullet lines (kept short to avoid overflow)
        bullets = VGroup(
            Text(
                "If the error is shrinking, nudge c only a little to avoid overshooting.",
                font_size=30,
            ),
            Text("Make the correction a fraction of the error.", font_size=30),
            Text("Big error → bigger change; small error → tiny nudge.", font_size=30),
            Text(
                "Neural networks learn by: try → measure error → refine.", font_size=30
            ),
            Text(
                "This is iterative—improve step by step, not in one shot.", font_size=30
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        # Fit bullets nicely on screen
        bullets.scale_to_fit_width(config.frame_width * 0.9)
        bullets.next_to(title, DOWN, buff=0.6).to_edge(LEFT, buff=0.8)

        # Animate bullets in a staggered way
        self.play(
            LaggedStart(
                *[FadeIn(line, shift=DOWN * 0.2) for line in bullets], lag_ratio=0.15
            ),
            run_time=2.6,
        )
        self.wait(2)
