S = input()
in_box = [False]*26
stack = [set()]

for c in S:
    if c.isalpha():
        idx = ord(c) - ord('a')
        if in_box[idx]:
            print('No')
            break
        else:
            in_box[idx] = True
            stack[-1].add(c)
    elif c == '(':
        cluster = set()
        stack.append(cluster)
    else:
        cluster = stack.pop()
        for s in cluster:
            idx = ord(s) - ord('a')
            in_box[idx] = False
else:
    print("Yes")






