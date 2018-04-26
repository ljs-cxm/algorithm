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
    nums.sort()
    print "sort number  is:", nums
    print "######after sort######"
    print "numbers list is:", nums_sort
    if nums != nums_sort:
        print "Sorted failed! Please check the code again!"
        sys.exit(1)
    else:
        print "Congratulations! Sorted successfully!"
