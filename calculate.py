import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
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
        return "Invalid shape"
    if func not in funcs:
        return "Invalid function"
    if fig == 'circle' and len(size) != 1:
        return "Invalid parameters for circle"
    if fig == 'square' and len(size) != 1:
        return "Invalid parameters for square"
    if fig == 'triangle' and len(size) != 3:
        return "Invalid parameters for triangle"
    try:
        result = eval(f'{fig}.{func}(*{size})')
        return result
    except Exception as e:
        return str(e)
if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
