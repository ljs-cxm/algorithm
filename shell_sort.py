# coding: utf-8
from check import check_func

'''shell排序相当于分组插入排序，先分成n=len(nums)/2组，每组2个元素，第一组的索引是[0, len(nums)/2],
第二组是[1, len(nums)/2+1]...，对每一组分别执插入排序
然后对n = n/2,直到n=1为止，就是插入排序'''
# def shellSort(items):
#   inc = len(items) / 2
#   while inc:
#     for i in xrange(len(items)):
#       j = i
#       temp = items[i]
#       while j >= inc and items[j-inc] > temp:
#         items[j] = items[j - inc]
#         j -= inc
#       items[j] = temp
#     inc = inc/2 if inc/2 else (0 if inc==1 else 1)
# a = [35, -8, 11, 1, 68, 0, 3];
# shellSort(a)
# print a # [-8, 0, 1, 3, 11, 35, 68]

def shell_sort_func(nums):
    n = len(nums)
    inc = n / 2

    while inc:
        for i in range(inc, n):
            j = i
            tmp = nums[i]
            while j >= inc and nums[j-inc] > tmp:   #对分组[i, i+inc, i+2inc, ...]这个小组进行插入排序
                nums[j] = nums[j-inc]
                nums[j-inc] = tmp
                j -= inc
        inc /= 2
    return nums

if __name__ == '__main__':
    check_func(shell_sort_func)