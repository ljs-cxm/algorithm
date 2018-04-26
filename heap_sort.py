import heapq
from check import check_func

def heap_sort_func(nums):
    heapq.heapify(nums)
    return nums

if __name__ == '__main__':
    check_func(heap_sort_func)