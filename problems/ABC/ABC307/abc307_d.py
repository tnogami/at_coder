N = int(input())
S = input()

start = 0

stack = []

for s in S:
    if s == '(':
        start += 1
        stack.append('(')

    elif s == ')':
        if start != 0:
            while stack:
                t = stack.pop()
                if t == '(':
                    break
            start -= 1
        else:
            start = 0
            stack.append(')')
    else:
        stack.append(s)

print(''.join(stack))


ｓｄｌ
