from collections import Counter
import random

a = [random.randint(0, 9) for i in list(range(10))]
b = [random.randint(0, 9) for y in list(range(10))]
print("Первый список чисел:", a)
print("Второй список чисел:", b)
print("Уникальные числа:", len(Counter(a).keys()))
print("Уникальные числа:", len(Counter(b).keys()))
print("Уникальные числа двух списков:", len(Counter(a+b).keys()))

#Попытка написать код в одну строку ниже, вроде тоже самое но не уверен насколько это грамотно
print(len(Counter([random.randint(0, 9) for o in list(range(10))]+[random.randint(0, 9) for d in list(range(10))]).keys()))
