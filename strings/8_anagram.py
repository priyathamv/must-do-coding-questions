# Input:
# 2
# geeksforgeeks
# forgeeksgeeks
# allergy
# allergic

# Output:
# YES
# NO

t = int(input())

for _ in range(t):
    str1 = input()
    str2 = input()
    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        print("NO")
        continue

    str1Map = {}
    for i in range(len1):
        if str1[i] not in str1Map:
            str1Map[str1[i]] = 1
        else:
            str1Map[str1[i]] += 1

    flag = 0
    for i in range(len2):
        if str2[i] not in str1Map or str1Map[str2[i]] <= 0:
            print("NO")
            flag = 1
            break
        else:
            str1Map[str2[i]] -= 1

    if flag == 0:
        print("YES")
