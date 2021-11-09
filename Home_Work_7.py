import random

a = [random.randint(0, 9) for i in list(range(10))]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print("Список чисел:", a)
print("Количесвто элементов больше своих соседей:", counter)
