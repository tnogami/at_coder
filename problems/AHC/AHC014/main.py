from collections import defaultdict
from itertools import combinations
N, M = map(int, input().split())
dots = []
dots_set = set(dots)
x_pos_group = defaultdict(list)
y_pos_group = defaultdict(list)
zero_dist_group = defaultdict(list)
n_dist_group = defaultdict(list)
x_lines = []
y_lines = []
zero_lined = []
n_lined = []
ans = []

for m in range(M):
    x, y = map(int, input().split())
    dots.append((x,y))
    x_pos_group[x].append(m)
    y_pos_group[y].append(m)
    zero_dist_group[x+y].append(m)
    n_dist_group[N-1-x+y].append(m)

isContinue = True

while isContinue:
    isContinue = False

    for x, x_dot_nums in x_pos_group.items(): #座標ごとのループ
        if len(x_dot_nums) == 1: continue #x座標のdotが1つしかない場合はcontinue
        for i, j in combinations(x_dot_nums, 2): #x座標のdotを2つ選ぶ
            if dots[i][1] in y_pos_group: #i番目のdotのy座標がy座標の集合に含まれている
                for y_dot_num in y_pos_group[dots[i][1]]: #y座標のdotでループ
                    another_x = dots[j][0]
                    pos = (another_x, dots[y_dot_num])
                    if pos not in dots_set:
                        dots_set.add(pos)
                        ans.append([dots[i][0], dots[i]1, dots[j][0], dots[j][1], another_x, dots[y_dot_num][1], dots[i][0], dots[j][1]])





print(len(ans))
for a in ans:
    print(*a)

