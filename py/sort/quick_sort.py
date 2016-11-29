#!/bin/env python3
# -*- coding: utf-8 -*-

import random
import copy


def quick(data):

    '''
    快速排序(quick sort)
    '''

    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        return quick([x for x in data[1:] if x < pivot]) + \
               [pivot] + \
               quick([x for x in data[1:] if x >= pivot])


if __name__ == '__main__':

    data = random.sample(range(100), 6)

    print(data)
    print(quick(data))




