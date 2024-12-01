import pytest
from square import area, perimeter

def test_square_area():
    # Arrange
    a = 4

    # Act
    result = area(a)

    # Assert
    expected_result = a * a
    assert result == expected_result

def test_square_perimeter():
    # Arrange
    a = 4

    # Act
    result = perimeter(a)

    # Assert
    expected_result = 4 * a
    assert result == expected_result
