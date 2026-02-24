import sys


def solve():
    # 입력 속도 향상을 위해 sys.stdin.read 사용
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    stack = []  # (탑의 인덱스, 탑의 높이)를 저장할 스택
    answer = []  # 결과를 저장할 리스트

    for i in range(N):
        while stack:
            # 스택의 Top에 있는 탑이 현재 탑보다 높다면? 신호를 수신함!
            if stack[-1][1] > arr[i]:
                answer.append(stack[-1][0] + 1)  # 1-based index이므로 +1
                break
            # 스택의 Top이 현재 탑보다 낮다면? 필요 없으니 제거
            else:
                stack.pop()

        # 스택이 비어있다면 왼쪽에서 수신할 탑이 없다는 뜻
        if not stack:
            answer.append(0)

        # 현재 탑을 스택에 추가 (다음 탑들을 위해)
        stack.append((i, arr[i]))

    print(*(answer))


solve()