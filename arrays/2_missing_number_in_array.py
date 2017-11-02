t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    arr_sum = 0
    for ele in arr:
        arr_sum = arr_sum + ele
    true_sum = n * (n + 1) // 2
    print(true_sum - arr_sum)
