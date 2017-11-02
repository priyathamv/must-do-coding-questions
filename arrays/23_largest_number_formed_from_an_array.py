# Input:
# 2
# 5
# 3 30 34 5 9
# 4
# 54 546 548 60
#
# Output:
# 9534330
# 6054854654

import functools

def customCompare(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return -1
    elif int(str(a) + str(b)) < int(str(b) + str(a)):
        return 1
    else:
        return 0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    print("".join([str(ele) for ele in sorted(arr, key=functools.cmp_to_key(customCompare))]))
