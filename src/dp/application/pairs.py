"""
https://kompege.ru/task, 2720

На вход программы поступает последовательность из N целых положительных чисел. Рассматриваются все пары различных
элементов последовательности. Необходимо определить количество пар чисел, произведение которых кратно 7.
"""

f = open("226-B.txt")
n = int(f.readline())
d = 7
k = [0] * d
count = 0
for _ in range(n):
    x = int(f.readline())
    """
    if x % d == 0:
        count += k[0]
    elif x % d == 1:
        count += k[9]
    elif x % d == 2:
        count += k[8]
    ...
    """
    count += k[(d - (x % d)) % d]
    k[x % d] += 1
print(count)
