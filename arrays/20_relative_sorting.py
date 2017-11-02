# Input:
# 1
# 11 4
# 2 1 2 5 7 1 9 3 6 8 8
# 2 1 8 3

# Output:
# 2 2 1 1 8 8 3 5 6 7 9

t = int(input())

for _ in range(t):
    n1, n2 = [int(ele) for ele in input().split()]
    arr1 = [int(ele) for ele in input().split()]
    arr2 = [int(ele) for ele in input().split()]

    arr1Map = {}
    remaining_arr = []
    for ele in arr1:
        if ele in arr1Map:
            arr1Map[ele] = arr1Map[ele] + 1
        else:
            arr1Map[ele] = 1
        if ele not in arr2:
            remaining_arr.append(ele)

    sorted_array = []
    for ele in arr2:
        if ele in arr1Map:
            n = arr1Map[ele]
            while n > 0:
                sorted_array.append(ele)
                n -= 1

    sorted_array.extend(sorted(remaining_arr))
    print(" ".join([str(ele) for ele in sorted_array]))
