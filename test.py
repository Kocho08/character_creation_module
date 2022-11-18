from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Функция вычисления корня из вашего числа."""
    if your_number >= 0:
        return calculate_square_root(your_number)


root = calculate_square_root(0)
print('Мы вычислили корень квадратный из введённого вами числа. '
      'Это будет:', calc(25.5))
