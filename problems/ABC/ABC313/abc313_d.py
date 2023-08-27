N, K = map(int, input().split())

bit = ['']*N
question = list(range(1, K+1))
idx = 1
for n in range(1, N+1):
    if n != N:
        print('? ' + ' '.join(map(str, question)))
        reply = int(input())
        if reply == 0:
            bit[question[-idx]-1] = 'a'
        else:
            bit[question[-idx]-1] = 'b'

        if question[-idx] != (N-idx+1):
            question[-idx] += 1
        else:
            idx += 1
            question[-idx] += 1

    else:
        question = list(range(N+1-K, N+1))
        print('? ' + ' '.join(map(str, range(N+1-K, N+1))))
        reply = int(input())
        ct = 0
        for c in bit[N+1-K:]:
            if c == 'a':
                ct += 1
        if reply == ct % 2:
            d = {'a': (reply+1) % 2, 'b': reply}
        else:
            d = {'a': reply, 'b': (reply+1) % 2}

        ans = []
        for b in bit:
            if b == '':
                ans.append('')
            else:
                ans.append(d[b])

        ct = 0
        for i, q in enumerate(question):
            if i == 0:
                continue
            ct += ans[q-1]
        if ct % 2 == 0 and reply == 0:
            ans = [0] + ans
        elif ct % 2 == 0 and reply == 1:
            ans = [1] + ans
        elif ct % 2 == 1 and reply == 0:
            ans = [1] + ans
        else:
            ans = [0] + ans

        print('! ' + ' '.join(map(str, ans)))
