a = input("Введите что нибудь: ")
b = "замена в строке"
c = f'Это строка в которую {a} новую строку'
print(c)

print(c.replace(a, b))

print(len(c))

if "строка" in c:
    print("Да")
else:
    print("Нет")
