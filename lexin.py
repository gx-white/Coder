from collections import defaultdict, deque
import sys

n = int(input())
time_list = [int(input()) for _ in range(n)]
m = int(input())
in_degree = [0 for _ in range(n)]
out_depend_dic = defaultdict(list)
for _ in range(m):
    values = map(int, sys.stdin.readline().strip().split())
    s, q = list(values)
    in_degree[q] += 1
    out_depend_dic[s].append(q)

queue = deque()
for key in range(n):
    if in_degree[key] == 0:
        queue.append([key, time_list[key]])
max_fee = 0
while len(queue) > 0:
    k, f = queue.popleft()
    max_fee = max(max_fee, f)
    for next_k in out_depend_dic[k]:
        queue.append([next_k, f+time_list[next_k]])
print(max_fee)