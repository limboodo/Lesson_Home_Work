a = input("Введите что нибудь: ")
b = "замена в строке"
c = 'Это строка в которую новую строку' + a
print('Это строка в которую', a, 'новую строку')

if a in c:
    print('Это строка в которую', b, 'новую строку')
    print(len(c))

if "строка" in c:
    print("Да")
else:
    print("Нет")
