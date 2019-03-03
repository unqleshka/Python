b = int(input("Введите количество элементов"+" "))
a = [0] * b
s=-1000000000000000000
for i in range(len(a)):
    i = str(i + 1)
    print("Введите элемент массива " + i+" ", end = "")
    i = int(i)
    i = i - 1
    a[i] = int(input())
print("")
for i in range(len(a)):
    if a[i] > s:
        s = a[i]
print("Максимальное число = " + str(s))
