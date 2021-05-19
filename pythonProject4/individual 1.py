#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':

    U = tuple([random.randint(20, 30) for i in range(7)])
    D = tuple([random.randint(20, 30) for i in range(7)])
    V = tuple([random.randint(20, 30) for i in range(7)])
    G = ()
    for (u, d, v) in zip(U, D, V):
        (Z, ) = ((u+d+v)/3, )
        G = G + (Z, )
    print("Среднее значение температуры по дням недели: ", G)
