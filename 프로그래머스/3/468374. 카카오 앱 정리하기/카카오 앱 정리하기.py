from collections import deque


def solution(board, commands):
    n, m = len(board), len(board[0])

    # 오른쪽, 아래쪽, 왼쪽, 위쪽
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for target, arrow in commands:
        dr, dc = dirs[arrow - 1]

        pending = deque([target])

        while pending:
            moving = set(pending)
            q = deque(pending)
            pending.clear()

            # BFS로 연쇄 이동할 앱 탐색
            while q:
                cur = q.popleft()

                for r in range(n):
                    for c in range(m):
                        if board[r][c] != cur:
                            continue

                        nr = (r + dr) % n
                        nc = (c + dc) % m

                        other = board[nr][nc]

                        if other and other not in moving:
                            moving.add(other)
                            q.append(other)

            # 이동 대상 앱을 동시에 이동
            new_board = [[0] * m for _ in range(n)]

            for r in range(n):
                for c in range(m):
                    app = board[r][c]

                    if app == 0:
                        continue

                    if app in moving:
                        nr = (r + dr) % n
                        nc = (c + dc) % m
                    else:
                        nr, nc = r, c

                    new_board[nr][nc] = app

            board = new_board

            # 경계에 걸친 앱 확인
            wrapped = set()

            if dc != 0:
                for r in range(n):
                    app = board[r][0]

                    if (
                        app != 0
                        and app == board[r][m - 1]
                        and any(
                            board[r][c] != app
                            for c in range(1, m - 1)
                        )
                    ):
                        wrapped.add(app)

            else:
                for c in range(m):
                    app = board[0][c]

                    if (
                        app != 0
                        and app == board[n - 1][c]
                        and any(
                            board[r][c] != app
                            for r in range(1, n - 1)
                        )
                    ):
                        wrapped.add(app)

            pending.extend(wrapped)

    return board