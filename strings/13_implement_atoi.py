# Input:
# 2
# 123
# 21a
#
# Output:
# 123
# -1

def atoi(string):
    for i in range(len(string)):
        if i == 0 and ord(string[i]) == 45:
            continue
        if ord(string[i]) < 48 or ord(string[i]) > 57:
            return -1
    return int(string)
