# combined.py
from __future__ import annotations
from pathlib import Path
import importlib.util
from manim import *


def load_module(path: Path):
    """Import a module from its file path."""
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


class Combined(Scene):
    def clear_screen(self, wait_seconds: float = 0.5):
        """Fade out everything on screen."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in list(self.mobjects)])
        if wait_seconds > 0:
            self.wait(wait_seconds)

    def run_scene_from_file(self, path: Path):
        """Load file (e.g., 1.py) and run its `main` Scene."""
        mod = load_module(path)
        SceneClass = getattr(mod, "main", None)
        if SceneClass is None or not issubclass(SceneClass, Scene):
            raise ValueError(f"{path} must define a Scene subclass named `main`")
        SceneClass.construct(self)  # run inside THIS combined scene

    def construct(self):
        root = Path(__file__).resolve().parent

        # Find numeric Python files like 1.py, 2.py...
        scene_files = sorted(
            [f for f in root.glob("*.py") if f.stem.isdigit()],
            key=lambda p: int(p.stem),
        )

        total = len(scene_files)
        for i, path in enumerate(scene_files, start=1):
            print(f"[run] {i}/{total}: {path.name}")
            self.run_scene_from_file(path)
            if i < total:
                self.clear_screen(0.5)
