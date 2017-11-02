# Input:
# 2
# 7
# 4 3 7 8 6 2 1
# 4
# 1 4 3 2
# Output:
# 3 7 4 8 2 6 1
# 1 4 2 3

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]

    flag = False
    for i in range(n-1):
        if flag == False and arr[i] > arr[i+1]:
            swap(arr, i, i+1)
        if flag == True and arr[i] < arr[i+1]:
            swap(arr, i, i+1)
        flag = not flag
    for ele in arr:
        print(ele, end=" ")
    print()
