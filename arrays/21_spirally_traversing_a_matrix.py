# Input:
# 1
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Output:
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

t = int(input())

for _ in range(t):
    rows, cols = 4, 4
    arr = [ [0] * cols ] * rows
    for i in range(rows):
        arr[i] = [int(ele) for ele in input().split()]

    start_row, end_row = 0, 3
    start_col, end_col = 0, 3

    while start_row < end_row and start_col < end_col:

        for j in range(start_col, end_col+1):
            print(arr[start_row][j], end=" ")
        start_row += 1

        for i in range(start_row, end_row+1):
            print(arr[i][end_col], end=" ")
        end_col -= 1

        for j in range(end_col, start_col-1, -1):
            print(arr[end_row][j], end=" ")
        end_row -= 1

        for i in range(end_row, start_row-1, -1):
            print(arr[i][start_col], end=" ")
        start_col += 1
    print()
