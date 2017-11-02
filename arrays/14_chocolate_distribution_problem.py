t = int(input())

for _ in range(t):
    n       = int(input())
    arr     = [int(ele) for ele in input().split()]
    k       = int(input())
    arr     = sorted(arr)
    min_val = 100000
    for i in range(0, n - k + 1):
        cur_diff = arr[i+k-1] - arr[i]
        if  cur_diff < min_val:
            min_val = cur_diff
    print(min_val)
