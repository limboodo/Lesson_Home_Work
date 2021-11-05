n = int(input("Введите значение: "))
for i in range(n + 1):
    for j in range(n - i):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
