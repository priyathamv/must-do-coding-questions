# Input:
# 2
# geeksforgeeks
# geeks for geeks

# Output:
# geksfor
# geks for

t = int(input())

for _ in range(t):
    string = input()
    length = len(string)
    strMap = {}
    for i in range(length):
        if string[i] not in strMap:
            print(string[i], end="")
            strMap[string[i]] = 1
    print()
