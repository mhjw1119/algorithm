from collections import deque

def bfs(start, goal) :
    count = deque([ start ])
    check = [-1] * 1000001
    check[start] = 0
    while count :
        now = count.popleft()
        if now == goal :
            return check[now]

        for next in [now +1, now -1, now *2] :
            if -1 < next  < 1000001 and check[next] == -1 :
                check[next] = check[now] + 1
                count.append(next)

N, K = map( int, input().split())
print(bfs(N, K))