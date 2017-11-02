# Input:
# 1
# 5
# 3 2 4 6 5
# Output:
# Yes

t = int(input())
for _ in range(t):
    n   = int(input())
    arr = [int(ele) ** 2 for ele in input().split()]
    arr = sorted(arr)

    if n < 3:
        print("No")
    else:
        flag = 0
        for i in range(n-1, 1, -1):
            l, r, cur_ele = 0, i-1, arr[i]
            while l < r:
                temp = arr[l] + arr[r]
                if temp == cur_ele:
                    print("Yes")
                    flag = 1
                    break
                elif temp > cur_ele:
                    r -= 1
                else:
                    l += 1
            if flag == 1:
                break
        if flag == 0:
            print("No")
