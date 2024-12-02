import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
@@ -10,50 +9,42 @@
    'triangle-perimeter': 3, 'triangle-area': 3
}

class InvalidShapeError(Exception):
    pass

class InvalidFunctionError(Exception):
    pass

class InvalidParametersError(Exception):
    pass

def calc(fig, func, size):
    if fig not in figs:
        raise InvalidShapeError(f"Invalid shape: {fig}")
        return "Invalid shape"
    if func not in funcs:
        raise InvalidFunctionError(f"Invalid function: {func}")

        return "Invalid function"

    if fig == 'circle' and len(size) != 1:
        return "Invalid parameters for circle"
    if fig == 'square' and len(size) != 1:
        return "Invalid parameters for square"
    if fig == 'triangle' and len(size) != 3:
        return "Invalid parameters for triangle"
    required_size = sizes.get(f'{fig}-{func}')
    if required_size is None:
        raise InvalidParametersError(f"Invalid combination of {fig} and {func}")
    
        return f"Invalid combination of {fig} and {func}"

    if len(size) != required_size:
        raise InvalidParametersError(f"Invalid parameters for {fig}. Expected {required_size} but got {len(size)}.")
        return f"Invalid parameters for {fig}"

    try:
        result = eval(f'{fig}.{func}(*{size})')
        return result
    except Exception as e:
        raise Exception(f"Error during calculation: {str(e)}")
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

    try:
        result = calc(fig, func, size)
        print(f'{func} of {fig} is {result}')
    except (InvalidShapeError, InvalidFunctionError, InvalidParametersError, Exception) as e:
        print(f"Error: {e}")
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
