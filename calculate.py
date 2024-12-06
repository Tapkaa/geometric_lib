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
    try:
        # Формирование строки для вызова функции через eval
        if fig == 'triangle' and func == 'area':
            # Для треугольника, где функция площади вычисляется вручную, мы прописываем ее отдельно
            a, b, c = size
            p = (a + b + c) / 2 
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            return area
        elif fig == 'triangle' and func == 'perimeter':
            # Для периметра треугольника
            return sum(size)

        # Для других фигур используем eval
        result = eval(f'{fig}.{func}(*{size})')
        return result
    except Exception as e:
        raise AssertionError(f"Error during calculation: {str(e)}")


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
        # Вычисление результата
        result = calc_with_eval(fig, func, size)
        print(f"Result: {result}")
    except AssertionError as e:
        # Вывод ошибки в случае неудачи
        print(f"Error: {e}")
