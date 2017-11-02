# Input:
# 2
# 4
# 7 4 0 9
# 3
# 6 9 9

# Output:
# 10
#  0

t = int(input())

for _ in range(t):
    n   = int(input())
    arr = [int(ele) for ele in input().split()]
    right_max_arr   = [0] * n
    left_max_arr    = [0] * n

    right_max_ele   = -1
    left_max_ele    = -1

    for i in range(n):
        if arr[i] > left_max_ele:
            left_max_ele = arr[i]
        left_max_arr[i] = left_max_ele

        if arr[n-1-i] > right_max_ele:
            right_max_ele = arr[n-1-i]
        right_max_arr[n-1-i] = right_max_ele

    result = 0
    for i in range(1, n-1):
        cur_height = min(left_max_arr[i], right_max_arr[i])
        if arr[i] < cur_height:
            result += cur_height - arr[i]
    print(result)
