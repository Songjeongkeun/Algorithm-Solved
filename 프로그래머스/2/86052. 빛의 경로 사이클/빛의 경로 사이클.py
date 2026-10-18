def solution(grid):
    row_count = len(grid)
    col_count = len(grid[0])

    # visited[row][col][direction]
    visited = [
        [[False] * 4 for _ in range(col_count)]
        for _ in range(row_count)
    ]

    dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
    dc = [0, 1, 0, -1]
    cycles = []

    for start_row in range(row_count):
        for start_col in range(col_count):
            for start_direction in range(4):
                if visited[start_row][start_col][start_direction]:
                    continue

                row = start_row
                col = start_col
                direction = start_direction
                length = 0

                # 시작 상태로 되돌아올 때까지 한 경로를 추적한다.
                while not visited[row][col][direction]:
                    visited[row][col][direction] = True
                    length += 1

                    if grid[row][col] == "L":
                        direction = (direction - 1) % 4
                    elif grid[row][col] == "R":
                        direction = (direction + 1) % 4

                    row = (row + dr[direction]) % row_count
                    col = (col + dc[direction]) % col_count

                cycles.append(length)

    return sorted(cycles)