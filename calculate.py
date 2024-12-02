class InvalidShapeError(Exception):
    pass

class InvalidFunctionError(Exception):
    pass

class InvalidParametersError(Exception):
    pass

class CalculationError(Exception):
    pass


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle-perimeter': 1, 'circle-area': 1,
    'square-perimeter': 1, 'square-area': 1,
    'triangle-perimeter': 3, 'triangle-area': 3
}


def calc(fig, func, size):
    if fig not in figs:
        raise InvalidShapeError(f"Invalid shape: {fig}")
    
    if func not in funcs:
        raise InvalidFunctionError(f"Invalid function: {func}")
    
    if fig == 'circle' and len(size) != 1:
        raise InvalidParametersError(f"Invalid parameters for circle: expected 1 parameter, got {len(size)}")
    
    if fig == 'square' and len(size) != 1:
        raise InvalidParametersError(f"Invalid parameters for square: expected 1 parameter, got {len(size)}")
    
    if fig == 'triangle' and len(size) != 3:
        raise InvalidParametersError(f"Invalid parameters for triangle: expected 3 parameters, got {len(size)}")
    
    try:
        result = eval(f'{fig}.{func}(*{size})')
        return result
    except Exception as e:
        raise CalculationError(f"Error during calculation: {str(e)}")


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

    try:
        result = calc(fig, func, size)
        print(f'{func} of {fig} is {result}')
    except (InvalidShapeError, InvalidFunctionError, InvalidParametersError, CalculationError) as e:
        print(f"Error: {e}")
