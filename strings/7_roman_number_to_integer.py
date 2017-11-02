# Input
# 2
# V
# III
#
# Output
# 5
# 3

def getVal(num):
    if num == 'I':
        return 1
    if num == 'V':
        return 5
    if num == 'X':
        return 10
    if num == 'L':
        return 50
    if num == 'C':
        return 100
    if num == 'D':
        return 500
    if num == 'M':
        return 1000

t = int(input())

for _ in range(t):
    num = input()
    length = len(num)

    i = length - 1
    final_num = 0
    while i >= 0:
        if i == 0:
            final_num += getVal(num[i])

        elif i > 0 and getVal(num[i]) == getVal(num[i-1]):
            final_num += getVal(num[i]) + getVal(num[i-1])
            i -= 1

        elif i > 0 and getVal(num[i]) > getVal(num[i-1]):
            final_num += getVal(num[i]) - getVal(num[i-1])
            i -= 1

        elif i > 0 and getVal(num[i]) < getVal(num[i-1]):
            final_num += getVal(num[i])

        i -= 1
    print(final_num)
