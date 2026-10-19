"""Classify finite real side lengths; invalid input returns 'Invalid'."""

import math
from numbers import Real


def is_valid_triangle(a, b, c) -> bool:
    """Require positive finite numbers and a strict triangle inequality."""
    sides = (a, b, c)
    if any(isinstance(s, bool) or not isinstance(s, Real) for s in sides):
        return False
    try:
        if any(not math.isfinite(s) or s <= 0 for s in sides):
            return False
    except (OverflowError, TypeError, ValueError):
        return False
    x, y, z = sorted(sides)
    # Equivalent to x + y > z, without overflowing the sum.
    return x > z - y


def classify_triangle(a, b, c) -> str:
    """Return Invalid or a shape label, optionally prefixed with 'Right '."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    x, y, z = sorted((a, b, c))
    if x == z:
        return "Equilateral"
    shape = "Isosceles" if x == y or y == z else "Scalene"
    # Normalize before squaring to avoid overflow/underflow at extreme scales.
    # Relative tolerance is 1e-9; no absolute tolerance is needed at this scale.
    if math.isclose((x / z) ** 2 + (y / z) ** 2, 1.0,
                    rel_tol=1e-9, abs_tol=0.0):
        return "Right " + shape
    return shape
