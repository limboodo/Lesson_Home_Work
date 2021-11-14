def square(i):
    p = 4 * i
    s = i * 2
    d = 2 ** 0.5 * i
    return (p, s, d)


print(square(int(input("Введите сторону квадрата = "))))
