# Math formulas
## Circle
```python
import math

def area(r):
    """Функция принимает значение - радиус круга"""
    return math.pi * r * r
    """Функция возвращает площадь круга"""


def perimeter(r):
    """Функция принимает значение - радиус круга"""
    return 2 * math.pi * r
    """Функция возвращает периметр круга"""
```

## Example of function input
```python
print(area(4))
print(perimeter(4))
```

## Example of function output
```python
50.26548245743669
25.132741228718345
```


## square
```python
def area(a):
    """"Принимает число n - сторона квадрата"""
    return a * a
    """Возращает площадь квадрата"""


def perimeter(a):
    """"Принимает число n - сторона квадрата"""
    return 4 * a
    """Возращает периметр квадрата"""
```

## Example of function input
```python
print(area(4))
print(perimeter(4))
```

## Example of function output
```python
16
16
```