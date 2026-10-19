import pytest
import math
from triangle import classify_triangle, is_valid_triangle

@pytest.mark.parametrize(
    "sides, expected",
    [
        ((3, 4, 5), True),    # valid triangle
        ((-1, 2, 2), False),  # negative side
        ((0, 2, 2), False),   # zero side
        ((1, 2, 3), False),   # degenerate boundary
        ((1, 1, 3), False),   # triangle inequality fails
    ],
)
def test_is_valid_triangle(sides, expected):
    assert is_valid_triangle(*sides) is expected


@pytest.mark.parametrize(
    "sides",
    [
        pytest.param((-1, 2, 2), id="negative-side"),
        pytest.param((0, 2, 2), id="zero-side"),
        pytest.param((1, 1, 3), id="triangle-inequality-fails"),
    ],
)
def test_invalid_triangle(sides):
    assert classify_triangle(*sides) == "Invalid"


def test_degenerate_boundary_is_invalid():
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_all_sides_equal():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_exactly_two_sides_equal():
    assert classify_triangle(3, 3, 4) == "Isosceles"


def test_all_sides_different_and_not_right():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_integer_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_non_integer_right_triangle():
    assert classify_triangle(1.5, 2.0, 2.5) == "Right Scalene"

def test_irrational_hypotenuse_right_isosceles():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"

def test_irrational_side_right_triangle():
    assert classify_triangle(1.0, 2**0.5, 3**0.5) == "Right Scalene"
