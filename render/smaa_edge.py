import math

def threshold(base, contrast):
    """自适应阈值。"""
    raise NotImplementedError("TODO: threshold")

def edge_rgb(r, g, b):
    """三通道检测。"""
    raise NotImplementedError("TODO: edge_rgb")

def diagonal(dx, dy):
    """对角图案。"""
    raise NotImplementedError("TODO: diagonal")

def temporal(enabled):
    """不做时域累积。"""
    raise NotImplementedError("TODO: temporal")

def order(after_taa):
    """放在 TAA 之后。"""
    raise NotImplementedError("TODO: order")

def step_for(width, base):
    """按分辨率缩放步长。"""
    raise NotImplementedError("TODO: step_for")

def after_tonemap(order):
    """tonemap 后检测。"""
    raise NotImplementedError("TODO: after_tonemap")

def normalize2(a, b):
    """权重归一。"""
    raise NotImplementedError("TODO: normalize2")

def to_linear(value):
    """线性空间。"""
    raise NotImplementedError("TODO: to_linear")

def alpha_edge(alpha):
    """透明单独处理。"""
    raise NotImplementedError("TODO: alpha_edge")

def span(step):
    """搜索范围。"""
    raise NotImplementedError("TODO: span")

def is_vertical(dx):
    """垂直边判定。"""
    raise NotImplementedError("TODO: is_vertical")

def weight(area):
    """混合权重。"""
    raise NotImplementedError("TODO: weight")

def key(pixel_id):
    """边缘键。"""
    raise NotImplementedError("TODO: key")

def clamp01(value):
    """归一钳制。"""
    raise NotImplementedError("TODO: clamp01")
