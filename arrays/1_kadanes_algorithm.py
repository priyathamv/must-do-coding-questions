t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    temp = 0

    arr = [int(ele) for ele in input().split()]
    max_val = arr[0]

    for cur_ele in arr:
        if temp + cur_ele > 0:
            temp = temp + cur_ele
            if temp > max_val:
                max_val = temp
        else:
            temp = 0
    print(max_val)
