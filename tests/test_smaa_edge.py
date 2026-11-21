import pytest
import math
from render import smaa_edge as mod

CASES = [
    ("threshold", 'm.threshold(0.1, 2) == approx(0.2)'),
    ("rgb", 'm.edge_rgb(0.2, 0.8, 0.5) == 0.8'),
    ("diag", 'm.diagonal(1, 1) is True'),
    ("temporal", 'm.temporal(True) is False'),
    ("order", 'm.order(True) is True'),
    ("step", 'm.step_for(1920, 480) == 4'),
    ("tonemap", 'm.after_tonemap("after") is True'),
    ("norm", 'm.normalize2(1, 3) == approx(0.25)'),
    ("linear", 'm.to_linear(0.5) == approx(0.2176, abs=1e-3)'),
    ("alpha", 'm.alpha_edge(0) is False'),
    ("span", 'm.span(2) == 5'),
    ("vertical", 'm.is_vertical(0) is True'),
    ("weight", 'm.weight(0.5) == 0.5'),
    ("key", 'm.key(1) == "e:1"'),
    ("clamp", 'm.clamp01(1.2) == 1.0')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
