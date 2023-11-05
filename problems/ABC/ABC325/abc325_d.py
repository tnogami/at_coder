
from heapq import heapify, heappop, heappush

N = int(input())
waiting_list = []
ending_list = []

for _ in range(N):
    start, duration = map(int, input().split())
    waiting_list.append((start, duration))

heapify(waiting_list)
ans = 0

cur_time, _ = heappop(waiting_list)
heappush(waiting_list, (cur_time, _))
while waiting_list or ending_list:
    if not ending_list:
        # 次の開始時間を確認
        start, duration = heappop(waiting_list)
        if start >= cur_time:
            cur_time = start
        heappush(waiting_list, (start, duration))

        # start == cur_timeまで捨てる
        while waiting_list:
            start, duration = heappop(waiting_list)
            if start > cur_time:
                heappush(waiting_list, (start, duration))
                break
            elif start == cur_time:
                heappush(ending_list, start + duration)
            else:
                continue
    else:
        # start == cur_timeまで捨てる
        while waiting_list:
            start, duration = heappop(waiting_list)
            if start > cur_time:
                heappush(waiting_list, (start, duration))
                break
            elif start == cur_time:
                heappush(ending_list, start + duration)
            else:
                continue

    while ending_list:
        end_time = heappop(ending_list)
        if end_time < cur_time:
            continue
        ans += 1
        cur_time += 1
        break

        

    while ending_list:
        end_time = heappop(ending_list)
        if end_time == cur_time:
            ans += 1
            cur_time += 1
        elif end_time > cur_time:
            heappush(ending_list, end_time)
            break

while ending_list:
    end_time = heappop(ending_list)
    if end_time < cur_time:
        continue
    ans += 1
    cur_time += 1

print(ans)
