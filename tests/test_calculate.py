import pytest
from calculate import calc
from math import pi


def test_circle_area():
    fig = 'circle'
    func = 'area'
    size = [1]
    res = calc(fig, func, size)
    assert res == pi

def test_square_area():
    fig = 'square'
    func = 'area'
    size = [1]
    res = calc(fig, func, size)
    assert res == 1

def test_triangle_area():
    fig = 'triangle'
    func = 'area'
    size = [5, 12, 13]
    res = calc(fig, func, size)
    assert res == 30

def test_circle_perimeter():
    fig = 'circle'
    func = 'perimeter'
    size = [1]
    res = calc(fig, func, size)
    assert res == 2 * pi

def test_square_perimeter():
    fig = 'square'
    func = 'perimeter'
    size = [1]
    res = calc(fig, func, size)
    assert res == 4

def test_triangle_perimeter():
    fig = 'triangle'
    func = 'perimeter'
    size = [5, 12, 13]
    res = calc(fig, func, size)
    assert res == 30

def test_wrong_fig():
    fig = 'rectangle'
    func = 'area'
    size = [1]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_wrong_func():
    fig = 'circle'
    func = 'diagonal'
    size = [1]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_wrong_size():
    fig = 'square'
    func = 'area'
    size = [1, 2]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_neg_size_area_circle():
    fig = 'circle'
    func = 'area'
    size = [-1]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_neg_size_area_square():
    fig = 'square'
    func = 'area'
    size = [-1]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_neg_size_area_triangle():
    fig = 'triangle'
    func = 'area'
    size = [-5, -12, -13]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_neg_size_perimeter_circle():
    fig = 'circle'
    func = 'perimeter'
    size = [-1]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_neg_size_perimeter_square():
    fig = 'square'
    func = 'perimeter'
    size = [-1]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_neg_size_perimeter_triangle():
    fig = 'triangle'
    func = 'perimeter'
    size = [-5, -12, -13]
    with pytest.raises(AssertionError):
        calc(fig, func, size)

def test_wrong_size_triangle():
    fig = 'triangle'
    func = 'area'
    size = [1, 2, 10]
    with pytest.raises(AssertionError):
        calc(fig, func, size)
