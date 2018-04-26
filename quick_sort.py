# coding: utf-8
from check import check_func

def partition(nums, i, j):
    '''最后这个i位置其实就是tmp，因为每次交换tmp之后，tmp的下标就不动了，直到下一次交换，最后中间值肯定是这个tmp'''
    tmp = nums[i]

    while i != j:
        while i != j and nums[j] >= tmp:
            j -= 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
        while i != j and nums[i] <= tmp:
            i += 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
    return i

def quick_sort_digui(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort_digui(nums, left, mid-1)
        quick_sort_digui(nums, mid + 1, right)

def quick_sort_func(nums):
    quick_sort_digui(nums, 0, len(nums)-1)
    return nums

if __name__ == '__main__':
    check_func(quick_sort_func)
