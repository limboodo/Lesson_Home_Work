def product_of_all_digits(b):
    a = 1
    for i in b:
        if int(i) != 0:
            a *= int(i)
    return a


x = input('Введите число: ')
print("Произведение всех цифр:", product_of_all_digits(x))
