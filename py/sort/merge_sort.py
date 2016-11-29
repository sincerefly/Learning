#!/bin/env python3
# -*- coding: utf-8 -*-

import random
from collections import deque


def merge(left, right):

    '''
    将两个有序队列合并为一个有序队列
    '''

    merged, left, right = deque(), deque(left), deque(right)
    while left and right:
        merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
    merged.extend(right if right else left)
    #print(merged)

    return list(merged)


def merge_sort(data):

    '''
    归并排序(merge sort)
    '''

    if len(data) <= 1:
        return data

    middle = int(len(data) // 2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    #print(left, right)
    return merge(left, right)


if __name__ == '__main__':

    data = random.sample(range(100), 6)

    print(data)
    print(merge_sort(data))




