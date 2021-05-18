#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':

    U = tuple([random.randint(20, 30) for i in range(7)])
    D = tuple([random.randint(20, 30) for i in range(7)])
    V = tuple([random.randint(20, 30) for i in range(7)])
    G = ()
    i = 0
    while i < 7:
        (Z, ) = ((U[i]+D[i]+V[i])/3, )
        G = G + (Z, )
        i += 1
    print("Среднее значение температуры по дням недели: ", G)
