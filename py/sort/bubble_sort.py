#!/bin/env python3
# -*- coding: utf-8 -*-

import random
import copy


def bubble(data):

    '''
    冒泡排序(bubble sort)
    '''

    count = 0
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            count = count + 1
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]

    return (data, count)


def bubble2(data):

    '''
    冒泡排序- 优化(bubble sort)
    当内层j循环一遍没有发生交换时，排序已经完成，设立exchange判断并跳出
    '''

    count = 0
    for i in range(len(data)-1, 0, -1):
        exchange = False
        for j in range(0, i):
            count = count + 1
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
                exchange = True

        if not exchange:
            return (data, count)

    return (data, count)



if __name__ == '__main__':

    data = random.sample(range(100), 6)
    #data = [1, 2, 3, 4, 5, 6] # 当有序时，冒泡排序的最佳时间复杂度为O(n)
    #data = [1, 2, 3, 4, 5, 6][::-1]
    data2 = copy.deepcopy(data)

    print(data)
    print(bubble(data))
    print(bubble2(data2))




