# Input:
# 3
# {([])}
# ()
# ()[]

# Output:
# balanced
# balanced
# balanced

t = int(input())

for _ in range(t):
    string = input()
    flag = 0
    arr = []
    for char in string:
        if char == '{' or char == '[' or char == '(':
            arr.append(char)
        else:
            if not arr:
                print("not balanced")
                flag = 1
                break
            popped_char = arr.pop()
            if (popped_char == '{' and char != '}') or \
                (popped_char == '[' and char != ']') or \
                (popped_char == '(' and char != ')'):
                    print("not balanced")
                    flag = 1
                    break
    if flag == 0 and arr:
        flag = 1
        print("not balanced")
    if flag == 0:
        print("balanced")
