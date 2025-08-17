from manim import *
import numpy as np
from typing import List, Tuple

# -------- Config --------
CENTER_SHOW_TIME = 1.2
MOVE_TIME = 1.0
POST_WAIT = 0.30

CENTER_SCALE = 1.0  # base scale when first centering a panel
DOCKED_SCALE = 0.85  # < 1 => docked panels look smaller in their slots

GRID_PAD = 0.92
SAFE_SIDE_MARGIN = 0.94
SAFE_TOP_GAP = 0.60

# Park/transition feel
PARK_SCALE = 0.92  # shrink parked panels during center preview
PARK_SHIFT = 0.25  # push parked panels outward a bit
DOCK_PATH_ARC = PI / 10  # gentle curve to avoid visual collision

# NEW: push docked grids further into corners (and keep within edges)
SLOT_PUSH = 0.2  # 0.0 = default quarter-grid; higher => closer to corners
SLOT_EDGE_PAD = 0.08  # keep a margin from the work-area edges (0..0.2 is typical)

GRID_LAYOUT = {
    "objective": "UL",
    "graph": "UR",
    "explainer": "LL",
    "calc": "LR",
}


# -------- Helpers --------
def normalize_vec(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    return v / n if n > 1e-8 else np.array([0.0, 0.0, 0.0])


def make_work_area(scene: Scene, title: Mobject) -> Rectangle:
    frame = scene.camera.frame  # requires MovingCameraScene
    usable_w = frame.width * SAFE_SIDE_MARGIN
    usable_h = frame.height - (title.height + SAFE_TOP_GAP)
    usable_h = max(usable_h, frame.height * 0.5)
    work_area = Rectangle(width=usable_w, height=usable_h, stroke_opacity=0)
    work_area.next_to(title, DOWN, buff=0.30)
    return work_area


def _slot_center_raw(work_area: Rectangle, slot: str) -> np.ndarray:
    """
    Base slot positions at the four quadrants; then pushed further toward corners
    using SLOT_PUSH, and softly clamped inside work-area via SLOT_EDGE_PAD.
    """
    # base quarter offsets
    dx, dy = work_area.width / 4, work_area.height / 4
    cx, cy, _ = work_area.get_center()

    # push further out
    dx *= 1.0 + SLOT_PUSH
    dy *= 1.0 + SLOT_PUSH

    target = {
        "UL": np.array([cx - dx, cy + dy, 0.0]),
        "UR": np.array([cx + dx, cy + dy, 0.0]),
        "LL": np.array([cx - dx, cy - dy, 0.0]),
        "LR": np.array([cx + dx, cy - dy, 0.0]),
    }[slot]

    # soft clamp inside edges
    half_w, half_h = work_area.width / 2, work_area.height / 2
    max_x = cx + half_w * (1.0 - SLOT_EDGE_PAD)
    min_x = cx - half_w * (1.0 - SLOT_EDGE_PAD)
    max_y = cy + half_h * (1.0 - SLOT_EDGE_PAD)
    min_y = cy - half_h * (1.0 - SLOT_EDGE_PAD)

    target[0] = np.clip(target[0], min_x, max_x)
    target[1] = np.clip(target[1], min_y, max_y)
    return target


def slot_center(work_area: Rectangle, slot: str) -> np.ndarray:
    return _slot_center_raw(work_area, slot)


def slot_size(work_area: Rectangle) -> Tuple[float, float]:
    # Half the work-area (2x2 grid)
    return (work_area.width / 2, work_area.height / 2)


def fit_to_slot(
    mob: Mobject, slot_w: float, slot_h: float, pad: float = GRID_PAD
) -> float:
    max_w, max_h = slot_w * pad, slot_h * pad
    if mob.width <= 1e-6 or mob.height <= 1e-6:
        return 1.0
    return min(max_w / mob.width, max_h / mob.height, 1.0)


def box_with_title(title_text: str, body=None, w=5.5, h=3.2):
    box = RoundedRectangle(
        corner_radius=0.25, width=w, height=h, fill_opacity=0.08, stroke_opacity=0.5
    )
    t = (
        Text(title_text, font_size=36, weight=BOLD)
        .move_to(box.get_top())
        .shift(DOWN * 0.45)
    )
    g = VGroup(box, t)
    if body is not None:
        body.set_width(w * 0.9)
        body.move_to(box.get_center()).shift(DOWN * 0.05)
        g.add(body)
    return g


# -------- Section builders (placeholders to replace later) --------
def build_objective():
    body = MarkupText(
        "<b>Objective</b>: Computers are just glorified calculators.\n.",
        font_size=30,
        line_spacing=1.05,
        justify=True,
    )
    return box_with_title("Objective", body)


def build_graph():
    axes = Axes(
        [0, 4, 1],
        [0, 4, 1],
        x_length=5.4,
        y_length=3.1,
        axis_config={"include_numbers": True, "font_size": 22},
        tips=False,
    )
    line = axes.plot(lambda x: 0.6 * x, x_range=[0, 4], color=BLUE, stroke_width=6)
    return box_with_title("Graph", VGroup(axes, line), w=6.6, h=4.2)


def build_explainer():
    body = MarkupText(
        "Explainer text goes here. Intuition, bullets, etc.",
        font_size=30,
        line_spacing=1.05,
        justify=True,
    )
    return box_with_title("Explainer", body)


def build_calculation():
    eq1 = MathTex(r"E = y - \hat{y}", font_size=40)
    eq2 = MathTex(r"\Delta A = \frac{E}{x}", font_size=40)
    return box_with_title("Calculation", VGroup(eq1, eq2).arrange(DOWN, buff=0.25))


# -------- Scene (MovingCameraScene) --------
class ModularFourPanelsSafe(MovingCameraScene):
    def setup(self):
        super().setup()
        self.docked: List[Mobject] = []

    def park_docked(self, work_area: Rectangle, animate=True):
        """Gently scale and push docked panels outward to avoid center overlap."""
        if not self.docked:
            return
        anims = []
        center = work_area.get_center()
        for m in self.docked:
            dir_vec = normalize_vec(m.get_center() - center)
            shift_vec = dir_vec * PARK_SHIFT
            anims.append(m.animate.scale(PARK_SCALE).shift(shift_vec))
        if animate:
            self.play(*anims, run_time=0.25)

    def restore_docked(self):
        if not self.docked:
            return
        inv_scale = 1.0 / PARK_SCALE
        anims = [m.animate.scale(inv_scale) for m in self.docked]
        self.play(*anims, run_time=0.20)

    def center_then_place(self, mob: Mobject, slot_key: str, work_area: Rectangle):
        # Center preview — scaled to fit work area (appears larger than docked)
        mob.move_to(work_area.get_center()).scale(CENTER_SCALE)
        center_fit = fit_to_slot(mob, work_area.width, work_area.height, pad=0.95)
        if center_fit < 1.0:
            mob.scale(center_fit)

        # Keep center clean
        self.park_docked(work_area, animate=True)

        # Show centered preview
        self.play(FadeIn(mob), run_time=CENTER_SHOW_TIME)
        self.wait(0.15)

        # Compute destination & final (smaller) docked scale
        dest = slot_center(work_area, GRID_LAYOUT[slot_key])
        sw, sh = slot_size(work_area)
        slot_scale = fit_to_slot(mob, sw, sh, pad=GRID_PAD)
        final_scale = slot_scale * DOCKED_SCALE

        # 1) Shrink at center (quick), then 2) move with a slight arc to the slot
        self.play(mob.animate.scale(final_scale), run_time=0.20)
        self.play(mob.animate.move_to(dest), run_time=MOVE_TIME, path_arc=DOCK_PATH_ARC)
        self.wait(POST_WAIT)

        # Restore parked panels and register this one as docked
        self.restore_docked()
        self.docked.append(mob)

    def construct(self):
        title = Text("Modular Sequence — 4 Panels (Corner-Pushed Slots)", font_size=48)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=1.0)

        work_area = make_work_area(self, title)
        # self.add(work_area.copy().set_stroke(YELLOW, 2, opacity=0.3))  # debug guide

        objective = build_objective()
        graph = build_graph()
        explainer = build_explainer()
        calc = build_calculation()

        self.center_then_place(objective, "objective", work_area)
        self.center_then_place(graph, "graph", work_area)
        self.center_then_place(explainer, "explainer", work_area)
        self.center_then_place(calc, "calc", work_area)
        self.wait(0.8)
