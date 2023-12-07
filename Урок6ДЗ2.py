x = int(input("Введите число х: "))
r = 0
for i in range (1, x + 1):
    if x % i == 0:
        r += 1
print(r)