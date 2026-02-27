N = int(input())
arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = int(input())
visted = [False] * (N+1)
visted_list = []
result = []
def dfs(now, start):
    visted[now] = True
    next_node = arr[now]
    if visted[next_node] == False:
        dfs(next_node, start)

    elif visted[next_node] and next_node == start:
        result.append(start)



for i in range(1,N+1):
    visted = [False] * (N + 1)
    dfs(i, i)
print(len(result))
for j in result:
    print(j)
