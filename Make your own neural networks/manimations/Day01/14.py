# LIM5.py
from manim import *


class main(Scene):
    def construct(self):
        # Title
        title = Text("Learning the Right Slope", font_size=40)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.0)

        # Paragraph text (story-like)
        story_text = VGroup(
            Text(
                "We’ve been drawing lines, hoping to separate our little garden bugs.",
                font_size=28,
            ),
            Text("But what if our line is wrong?", font_size=28, color=RED),
            Text(
                "What if the slope just isn’t right, and some bugs sneak to the wrong side?",
                font_size=28,
            ),
            Text("That’s the puzzle.", font_size=28, color=YELLOW),
            Text(
                "The real magic of neural networks is how they keep adjusting—",
                font_size=28,
            ),
            Text("nudging the line until it fits.", font_size=28, color=GREEN),
            Text("That’s the secret we’ll uncover next.", font_size=28, slant=ITALIC),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        story_text.to_edge(DOWN, buff=1.2)

        # Animate each line appearing
        for line in story_text:
            self.play(Write(line), run_time=1.2)
            self.wait(0.3)

        self.wait(2)
