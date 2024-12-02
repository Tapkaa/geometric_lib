import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle-perimeter': 1, 'circle-area': 1,
    'square-perimeter': 1, 'square-area': 1,
    'triangle-perimeter': 3, 'triangle-area': 3
}


def calc(fig, func, size):
    if fig not in figs:
        return "Invalid shape"
    if func not in funcs:
        return "Invalid function"

    key = f'{fig}-{func}'

    if key in sizes and len(size) != sizes[key]:
        return f"Invalid parameters for {fig}"

    required_size = sizes.get(f'{fig}-{func}')
    if required_size is None:
        return f"Invalid combination of {fig} and {func}"

    if len(size) != required_size:
        return f"Invalid parameters for {fig}"

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
    while len(size) != sizes.get(f"{fig}-{func}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
