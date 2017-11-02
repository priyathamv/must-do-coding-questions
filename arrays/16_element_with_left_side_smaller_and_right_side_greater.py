# Input:
# 3
# 4
# 4 2 5 7
# 3
# 11 9 12
# 6
# 4 3 2 7 8 9
#
# Output:
# 5
# -1
# 7

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]

    left_max    = [arr[0]] * n
    right_min   = [arr[n-1]] * n

    max_val = arr[0]
    min_val = arr[n-1]

    for i in range(1, n-1):
        if arr[i-1] > max_val:
            max_val = arr[i-1]
            left_max[i] = max_val
        else:
            left_max[i] = max_val

        if arr[n-i] < min_val:
            min_val = arr[n-i]
            right_min[n-i-1] = min_val
        else:
            right_min[n-i-1] = min_val

    flag = 0
    for i in range(1, n-1):
        if arr[i] >= left_max[i] and arr[i] <= right_min[i]:
            print(arr[i])
            flag = 1
            break
    if flag == 0:
        print(-1)
