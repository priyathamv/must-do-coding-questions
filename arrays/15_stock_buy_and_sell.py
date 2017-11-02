# Input:
# 2
# 7
# 100 180 260 310 40 535 695
# 10
# 23 13 25 29 33 19 34 45 65 67

# Output:

# (0 3) (4 6)
# (1 4) (5 9)

t = int(input())

for _ in range(t):
    n   = int(input())
    arr = [int(ele) for ele in input().split()]
    i   = 0
    bought_flag = 0
    sold_flag   = 1

    bought_index    = 0
    sold_index      = 0
    flag = 0
    while i < n:
        if bought_flag == 0:
            while i+1 < n and arr[i] > arr[i+1]:
                i += 1
            bought_index = i
            sold_flag = 0
            bought_flag = 1
        else:
            while i+1 < n and arr[i] < arr[i+1]:
                i += 1
            sold_index = i
            print("(%d %d)" % (bought_index, sold_index), end=" ")
            sold_flag = 1
            bought_flag = 0
            flag = 1
        i += 1
    if flag == 0:
        print("No Profit")
    else:
        print()
