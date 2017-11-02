# Input:
# 2
# ABC
# ABSG
#
# Output:
# ABC ACB BAC BCA CAB CBA
# ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

def permutate(cur_list, l, r):
    if l == r:
        print("".join(cur_list), end=" ")
    else:
        for i in range(l, r+1):
            cur_list[l], cur_list[i] = cur_list[i], cur_list[l]
            permutate(cur_list, l+1, r)
            cur_list[l], cur_list[i] = cur_list[i], cur_list[l]

t = int(input())

for _ in range(t):
    string = input()
    permutate(list(string), 0, len(string)-1)
    print()
