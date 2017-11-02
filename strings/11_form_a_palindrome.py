# Input:
# 3
# abcd
# aba
# geeks
#
# Output:
# 3
# 0
# 3

def formPalindrome(string, n):
    arr = [[0 for i in range(n)] for j in range(n)]
    for l in range(2, n+1):     # substrings of length 2 to n
        for i in range(n-l+1):  # i is the start index
            j = i+l-1           # j is the end index
            if string[i] == string[j]:
                arr[i][j] = arr[i+1][j-1]
            else:
                arr[i][j] =  min(arr[i][j-1], arr[i+1][j]) + 1
    return arr[0][-1]

for _ in range(int(input())):
    string = input()
    length = len(string)
    print(formPalindrome(string, length))
