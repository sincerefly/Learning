#!/bin/env python3
# -*- coding: utf-8 -*-

import random
import copy


def selection(data):

    '''
    选择排序(selection sort)
    '''

    N = len(data)
    count = 0
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if data[min_index] > data[j]:
                min_index = j
        if min_index != i:
            count = count + 1
            data[min_index], data[i] = data[i], data[min_index]

    return (data, count)


if __name__ == '__main__':

    data = random.sample(range(100), 6)

    print(data)
    print(selection(data))




