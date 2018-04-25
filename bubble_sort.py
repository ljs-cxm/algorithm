# coding: utf-8
# !/usr/bin/python
from check import check_func

def bubble_sort_func(nums):
    '''冒泡排序，小的往低序号排'''
    n = len(nums)

    for i in range(n):
        for j in range(n-1,i,-1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

if __name__ == '__main__':
    check_func(bubble_sort_func)