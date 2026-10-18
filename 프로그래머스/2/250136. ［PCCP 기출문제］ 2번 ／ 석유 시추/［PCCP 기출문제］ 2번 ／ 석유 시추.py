from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    oil_by_col = [0] * m

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(n):
        for col in range(m):
            if land[row][col] == 0 or visited[row][col]:
                continue

            queue = deque([(row, col)])
            visited[row][col] = True

            oil_size = 0
            columns = set()

            while queue:
                current_row, current_col = queue.popleft()

                oil_size += 1
                columns.add(current_col)

                for dr, dc in directions:
                    next_row = current_row + dr
                    next_col = current_col + dc

                    if not (0 <= next_row < n and 0 <= next_col < m):
                        continue

                    if visited[next_row][next_col]:
                        continue

                    if land[next_row][next_col] == 0:
                        continue

                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))

            for c in columns:
                oil_by_col[c] += oil_size

    return max(oil_by_col)