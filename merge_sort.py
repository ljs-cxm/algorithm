from check import check_func

def merge(l_nums, r_nums):
    l_n = len(l_nums)
    r_n = len(r_nums)

    i, j = 0, 0
    merge_list = []
    while i < l_n and j < r_n:
        if l_nums[i] <= r_nums[j]:
            merge_list.append(l_nums[i])
            i += 1
        else:
            merge_list.append(r_nums[j])
            j += 1
    merge_list += l_nums[i:]
    merge_list += r_nums[j:]
    return merge_list

def merge_sort_func(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) / 2
    l_nums = merge_sort_func(nums[:mid])
    r_nums = merge_sort_func(nums[mid:])
    return merge(l_nums, r_nums)

if __name__ == '__main__':
    check_func(merge_sort_func)