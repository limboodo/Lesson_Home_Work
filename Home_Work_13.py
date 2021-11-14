a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Введите операцию: ')


def arithmetic(a, b, c):
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a / b)
    else:
        print("Неизвестная операция")


arithmetic(a, b, c)
