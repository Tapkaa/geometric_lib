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

def circle_perimeter(r):
    return 2 * 3.14159 * r

def circle_area(r):
    return 3.14159 * r ** 2

def square_perimeter(s):
    return 4 * s

def square_area(s):
    return s ** 2

def triangle_perimeter(a, b, c):
    return a + b + c

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

functions = {
    'circle': {
        'perimeter': circle_perimeter,
        'area': circle_area
    },
    'square': {
        'perimeter': square_perimeter,
        'area': square_area
    },
    'triangle': {
        'perimeter': triangle_perimeter,
        'area': triangle_area
    }
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
        result = eval(f'functions["{fig}"]["{func}"](*size)')
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
