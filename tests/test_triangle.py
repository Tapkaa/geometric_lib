import pytest
from triangle import area, perimeter

def test_triangle_area():
    # Arrange
    a, b, c = 3, 4, 5

    # Act
    result = area(a, b, c)

    # Assert
    s = (a + b + c) / 2
    expected_result = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    assert result == pytest.approx(expected_result, rel=1e-9)

def test_triangle_perimeter():
    # Arrange
    a, b, c = 3, 4, 5

    # Act
    result = perimeter(a, b, c)

    # Assert
    expected_result = a + b + c
    assert result == expected_result
