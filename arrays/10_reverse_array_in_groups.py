# Input
# 1
# 5
# 1 2 3 4 5
# 3
# Output
# 3 2 1 5 4

def reverse(arr, l, r):
    temp    = 0
    mid     = (l + r) // 2
    for i in range(l, mid + 1):
        temp            = arr[i]
        arr[i]          = arr[r + l - i]
        arr[r + l - i]  = temp

t = int(input())

for _ in range(t):
    n   = int(input())
    arr = [int(ele) for ele in input().split()]
    k   = int(input())

    for i in range(0, n, k):
        r = i + k - 1 if (i + k - 1) < n else n - 1
        reverse(arr, i, r)

    for ele in arr:
        print(ele, end=" ")
    print()
