# Input:
# 2
# 4
# geeksforgeeks geeks geek geezer
# 3
# apple ape april

# Output:
# gee
# ap

t = int(input())

for _ in range(t):
    k = int(input())
    string_arr = [ele for ele in input().split(" ")]

    if  k == 1:
        print(string_arr[0])
        continue
    arr = []
    small_str_len = len(string_arr[0])
    for string in string_arr:
        cur_len = len(string)
        if cur_len < small_str_len:
            small_str_len = cur_len
        arr.append(list(string))

    i = 0
    final_str = ""
    flag = 0
    while i < small_str_len and flag == 0:
        cur_char = arr[0][i]
        for j in range(1, k):
            if cur_char != arr[j][i]:
                flag = 1
                break
        if flag == 0:
            final_str += cur_char
        i += 1

    if final_str == "":
        print(-1)
    else:
        print(final_str)
