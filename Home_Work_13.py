def arithmetic():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = input('Введите операцию: ')
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '*':
        d = a * b
    elif c == '/':
        d = a / b
    else:
        d = "Незвестная операция"
    return d


print(arithmetic())
