import random
import sys
def check_func(sort_func):
    n = random.randint(10, 20)
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 100))

    print "######begin sort######"
    print "numbers list is:", nums
    nums_sort = sort_func(nums)
    print "######after sort######"
    print "numbers list is:", nums_sort
    for i in range(1, len(nums_sort)):
        if nums_sort[i-1] > nums_sort[i]:
            print "Sorted failed! Please check the code again!"
            sys.exit(1)
    else:
        print "Congratulations! Sorted successfully!"
