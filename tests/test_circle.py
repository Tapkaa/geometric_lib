import math
import pytest
from calculate import calc
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
    # Arrange
    r = 5

    # Act
    result = perimeter(r)

    # Assert
    expected_result = 2 * math.pi * r
    assert result == pytest.approx(expected_result, rel=1e-9)
