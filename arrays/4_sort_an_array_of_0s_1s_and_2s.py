t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    i, l, r = 0, 0, n-1
    while i <= r:
        if arr[i] == 2:
            temp = arr[i]
            arr[i] = arr[r]
            arr[r] = temp
            r -= 1
        elif arr[i] == 0:
            temp = arr[i]
            arr[i] = arr[l]
            arr[l] = temp
            l += 1
            i += 1
        else:
            i += 1
    print(" ".join(map(str, arr)))
