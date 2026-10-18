def solution(grid):
    n, m = len(grid), len(grid[0])

    # 방향: 오른쪽, 왼쪽, 아래, 위
    RIGHT, LEFT, DOWN, UP = 0, 1, 2, 3
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    # 현재 진행 방향으로 진입했을 때 놓을 수 있는 선로
    placeable = {
        RIGHT: [1, 3, 4, 7],
        LEFT:  [1, 3, 5, 6],
        DOWN:  [2, 3, 4, 5],
        UP:    [2, 3, 6, 7],
    }

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    visited[n - 1][m - 1] = 1

    answer = 0

    def is_valid_rail(rail, direction):
        if rail == 1:
            return direction in (RIGHT, LEFT)
        if rail == 2:
            return direction in (UP, DOWN)
        if rail == 3:
            return True
        if rail == 4:
            return direction in (RIGHT, DOWN)
        if rail == 5:
            return direction in (LEFT, DOWN)
        if rail == 6:
            return direction in (LEFT, UP)
        if rail == 7:
            return direction in (RIGHT, UP)
        return False

    def next_state(y, x, direction):
        rail = grid[y][x]

        if rail == 4:
            direction = LEFT if direction == DOWN else UP
        elif rail == 5:
            direction = RIGHT if direction == DOWN else UP
        elif rail == 6:
            direction = RIGHT if direction == UP else DOWN
        elif rail == 7:
            direction = LEFT if direction == UP else DOWN

        return y + dy[direction], x + dx[direction], direction

    def visited_all_rails():
        for y in range(n):
            for x in range(m):
                if 1 <= grid[y][x] <= 7:
                    if grid[y][x] == 3:
                        if visited[y][x] != 2:
                            return False
                    elif visited[y][x] < 1:
                        return False
        return True

    def dfs(y, x, direction):
        nonlocal answer

        if y < 0 or y >= n or x < 0 or x >= m:
            return

        if grid[y][x] == -1:
            return

        if y == n - 1 and x == m - 1:
            if is_valid_rail(grid[y][x], direction) and visited_all_rails():
                answer += 1
            return

        visited[y][x] += 1

        if grid[y][x] == 0:
            for rail in placeable[direction]:
                grid[y][x] = rail

                ny, nx, nd = next_state(y, x, direction)
                dfs(ny, nx, nd)

                grid[y][x] = 0
        else:
            if is_valid_rail(grid[y][x], direction):
                ny, nx, nd = next_state(y, x, direction)
                dfs(ny, nx, nd)

        visited[y][x] -= 1

    # 시작점 (0,0)의 1번 선로에서 오른쪽으로 출발
    dfs(0, 1, RIGHT)

    return answer