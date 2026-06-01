from collections import deque


def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    board = [["."] * (m + 2)]

    for row in storage:
        board.append(["."] + list(row) + ["."])

    board.append(["."] * (m + 2))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def use_forklift(target):
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        q = deque([(0, 0)])
        visited[0][0] = True
        remove_set = set()

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < n + 2 and 0 <= ny < m + 2):
                    continue

                if visited[nx][ny]:
                    continue

                if board[nx][ny] == ".":
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif board[nx][ny] == target:
                    remove_set.add((nx, ny))

        for x, y in remove_set:
            board[x][y] = "."

    def use_crane(target):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i][j] == target:
                    board[i][j] = "."

    for request in requests:
        target = request[0]

        if len(request) == 1:
            use_forklift(target)
        else:
            use_crane(target)

    answer = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != ".":
                answer += 1

    return answer