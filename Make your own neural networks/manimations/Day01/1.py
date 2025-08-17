from manim import *


class main(Scene):
    def construct(self):
        # Intro narration
        intro_text = Text(
            "Computers are just glorified calculators,\n"
            "so let’s use more appropriate words to describe what’s going on:",
            font_size=32,
            line_spacing=1.2,
        ).to_edge(UP)
        self.play(Write(intro_text), run_time=3)
        self.wait(1)

        # Process circle
        process_circle = Circle(color=PURPLE, radius=1.2, stroke_width=5).move_to(
            ORIGIN
        )
        process_label = Text("calculate", font_size=32).move_to(
            process_circle.get_center() + UP * 0.3
        )

        self.play(Create(process_circle), run_time=1.2)
        self.play(Write(process_label), run_time=0.8)

        # Input label
        input_label = (
            Text("input", font_size=36).to_edge(LEFT, buff=1.5).shift(UP * 0.3)
        )
        self.play(FadeIn(input_label, shift=LEFT * 0.3), run_time=0.6)

        # Arrow from input -> process
        arrow_style = {
            "stroke_width": 8,
            "max_tip_length_to_length_ratio": 0.2,
            "color": BLUE,
        }
        arrow1 = Arrow(
            input_label.get_right() + DOWN * 0.1,
            process_circle.get_left() + DOWN * 0.1,
            **arrow_style,
        )
        self.play(Create(arrow1), run_time=0.6)

        # Output label
        output_label = (
            Text("output", font_size=36).to_edge(RIGHT, buff=1.5).shift(UP * 0.3)
        )
        self.play(FadeIn(output_label, shift=RIGHT * 0.3), run_time=0.6)

        # Arrow from process -> output
        arrow2 = Arrow(
            process_circle.get_right() + DOWN * 0.1,
            output_label.get_left() + DOWN * 0.1,
            **arrow_style,
        )
        self.play(Create(arrow2), run_time=0.6)

        self.wait(1)

        # Outro narration
        outro_text = Text(
            "It takes some inputs, processes them, and gives us an output.",
            font_size=32,
        ).to_edge(DOWN)
        self.play(Write(outro_text), run_time=2)
        self.wait(1)

        # Example values (in green)
        example_input = Text("Exaple : 3 × 4", font_size=32, color=GREEN).next_to(
            input_label, DOWN
        )
        example_process = Text("4 + 4 + 4", font_size=32, color=GREEN).next_to(
            process_label, DOWN
        )
        example_output = Text("12", font_size=32, color=GREEN).next_to(
            output_label, DOWN
        )

        # Animate example appearing
        self.play(Write(example_input))
        self.play(Write(example_process))
        self.play(Write(example_output))

        self.wait(1.5)
