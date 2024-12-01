import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	# Используем eval для вычисления результата, результат теперь возвращается, а не выводится
	result = eval(f'{fig}.{func}(*{size})')
	return result  # Возвращаем результат вместо печати


if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()

	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")

	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")

	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

	result = calc(fig, func, size)  # Получаем результат из функции
	print(f'{func} of {fig} is {result}')  # Печатаем результат


