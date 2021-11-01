n1 = int(input(" "))
a = n1 // 100
b = n1 % 100 // 10
c = n1 % 10
c2 = c * 100
b2 = b * 10
n2 = c2 + b2 + a
print(n2)
