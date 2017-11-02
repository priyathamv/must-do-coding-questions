# Input:
# 1
# 5
# 5 5 4 6 4

# Output:
# 4 4 5 5 6
import operator

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]

    arrMap = {}
    for ele in arr:
        if ele not in arrMap:
            arrMap[ele] = 1
        else:
            arrMap[ele] = arrMap[ele] + 1
    sorted_arr = sorted(arrMap.items(),
                        key=operator.itemgetter(1),
                        reverse=True)

    for (key, val) in sorted_arr:
        n = val
        while n > 0:
            print(key, end=" ")
            n -= 1
    print()
