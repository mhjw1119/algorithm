# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

import queue


def dfs( start):
    global dfs_result
    check_dfs[start - 1] = 1
    dfs_result.append(start)


    for nx_dfs in arr[start-1] :
        # if len(dfs_result) == N :
        #     return
        if check_dfs[nx_dfs] != 1 :
            dfs(nx_dfs+1)
            # check_dfs[start -1] = 0

def bfs(start_bfs):
    global bfs_result
    bfs_list = [start_bfs-1]
    check_bfs[start_bfs-1] = 1
    while bfs_list :
        start = bfs_list.pop(0)
        bfs_result.append(start+1)
        for nx_bfs in arr[start] :
            if check_bfs[nx_bfs] != 1 :
                check_bfs[nx_bfs] = 1
                bfs_list.append(nx_bfs)


N, M, V = map(int, input().split())
arr = [[] for _ in range(N) ]
check_dfs = [0] * N
check_bfs = [0] * N
dfs_result = []
bfs_result = []

check_dfs[V-1] = 1

for i in range(M):
    now, nx = map(int, input().split())
    arr[now-1].append(nx-1)
    arr[nx-1].append(now-1)
for i in range(N):
    arr[i] = sorted(arr[i])
bfs(V)
dfs(V)
print(* dfs_result)
print(* bfs_result)
