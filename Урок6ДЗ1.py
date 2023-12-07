n = int(input("Количество чисел"))
count = 0
for i in range(n):
    u = int(input("Введите целое число"))
    if u == 0:
        count += 1
print ("Количество нулевых чисел", count)