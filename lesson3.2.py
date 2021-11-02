a = input("Введите что нибудь: ")
b = "замена в строке"
c = f'Это строка в которую {a} новую строку'
print(c)

x = c.replace(a, b)
print(x)

print(len(c))

if "строка" in c:
    print("Да")
else:
    print("Нет")
