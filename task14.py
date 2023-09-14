# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Num = abs(int(input('Введите число Num: ')))
stop = 0
P = 2
for i in range(Num):
    if stop != 1:
        P = P ** i
        if P <= Num:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = Num
