import random

height = int(input("Введите рост Пети: "))
a = [random.randint(130, 200) for i in list(range(15))]
print(a)
a.sort(reverse=True)
print(a)
result = 0
while result < len(a) and a[result] >= height:
    result += 1
print("Место в строю:", result + 1)
