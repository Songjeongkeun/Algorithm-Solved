from collections import deque


def solution(maps):
    row_count = len(maps)
    col_count = len(maps[0])
    start = lever = exit_point = None

    for row in range(row_count):
        for col in range(col_count):
            if maps[row][col] == "S":
                start = (row, col)
            elif maps[row][col] == "L":
                lever = (row, col)
            elif maps[row][col] == "E":
                exit_point = (row, col)

    def bfs(start_point, target_point):
        visited = [[False] * col_count for _ in range(row_count)]
        start_row, start_col = start_point
        visited[start_row][start_col] = True
        queue = deque([(start_row, start_col, 0)])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, distance = queue.popleft()

            if (row, col) == target_point:
                return distance

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                if not (0 <= next_row < row_count and 0 <= next_col < col_count):
                    continue

                if visited[next_row][next_col] or maps[next_row][next_col] == "X":
                    continue

                visited[next_row][next_col] = True
                queue.append((next_row, next_col, distance + 1))

        return -1

    start_to_lever = bfs(start, lever)
    lever_to_exit = bfs(lever, exit_point)

    if start_to_lever == -1 or lever_to_exit == -1:
        return -1

    return start_to_lever + lever_to_exit