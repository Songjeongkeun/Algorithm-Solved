from collections import deque

def solution(board):
    n = len(board)

    # 상, 우, 하, 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # cost[x][y][dir] = (x, y)에 dir 방향으로 도착했을 때 최소 비용
    cost = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    q = deque()

    # 시작점에서는 방향이 없으므로 4방향 모두 0으로 시작
    for d in range(4):
        cost[0][0][d] = 0
        q.append((0, 0, d, 0))

    while q:
        x, y, direction, current_cost = q.popleft()

        for nd in range(4):
            nx = x + dx[nd]
            ny = y + dy[nd]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[nx][ny] == 1:
                continue

            # 같은 방향이면 직선 도로
            if direction == nd:
                next_cost = current_cost + 100
            # 방향이 바뀌면 코너 + 직선 도로
            else:
                next_cost = current_cost + 600

            if cost[nx][ny][nd] > next_cost:
                cost[nx][ny][nd] = next_cost
                q.append((nx, ny, nd, next_cost))

    return min(cost[n - 1][n - 1])