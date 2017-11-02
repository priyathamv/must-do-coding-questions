t = int(input())

for _ in range(t):
    n, given_sum = [int(x) for x in input().split()]
    arr = [int(ele) for ele in input().split()]
    flag = 0
    table = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                table[i][j] = arr[j]
            elif i < j:
                table[i][j] = table[i][j-1] + arr[j]
            else:
                table[i][j] = 0
            if table[i][j] == given_sum:
                print(str(i+1) + " " + str(j+1))
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        print(-1)
