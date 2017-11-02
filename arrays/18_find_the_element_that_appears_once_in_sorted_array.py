# Input:

# 1
# 11
# 1 1 2 2 3 3 4 50 50 65 65
# 0 1 2 3 4 5 6  7  8  9 10
# l         m             r

# Output:

# 4

def binarySearch(arr, l, r):
    if l > r:
        return -1

    if l == r:
        return arr[l]

    mid  = (l + r) // 2
    if (mid % 2) == 0:
        if arr[mid] == arr[mid+1]:
            return binarySearch(arr, mid+2, r)
        else:
            return binarySearch(arr, l, mid)
    if (mid % 2) == 1:
        if arr[mid] == arr[mid-1]:
            return binarySearch(arr, mid+1, r)
        else:
            return binarySearch(arr, l, mid-1)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    print(binarySearch(arr, 0, n-1))
