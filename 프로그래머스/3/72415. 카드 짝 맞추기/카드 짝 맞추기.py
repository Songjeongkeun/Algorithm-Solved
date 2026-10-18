from collections import deque
from functools import lru_cache


def solution(board, r, c):
    positions = {}

    for row in range(4):
        for col in range(4):
            value = board[row][col]

            if value != 0:
                positions.setdefault(value, []).append((row, col))

    card_numbers = list(positions)
    full_mask = sum(1 << number for number in card_numbers)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def has_card(row, col, removed_mask):
        value = board[row][col]
        return value != 0 and (removed_mask & (1 << value)) == 0

    def ctrl_move(row, col, dr, dc, removed_mask):
        while True:
            next_row = row + dr
            next_col = col + dc

            # 해당 방향의 끝 칸에서 멈춘다.
            if not (0 <= next_row < 4 and 0 <= next_col < 4):
                return row, col

            row, col = next_row, next_col

            if has_card(row, col, removed_mask):
                return row, col

    def move_distance(start_row, start_col, target_row, target_col, removed_mask):
        visited = [[False] * 4 for _ in range(4)]
        visited[start_row][start_col] = True
        queue = deque([(start_row, start_col, 0)])

        while queue:
            row, col, distance = queue.popleft()

            if (row, col) == (target_row, target_col):
                return distance

            for dr, dc in directions:
                # 일반 방향키 이동
                next_row = row + dr
                next_col = col + dc

                if (
                    0 <= next_row < 4
                    and 0 <= next_col < 4
                    and not visited[next_row][next_col]
                ):
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col, distance + 1))

                # Ctrl + 방향키 이동
                next_row, next_col = ctrl_move(
                    row,
                    col,
                    dr,
                    dc,
                    removed_mask
                )

                if not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col, distance + 1))

    @lru_cache(None)
    def dfs(removed_mask, row, col):
        if removed_mask == full_mask:
            return 0

        minimum = float("inf")

        for number in card_numbers:
            bit = 1 << number

            if removed_mask & bit:
                continue

            first, second = positions[number]
            next_mask = removed_mask | bit

            # first 카드를 먼저 선택하는 경우
            first_to_second = (
                move_distance(row, col, *first, removed_mask)
                + move_distance(*first, *second, removed_mask)
                + 2
                + dfs(next_mask, *second)
            )

            # second 카드를 먼저 선택하는 경우
            second_to_first = (
                move_distance(row, col, *second, removed_mask)
                + move_distance(*second, *first, removed_mask)
                + 2
                + dfs(next_mask, *first)
            )

            minimum = min(minimum, first_to_second, second_to_first)

        return minimum

    return dfs(0, r, c)