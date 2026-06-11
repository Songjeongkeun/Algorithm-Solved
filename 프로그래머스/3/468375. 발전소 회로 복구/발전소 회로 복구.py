from collections import deque


def solution(h, grid, panels, seqs):
    n = len(grid)
    m = len(grid[0])
    k = len(panels)

    elevator_row = -1
    elevator_col = -1

    for row in range(n):
        for col in range(m):
            if grid[row][col] == "@":
                elevator_row = row
                elevator_col = col

    floors = []
    positions = []

    for floor, row, col in panels:
        floors.append(floor)
        positions.append((row - 1, col - 1))

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    panel_distance = [[0] * k for _ in range(k)]
    elevator_distance = [0] * k

    for start in range(k):
        start_row, start_col = positions[start]

        distance = [[-1] * m for _ in range(n)]
        distance[start_row][start_col] = 0

        queue = deque([(start_row, start_col)])

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                if not (0 <= next_row < n and 0 <= next_col < m):
                    continue

                if grid[next_row][next_col] == "#":
                    continue

                if distance[next_row][next_col] != -1:
                    continue

                distance[next_row][next_col] = distance[row][col] + 1
                queue.append((next_row, next_col))

        elevator_distance[start] = distance[elevator_row][elevator_col]

        for target in range(k):
            target_row, target_col = positions[target]
            panel_distance[start][target] = distance[target_row][target_col]

    move_time = [[0] * k for _ in range(k)]

    for start in range(k):
        for target in range(k):
            if floors[start] == floors[target]:
                move_time[start][target] = panel_distance[start][target]
            else:
                move_time[start][target] = (
                    elevator_distance[start]
                    + abs(floors[start] - floors[target])
                    + elevator_distance[target]
                )

    required = [0] * k

    for a, b in seqs:
        required[b - 1] |= 1 << (a - 1)

    state_count = 1 << k
    infinity = 10**18
    dp = [[infinity] * k for _ in range(state_count)]

    # 기술자는 1번 패널의 위치에서 출발하지만,
    # 아직 어떤 패널도 활성화하지 않은 상태다.
    dp[0][0] = 0

    for mask in range(state_count):
        for last in range(k):
            current_time = dp[mask][last]

            if current_time == infinity:
                continue

            for next_panel in range(k):
                bit = 1 << next_panel

                if mask & bit:
                    continue

                if required[next_panel] & mask != required[next_panel]:
                    continue

                next_mask = mask | bit
                next_time = current_time + move_time[last][next_panel]

                if next_time < dp[next_mask][next_panel]:
                    dp[next_mask][next_panel] = next_time

    full_mask = state_count - 1
    return min(dp[full_mask])