# Input
# 2
# GeeksForGeeks Fr
# GeeksForGeeks For
#
# Output
# -1
# 5

def strstr(string, substring):
    str_len     = len(string)
    sub_str_len = len(substring)
    for i in range(str_len - sub_str_len + 1):
        j = i
        k = 0
        while k < sub_str_len and string[j] == substring[k]:
            j += 1
            k += 1
        if k == sub_str_len:
            return i
    return -1
