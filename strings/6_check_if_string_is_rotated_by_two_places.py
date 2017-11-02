# Input:
# 2
# amazon
# azonam
# geeksforgeeks
# geeksgeeksfor
#
# Output:
# 1
# 0

t = int(input())

for _ in range(t):
    str1 = input()
    str2 = input()
    n1, n2 = len(str1), len(str2)

    if n1 != n2 or (n1 < 3 and str1 != str2):
        print(0)
        continue

    if (str1[n1-2] == str2[0] and str1[n1-1] == str2[1] and str1[:n1-2] == str2[2:]) or \
    (str1[0] == str2[n2-2] and str1[1] == str2[n2-1] and str1[2:] == str2[:n2-2]):
        print(1)
    else:
        print(0)
