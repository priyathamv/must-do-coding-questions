# Input
# 2
# abababcdefababcdab
# geeksforgeeks


# Output:
# 6
# 7

t = int(input())

for _ in range(t):
    string = input()
    length = len(string)
    arr = [[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        arr[i][i] = 1

    max_len = 1
    for i in range(length):
        for j in range(length):
            if i < j and string[j] not in string[i:j]:
                arr[i][j] = arr[i][j-1] + 1
                if arr[i][j] > max_len:
                    max_len = arr[i][j]
    print(max_len)
