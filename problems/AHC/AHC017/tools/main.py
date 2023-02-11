from copy import copy
import math
from collections import deque
import itertools
import numpy as np
    

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


def last_check(output, remove_edge_candidate, day):
    # print("aaaa")
    global N
    global M
    # 連結のチェック
    uf = UnionFind(N)
    # print(remove_edge_candidate)
    for idx in range(M):
        if idx in remove_edge_candidate:continue
        uf.union(edges[idx][2], edges[idx][3])
        # print(uf.size(0),idx,edges[idx][2], edges[idx][3])
    if uf.size(0) == N: #連結なのでOK
        for idx in remove_edge_candidate:
            output[idx] = day
        return

    # どの辺をスワップするか確認
    reverse_edges = dict()
    for idx in remove_edge_candidate:
        idx_u, idx_v = edges[idx][2], edges[idx][3]
        if uf.same(idx_u, idx_v):continue
        uf.union(idx_u, idx_v)
        reverse_edges[idx] = remove_edge_candidate[idx]
        if uf.size(0) == N:
            break

    # 残りのedgeで連結になるようなものが組めるか確かめる
    req_ct = len(reverse_edges)
    for new_d in range(1, day):#1日目から確認
        swap_candidate_idx = set([idx for idx, _day in enumerate(output) if _day == new_d])
        for swap_list in itertools.combinations(swap_candidate_idx, req_ct):
            # 連結のチェック
            uf1 = UnionFind(N)
            for idx in range(M):
                if idx in reverse_edges:continue
                if idx in swap_candidate_idx and idx not in swap_list: continue
                uf1.union(edges[idx][2], edges[idx][3])

            uf2 = UnionFind(N)
            for idx in range(M):
                if idx in swap_list:continue
                if idx in remove_edge_candidate and idx not in reverse_edges: continue
                uf2.union(edges[idx][2], edges[idx][3])

            if uf1.size(0) == N and uf2.size(0) == N: #連結なのでOK
                for idx in remove_edge_candidate:
                    output[idx] = day
                for idx in swap_list:
                    output[idx] = day
                for idx in reverse_edges:
                    output[idx] = new_d
                return


N, M, D, K = map(int, input().split())
nodes = [[] for _ in range(N)]
dist = [[10**9]*N for _ in range(N)]
output = [-1]*M
req_for_one_day = M // D + 1
edges = []
for i in range(M):
    u, v, w = map(int, input().split())
    nodes[u-1].append((v-1, w))
    nodes[v-1].append((u-1, w))
    edges.append((w, i, u-1, v-1))

idx2pos = []
for i in range(N):
    x, y = map(int, input().split())
    idx2pos.append((x,y))

block_num = int(math.sqrt(req_for_one_day)) + 1
l = 1000//block_num
areas = [[deque() for __ in range(block_num)] for _ in range(block_num)]

for edge in edges:
    m_idx = edge[1]
    n1_idx = edge[2]
    n2_idx = edge[3]
    center_x = (idx2pos[n1_idx][0] + idx2pos[n2_idx][0])/2.0
    center_y = (idx2pos[n1_idx][1] + idx2pos[n2_idx][1])/2.0
    for i in range(block_num):
        if center_x < (i+1) * l:
            x_idx = i
            break
    for i in range(block_num):
        if center_y < (i+1) * l:
            y_idx = i
            break
    areas[y_idx][x_idx].append(m_idx)

l = list(range(M))
l = list(np.array_split(l, D)) # [array([1, 2, 3, 4]), array([5, 6, 7]), array([ 8,  9, 10])]
req_for_one_day = [0] + [len(_l) for _l in l]
x_idx = 0
y_idx = 0
ct = 0
day = 1
total = 0
remove_edge_candidate = dict()
rest_edges = set([i for i in range(M)])
while True:
    used_node = set()

# first+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # エリアに辺が存在する場合に削除候補とする
    while areas[y_idx][x_idx]:
        idx = areas[y_idx][x_idx].popleft()
        if idx in rest_edges:
            ct += 1
            remove_edge_candidate[idx] = (x_idx, y_idx)
            used_node.add(edges[idx][2])
            used_node.add(edges[idx][3])
            break
        else:
            continue

    if total + ct == M:
        last_check(output, remove_edge_candidate, day)
        break

    if ct == req_for_one_day[day]:
        # 連結のチェック
        uf = UnionFind(N)
        for idx in range(M):
            if idx in remove_edge_candidate:continue
            uf.union(edges[idx][2], edges[idx][3])
        if uf.size(0) == N: #連結なので工事する
            total += ct
            ct = 0
            for idx in remove_edge_candidate:
                output[idx] = day
                rest_edges.remove(idx)
            remove_edge_candidate = dict()
            day += 1
        else:
            reverse_edges = dict()
            for idx in remove_edge_candidate:
                idx_u, idx_v = edges[idx][2], edges[idx][3]
                if uf.same(idx_u, idx_v):continue
                uf.union(idx_u, idx_v)
                reverse_edges[idx] = remove_edge_candidate[idx]
                if uf.size(0) == N:
                    break
            
            # 残りのedgeで連結になるようなものが組めるか確かめる
            req_ct = len(reverse_edges)
            tmp_rest_edges = copy(rest_edges) # 確認用に残りの辺から候補を除外した集合を作成
            for idx in remove_edge_candidate.keys():
                tmp_rest_edges.remove(idx)
            for remove_list in itertools.combinations(tmp_rest_edges, req_ct):
                # 連結のチェック
                uf = UnionFind(N)
                for idx in range(M):
                    if (idx in remove_edge_candidate and idx not in reverse_edges) or idx in remove_list:continue
                    uf.union(edges[idx][2], edges[idx][3])
                    
                if uf.size(0) == N: #連結なので工事する
                    total += ct
                    ct = 0
                    for idx in remove_edge_candidate:
                        if idx in reverse_edges:continue
                        output[idx] = day
                        rest_edges.remove(idx)
                    for idx in remove_list:
                        output[idx] = day
                        rest_edges.remove(idx)
                    for idx, xy_idx in reverse_edges.items():
                        x_idx, y_idx = xy_idx
                        areas[y_idx][x_idx].append(idx)

                    remove_edge_candidate = dict()
                    day += 1
                    break
            else:#無理なので諦める
                total += ct
                ct = 0
                for idx in remove_edge_candidate:
                    output[idx] = day
                    rest_edges.remove(idx)
                remove_edge_candidate = dict()
                day += 1

    # if total == M : break

    if total + ct == M:
        last_check(output, remove_edge_candidate, day)
        break

# first+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# second+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    if D - day + 1 < len(areas[y_idx][x_idx]):
        # while areas[y_idx][x_idx]:
        #     idx = areas[y_idx][x_idx].popleft()
        #     if idx in rest_edges:
        #         ct += 1
        #         remove_edge_candidate[idx] = (x_idx, y_idx)
        #         break

        tmp = []
        while areas[y_idx][x_idx]:
            idx = areas[y_idx][x_idx].popleft()
            if idx not in rest_edges: continue
            if edges[idx][2] in used_node or edges[idx][3] in used_node:
                tmp.append(idx)
            else:
                ct += 1
                remove_edge_candidate[idx] = (x_idx, y_idx)
                used_node.add(edges[idx][2])
                used_node.add(edges[idx][3])
                for t in tmp:
                    areas[y_idx][x_idx].append(t)
                break

        if not areas[y_idx][x_idx]:
            for t in tmp:
                areas[y_idx][x_idx].append(t)

    if total + ct == M:
        last_check(output, remove_edge_candidate, day)
        break

    if ct == req_for_one_day[day]:
        # 連結のチェック
        uf = UnionFind(N)
        for idx in range(M):
            if idx in remove_edge_candidate:continue
            uf.union(edges[idx][2], edges[idx][3])
        if uf.size(0) == N: #連結なので工事する
            total += ct
            ct = 0
            for idx in remove_edge_candidate:
                output[idx] = day
                rest_edges.remove(idx)
            remove_edge_candidate = dict()
            day += 1
        else:
            reverse_edges = dict()
            for idx in remove_edge_candidate:
                idx_u, idx_v = edges[idx][2], edges[idx][3]
                if uf.same(idx_u, idx_v):continue
                uf.union(idx_u, idx_v)
                reverse_edges[idx] = remove_edge_candidate[idx]
                if uf.size(0) == N:
                    break
            
            # 残りのedgeで連結になるようなものが組めるか確かめる
            req_ct = len(reverse_edges)
            tmp_rest_edges = copy(rest_edges) # 確認用に残りの辺から候補を除外した集合を作成
            for idx in remove_edge_candidate.keys():
                tmp_rest_edges.remove(idx)
            for remove_list in itertools.combinations(tmp_rest_edges, req_ct):
                # 連結のチェック
                uf = UnionFind(N)
                for idx in range(M):
                    if (idx in remove_edge_candidate and idx not in reverse_edges) or idx in remove_list:continue
                    uf.union(edges[idx][2], edges[idx][3])
                    
                if uf.size(0) == N: #連結なので工事する
                    total += ct
                    ct = 0
                    for idx in remove_edge_candidate:
                        if idx in reverse_edges:continue
                        output[idx] = day
                        rest_edges.remove(idx)
                    for idx in remove_list:
                        output[idx] = day
                        rest_edges.remove(idx)
                    for idx, xy_idx in reverse_edges.items():
                        x_idx, y_idx = xy_idx
                        areas[y_idx][x_idx].append(idx)

                    remove_edge_candidate = dict()
                    day += 1
                    break
            else:#無理なので諦める
                total += ct
                ct = 0
                for idx in remove_edge_candidate:
                    output[idx] = day
                    rest_edges.remove(idx)
                remove_edge_candidate = dict()
                day += 1

    # if total == M : break

    if total + ct == M:
        last_check(output, remove_edge_candidate, day)
        break

# second+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# third+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # if D - day + 2 < len(areas[y_idx][x_idx]):
    #     while areas[y_idx][x_idx]:
    #         idx = areas[y_idx][x_idx].popleft()
    #         if idx in rest_edges:
    #             ct += 1
    #             remove_edge_candidate[idx] = (x_idx, y_idx)
    #             break

    # if total + ct == M:
    #     last_check(output, remove_edge_candidate, day)
    #     break

    # if ct == req_for_one_day[day]:
    #     # 連結のチェック
    #     uf = UnionFind(N)
    #     for idx in range(M):
    #         if idx in remove_edge_candidate:continue
    #         uf.union(edges[idx][2], edges[idx][3])
    #     if uf.size(0) == N: #連結なので工事する
    #         total += ct
    #         ct = 0
    #         for idx in remove_edge_candidate:
    #             output[idx] = day
    #             rest_edges.remove(idx)
    #         remove_edge_candidate = dict()
    #         day += 1
    #     else:
    #         reverse_edges = dict()
    #         for idx in remove_edge_candidate:
    #             idx_u, idx_v = edges[idx][2], edges[idx][3]
    #             if uf.same(idx_u, idx_v):continue
    #             uf.union(idx_u, idx_v)
    #             reverse_edges[idx] = remove_edge_candidate[idx]
    #             if uf.size(0) == N:
    #                 break
            
    #         # 残りのedgeで連結になるようなものが組めるか確かめる
    #         req_ct = len(reverse_edges)
    #         tmp_rest_edges = copy(rest_edges) # 確認用に残りの辺から候補を除外した集合を作成
    #         for idx in remove_edge_candidate.keys():
    #             tmp_rest_edges.remove(idx)
    #         for remove_list in itertools.combinations(tmp_rest_edges, req_ct):
    #             # 連結のチェック
    #             uf = UnionFind(N)
    #             for idx in range(M):
    #                 if (idx in remove_edge_candidate and idx not in reverse_edges) or idx in remove_list:continue
    #                 uf.union(edges[idx][2], edges[idx][3])
                    
    #             if uf.size(0) == N: #連結なので工事する
    #                 total += ct
    #                 ct = 0
    #                 for idx in remove_edge_candidate:
    #                     if idx in reverse_edges:continue
    #                     output[idx] = day
    #                     rest_edges.remove(idx)
    #                 for idx in remove_list:
    #                     output[idx] = day
    #                     rest_edges.remove(idx)
    #                 for idx, xy_idx in reverse_edges.items():
    #                     x_idx, y_idx = xy_idx
    #                     areas[y_idx][x_idx].append(idx)

    #                 remove_edge_candidate = dict()
    #                 day += 1
    #                 break
    #         else:#無理なので諦める
    #             total += ct
    #             ct = 0
    #             for idx in remove_edge_candidate:
    #                 output[idx] = day
    #                 rest_edges.remove(idx)
    #             remove_edge_candidate = dict()
    #             day += 1

    # # if total == M : break

    # if total + ct == M:
    #     last_check(output, remove_edge_candidate, day)
    #     break

# third+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # 次のブロックに移動
    x_idx += 1
    if x_idx == block_num:
        x_idx = 0
        y_idx += 1
        if y_idx == block_num:
            y_idx = 0
            
print(*output)


