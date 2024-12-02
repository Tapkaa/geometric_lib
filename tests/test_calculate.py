import pytest
from calculate import calc, InvalidShapeError, InvalidFunctionError

# Тесты для корректных данных

def test_square_perimeter():
    # Arrange
    fig = 'square'
    func = 'perimeter'
    size = [4]  # Сторона квадрата

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 16  # Периметр квадрата с стороной 4 = 4 * 4

def test_square_area():
    # Arrange
    fig = 'square'
    func = 'area'
    size = [4]  # Сторона квадрата

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 16  # Площадь квадрата с стороной 4 = 4^2

def test_circle_perimeter():
    # Arrange
    fig = 'circle'
    func = 'perimeter'
    size = [5]  # Радиус круга

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 31.41592653589793  # Периметр круга с радиусом 5 = 2 * 3.14159 * 5

def test_circle_area():
    # Arrange
    fig = 'circle'
    func = 'area'
    size = [5]  # Радиус круга

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 78.53981633974483  # Площадь круга с радиусом 5 = 3.14159 * 5^2

def test_triangle_perimeter():
    # Arrange
    fig = 'triangle'
    func = 'perimeter'
    size = [3, 4, 5]  # Стороны треугольника

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 12  # Периметр треугольника с длинами сторон 3, 4, 5

def test_triangle_area():
    # Arrange
    fig = 'triangle'
    func = 'area'
    size = [3, 4, 5]  # Стороны треугольника

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 6  # Площадь треугольника с длинами сторон 3, 4, 5 по формуле Герона

# Тесты для некорректных данных

def test_invalid_shape():
    # Arrange
    fig = 'pentagon'  # Некорректная фигура
    func = 'perimeter'
    size = [5]

    # Act & Assert
    with pytest.raises(InvalidShapeError) as exc_info:  # Сохраняем информацию о выброшенном исключении
        calc(fig, func, size)
    
    # Проверяем, что исключение содержит нужное сообщение
    assert str(exc_info.value) == "Invalid shape: pentagon"

def test_invalid_function():
    # Arrange
    fig = 'square'
    func = 'volume'  # Некорректная функция
    size = [4]

    # Act & Assert
    with pytest.raises(InvalidFunctionError) as exc_info:  # Сохраняем информацию о выброшенном исключении
        calc(fig, func, size)
    
    # Проверяем, что исключение содержит нужное сообщение
    assert str(exc_info.value) == "Invalid function: volume"

def test_invalid_size_for_square():
    # Arrange
    fig = 'square'
    func = 'area'
    size = [4, 5]  # Слишком много параметров для квадрата

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == "Invalid parameters for square"  # Ожидаем сообщение об ошибке

def test_invalid_size_for_circle():
    # Arrange
    fig = 'circle'
    func = 'area'
    size = []  # Отсутствует параметр для круга

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == "Invalid parameters for circle"  # Ожидаем сообщение об ошибке

def test_invalid_size_for_triangle():
    # Arrange
    fig = 'triangle'
    func = 'area'
    size = [3, 4]  # Треугольник требует 3 стороны

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == "Invalid parameters for triangle"  # Ожидаем сообщение об ошибке
