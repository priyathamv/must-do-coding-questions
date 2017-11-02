# Input:
# 2
# 6
# 16 17 4 3 5 2
# 5
# 1 2 3 4 0
# Output:
# 17 5 2
# 4 0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    max_val = -1
    result = ""
    for i in range(n-1, -1, -1):
        if arr[i] > max_val:
            result = str(arr[i]) + " " + result
            max_val = arr[i]
    print(result)
