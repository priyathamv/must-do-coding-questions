# INPUT:
# 1
# 6
# 900  940 950  1100 1500 1800
# 910 1200 1120 1130 1900 2000
#
# OUTPUT:
# 3

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    dep = [int(ele) for ele in input().split()]

    arr_sorted = sorted(arr)
    dep_sorted = sorted(dep)

    i, j, platforms,  max_platforms = 1, 0, 1, 1
    while i < n and j < n:
        if arr_sorted[i] < dep_sorted[j]:
            i += 1
            platforms += 1
            if platforms > max_platforms:
                max_platforms = platforms
        else:
            j += 1
            platforms -= 1
    print(max_platforms)
