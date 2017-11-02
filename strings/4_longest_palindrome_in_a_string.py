# Input:
# 1
# aaaabbaa
#
# Output:
# aabbaa

t = int(input())

for _ in range(t):
    string  = input()
    n       = len(string)
    a = [[0] * n for i in range(n)]

    if n == 1:
        print(string)
        continue

    for i in range(n):
        arr[i][i] = 1

    max_len = 1
    start_index = 0

    for i in range(n-1):
        if string[i] == string[i+1]:
            arr[i][i+1] = 1
            cur_len = 2
            if cur_len > max_len:
                max_len = 2
                start_index = i

    for k in range(3, n+1):
        for i in range(0, n-k+1):
            j = i + k - 1
            if string[i] == string[j] and arr[i+1][j-1] == 1:
                arr[i][j] = 1
                if k > max_len:
                    max_len = k
                    start_index = i
    print(string[start_index:start_index+max_len])
