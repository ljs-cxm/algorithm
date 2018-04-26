from check import check_func
import math

def radix_sort_func(nums):
    k = int(math.ceil(math.log(max(nums)+1, 10)))
    list = nums[:]

    for i in range(k):
        s = [[] for _ in range(10)]
        for j in list:
            s[j / (10**i) % 10].append(j)
        list = [a for b in s for a in b]
        del s
    return list

if __name__ == '__main__':
    check_func(radix_sort_func)