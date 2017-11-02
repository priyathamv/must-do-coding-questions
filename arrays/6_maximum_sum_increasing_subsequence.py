# Input:
# 2
# 7
# 1 101 2 3 100 4 5
# 4
# 10 5 4 3

# Output:
# 106
# 10

t = int(input())

for _ in range(t):
    n   = int(input())
    arr = [int(ele) for ele in input().split()]
    max_arr = arr[:]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and max_arr[i] < max_arr[j] + arr[i]:
                max_arr[i] = max_arr[j] + arr[i]
    print(max(max_arr))
