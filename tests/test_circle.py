import math
import pytest
from circle import area, perimeter

def test_circle_area():
    # Arrange
    r = 5

    # Act
    result = area(r)

    # Assert
    expected_result = math.pi * r * r
    assert result == pytest.approx(expected_result, rel=1e-9)

def test_circle_perimeter():
    fig = 'circle'
    func = 'perimeter'
    size = [5]

    result = calc(fig, func, size)

    expected_result = 31.41592653589793
    assert result == pytest.approx(expected_result, rel=1e-9)
