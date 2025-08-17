from manim import *
import itertools as it


class myNN(Scene):
    def construct(self):
        # Create neural network
        net = NeuralNetworkMobject([4, 3, 3, 1])

        # Label neurons
        net.label_inputs(
            [f"x1{i + 1}" for i in range(len(net.layers[0].neurons))], color=BLACK
        )
        net.label_hidden_layer(
            1, [f"a1{i + 1}" for i in range(len(net.layers[1].neurons))], color=BLACK
        )
        net.label_hidden_layer(
            2, [f"a2{i + 1}" for i in range(len(net.layers[2].neurons))], color=BLACK
        )
        net.label_outputs(
            [f"o{i + 1}" for i in range(len(net.layers[-1].neurons))], color=BLACK
        )

        # Set neuron colors
        net.color_layer(0, YELLOW)  # Input
        net.color_layer(1, BLUE)  # Hidden 1
        net.color_layer(2, BLUE)  # Hidden 2
        net.color_layer(3, ORANGE)  # Output

        # Scale for spacing
        net.scale(0.8)

        # Semi-transparent filled highlights
        input_box = SurroundingRectangle(
            net.layers[0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.15, buff=0.25
        )
        hidden_box1 = SurroundingRectangle(
            net.layers[1], color=BLUE, fill_color=BLUE, fill_opacity=0.15, buff=0.25
        )
        hidden_box2 = SurroundingRectangle(
            net.layers[2], color=BLUE, fill_color=BLUE, fill_opacity=0.15, buff=0.25
        )
        output_box = SurroundingRectangle(
            net.layers[3], color=ORANGE, fill_color=ORANGE, fill_opacity=0.15, buff=0.25
        )

        # Layer labels moved higher and scaled smaller
        input_label = (
            Text("Input Layer", color=YELLOW)
            .scale(0.45)
            .next_to(input_box, UP, buff=0.5)
        )
        hidden_label1 = (
            Text("Hidden Layer 1", color=BLUE)
            .scale(0.45)
            .next_to(hidden_box1, UP, buff=0.5)
        )
        hidden_label2 = (
            Text("Hidden Layer 2", color=BLUE)
            .scale(0.45)
            .next_to(hidden_box2, UP, buff=0.5)
            .shift(RIGHT)
        )
        output_label = (
            Text("Output Layer", color=ORANGE)
            .scale(0.45)
            .next_to(output_box, UP, buff=0.5)
        )

        # Animate everything
        self.play(Write(net))
        self.play(FadeIn(input_box), FadeIn(input_label))
        self.play(FadeIn(hidden_box1), FadeIn(hidden_label1))
        self.play(FadeIn(hidden_box2), FadeIn(hidden_label2))
        self.play(FadeIn(output_box), FadeIn(output_label))
        self.wait()


class NeuralNetworkMobject(VGroup):
    CONFIG = {
        "neuron_radius": 0.15,
        "neuron_to_neuron_buff": MED_SMALL_BUFF,
        "layer_to_layer_buff": 1.5 * LARGE_BUFF,
        "neuron_stroke_width": 2,
        "edge_color": LIGHT_GREY,
        "edge_stroke_width": 2,
        "max_shown_neurons": 16,
        "brace_for_large_layers": True,
        "neuron_fill_opacity": 1,
    }

    def __init__(self, neural_network, *args, **kwargs):
        VGroup.__init__(self, *args, **kwargs)
        self.layer_sizes = neural_network
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)

    def add_neurons(self):
        layers = VGroup(*[self.get_layer(size) for size in self.layer_sizes])
        layers.arrange_submobjects(RIGHT, buff=self.CONFIG["layer_to_layer_buff"])
        self.layers = layers

    def get_layer(self, size):
        n_neurons = min(size, self.CONFIG["max_shown_neurons"])
        neurons = VGroup(
            *[
                Circle(
                    radius=self.CONFIG["neuron_radius"],
                    stroke_color=WHITE,
                    stroke_width=self.CONFIG["neuron_stroke_width"],
                    fill_color=BLACK,
                    fill_opacity=self.CONFIG["neuron_fill_opacity"],
                )
                for _ in range(n_neurons)
            ]
        )
        neurons.arrange_submobjects(DOWN, buff=self.CONFIG["neuron_to_neuron_buff"])
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()

        layer = VGroup(neurons)
        layer.neurons = neurons
        return layer

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = Line(
                    n1.get_center(),
                    n2.get_center(),
                    stroke_color=self.CONFIG["edge_color"],
                    stroke_width=self.CONFIG["edge_stroke_width"],
                )
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def label_inputs(self, labels, color=WHITE):
        self.input_labels = VGroup()
        for neuron, label in zip(self.layers[0].neurons, labels):
            tex = Tex(label, color=color).scale(0.5)
            tex.move_to(neuron)
            self.input_labels.add(tex)
        self.add(self.input_labels)

    def label_outputs(self, labels, color=WHITE):
        self.output_labels = VGroup()
        for neuron, label in zip(self.layers[-1].neurons, labels):
            tex = Tex(label, color=color).scale(0.5)
            tex.move_to(neuron)
            self.output_labels.add(tex)
        self.add(self.output_labels)

    def label_hidden_layer(self, layer_index, labels, color=WHITE):
        hidden_labels = VGroup()
        for neuron, label in zip(self.layers[layer_index].neurons, labels):
            tex = Tex(label, color=color).scale(0.5)
            tex.move_to(neuron)
            hidden_labels.add(tex)
        self.add(hidden_labels)

    def color_layer(self, layer_index, fill_color):
        for neuron in self.layers[layer_index].neurons:
            neuron.set_fill(fill_color, opacity=1)
