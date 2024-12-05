import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3
}


def calc(fig, func, size):
    # Проверка на допустимые фигуры и функции
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}")

    # Получаем ключ и ожидаемое количество параметров
    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    if expected_args is None:
        raise ValueError(f"Invalid size configuration for {fig} and {func}")
    if len(size) != expected_args:
        raise ValueError(f"Expected {expected_args} parameters for {fig} {func}, but got {len(size)}")

    if any(s <= 0 for s in size):
        raise ValueError("All sizes must be positive numbers")

    if fig == "triangle":
        a, b, c = size
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The provided sides do not form a valid triangle")
        if func == 'area':
            p = (a + b + c) / 2 
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5 
            return area
        elif func == 'perimeter':
            return a + b + c

    if fig == 'circle':
        if func == 'area':
            return circle.area(*size)
        elif func == 'perimeter':
            return circle.perimeter(*size)

    if fig == 'square':
        if func == 'area':
            return square.area(*size)
        elif func == 'perimeter':
            return square.perimeter(*size)

    raise ValueError(f"Unexpected error for {fig} {func}")


def calc_with_eval(fig, func, size):
    try:
        result = eval(f'{fig}.{func}(*{size})')
        return result
    except Exception as e:
        raise ValueError(f"Error during calculation: {str(e)}")


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    # Ввод фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Ввод функции
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Ввод размеров
    while len(size) != sizes.get(f"{fig}-{func}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and square, 3 for triangle:\n"
        ).split()))

    try:
        result = calc_with_eval(fig, func, size)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
