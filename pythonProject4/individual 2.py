#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    A = tuple(map(float, input("Введите значения U: ").split()))
    m = 999999999999
    n = 0
    count = 1
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    for item in A:
        if item > 0:
            count *= item
    print('Произведение положительных элементов', count)
    for i, a in enumerate(A):
        if m > A[i]:
            m = A[i]
            n = i
    c = A[:n]
    s = sum(c)
    print("Сумма перед минимальным числом", s)
    chet = ()
    nechet = ()
    for i, a in enumerate(A):
        if i % 2 == 0:
            chet = chet + (A[i], )
        else:
            nechet = nechet + (A[i], )
    q = tuple(sorted(chet, ))
    y = tuple(sorted(nechet, ))
    print('По возрастанию на чётных местах', q)
    print('По возрастанию на нечётных местах', y)
