def solution(maze):
    n = len(maze)
    m = len(maze[0])

    red_start = blue_start = None
    red_goal = blue_goal = None

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_goal = (i, j)
            elif maze[i][j] == 4:
                blue_goal = (i, j)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = float("inf")

    def cell_bit(x, y):
        return 1 << (x * m + y)

    def get_next_positions(x, y, visited, goal):
        if (x, y) == goal:
            return [(x, y)]

        positions = []

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 5:
                continue

            bit = cell_bit(nx, ny)

            if visited & bit:
                continue

            positions.append((nx, ny))

        return positions

    def dfs(red, blue, red_visited, blue_visited, turn):
        nonlocal answer

        if turn >= answer:
            return

        if red == red_goal and blue == blue_goal:
            answer = turn
            return

        red_next_positions = get_next_positions(
            red[0],
            red[1],
            red_visited,
            red_goal,
        )

        blue_next_positions = get_next_positions(
            blue[0],
            blue[1],
            blue_visited,
            blue_goal,
        )

        for next_red in red_next_positions:
            for next_blue in blue_next_positions:
                if next_red == next_blue:
                    continue

                if next_red == blue and next_blue == red:
                    continue

                next_red_visited = red_visited | cell_bit(next_red[0], next_red[1])
                next_blue_visited = blue_visited | cell_bit(next_blue[0], next_blue[1])

                dfs(
                    next_red,
                    next_blue,
                    next_red_visited,
                    next_blue_visited,
                    turn + 1,
                )

    initial_red_visited = cell_bit(red_start[0], red_start[1])
    initial_blue_visited = cell_bit(blue_start[0], blue_start[1])

    dfs(
        red_start,
        blue_start,
        initial_red_visited,
        initial_blue_visited,
        0,
    )

    if answer == float("inf"):
        return 0

    return answer