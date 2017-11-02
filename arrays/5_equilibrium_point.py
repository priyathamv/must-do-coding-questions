t = int(input())

for _ in range(t):
    n       = int(input())
    arr     = [int(ele) for ele in input().split()]
    flag    = 0

    for i in range(n):
        left    = 0 if i == 0 else left + arr[i-1]
        right   = sum(arr) - left - arr[i]
        if left == right:
            print(i + 1)
            flag = 1
            break
    if flag == 0:
        print(-1)
