
N, M = map(int, input().split())
words_length = list(map(int, input().split()))

max_length = max(words_length)

ng = max_length - 1
ok = sum(words_length) + len(words_length)


def check(width):
    cur_width = 0
    line_ct = 1
    for l in words_length:
        if cur_width + l <= width:
            cur_width += l + 1
        else:
            line_ct += 1
            cur_width = l + 1

    return line_ct <= M


while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid


print(ok)
