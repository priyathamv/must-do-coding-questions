# Input:
# 2
# i.like.this.program.very.much
# pqr.mno

# Output:
# much.very.program.this.like.i
# mno.pqr

t = int(input())

for _ in range(t):
    arr = [ele for ele in input().split(".")]
    n = len(arr)
    final_str = ""
    for i in range(n-1, -1, -1):
        if i != n-1:
            final_str += "."
        final_str += arr[i]
    print(final_str)
