from check import check_func
def select_sort_func(nums):
    n = len(nums)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if nums[min] > nums[j]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums
if __name__ == '__main__':
    check_func(select_sort_func)