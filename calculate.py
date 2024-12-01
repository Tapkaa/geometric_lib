import circle
import square
import triangle

# Используем множества для быстрой проверки
figs = {'circle', 'square', 'triangle'}
funcs = {'perimeter', 'area'}
sizes = {
    'circle-perimeter': 1,
    'circle-area': 1,
    'square-perimeter': 1,
    'square-area': 1,
    'triangle-perimeter': 3,
    'triangle-area': 3
}
def calc(fig, func, size):
    if fig not in figs:
        return 'Invalid shape'
    if func not in funcs:
        return 'Invalid function'
    if fig == 'circle' and len(size) != 1:
        return 'Invalid parameters for circle'
    if fig == 'square' and len(size) != 1:
        return 'Invalid parameters for square'
    if fig == 'triangle' and len(size) != 3:
        return 'Invalid parameters for triangle'
    try:
        if fig == 'circle':
            if func == 'area':
                return circle.area(*size)
            elif func == 'perimeter':
                return circle.perimeter(*size)
        elif fig == 'square':
            if func == 'area':
                return square.area(*size)
            elif func == 'perimeter':
                return square.perimeter(*size)
        elif fig == 'triangle':
            if func == 'area':
                return triangle.area(*size)
            elif func == 'perimeter':
                return triangle.perimeter(*size)
    except Exception as e:
        return f'Error during calculation: {str(e)}'
if __name__ == '__main__':
    func = ''
    fig = ''
    size = list()
    while fig not in figs:
        fig = input(f'Enter figure name, available are {figs}:\n')
    while func not in funcs:
        func = input(f'Enter function name, available are {funcs}:\n')
    while len(size) != sizes.get(f'{func}-{fig}', 1):
        try:
            size = list(map(int, input('Input figure sizes separated by space, 1 for circle and square\n').split(' ')))
        except ValueError:
            print('Invalid input. Please enter integer values for the sizes.')
            continue
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
