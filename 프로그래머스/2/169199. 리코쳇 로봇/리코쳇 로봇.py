from collections import deque


def solution(board):
    row_count = len(board)
    col_count = len(board[0])
    start = None
    goal = None

    for row in range(row_count):
        for col in range(col_count):
            if board[row][col] == "R":
                start = (row, col)
            elif board[row][col] == "G":
                goal = (row, col)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def slide(row, col, dr, dc):
        while True:
            next_row = row + dr
            next_col = col + dc

            if (
                next_row < 0
                or next_row >= row_count
                or next_col < 0
                or next_col >= col_count
                or board[next_row][next_col] == "D"
            ):
                return row, col

            row, col = next_row, next_col

    visited = [[False] * col_count for _ in range(row_count)]
    start_row, start_col = start
    visited[start_row][start_col] = True
    queue = deque([(start_row, start_col, 0)])

    while queue:
        row, col, move_count = queue.popleft()

        if (row, col) == goal:
            return move_count

        for dr, dc in directions:
            next_row, next_col = slide(row, col, dr, dc)

            # 이미 경계 또는 장애물에 붙어 있어 움직이지 못한 경우
            if (next_row, next_col) == (row, col):
                continue

            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col, move_count + 1))

    return -1