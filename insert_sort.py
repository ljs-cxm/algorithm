from check import check_func

def insert_sort_func(nums):
    n = len(nums)
    for i in range(1, n):
        s = i - 1
        tmp = nums[i]
        while tmp < nums[s] and s >= 0:
            nums[s+1] = nums[s]
            nums[s] = tmp
            s -= 1
    return nums

if __name__ == '__main__':
    check_func(insert_sort_func)