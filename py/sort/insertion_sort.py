#!/bin/env python3
# -*- coding: utf-8 -*-

import random
import copy


def insertion(data):

    '''
    插入排序(insertion sort)
    '''

    N = len(data)
    if N==1: return data

    count = 0
    for i in range(1, N):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                count = count + 1
                data[j-1], data[j] = data[j], data[j-1]

    return (data, count)


if __name__ == '__main__':

    data = random.sample(range(100), 6)

    print(data)
    print(insertion(data))




