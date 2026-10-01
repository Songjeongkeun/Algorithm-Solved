from itertools import product

def solution(clockHands):
    n = len(clockHands)
    answer = float("inf")

    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    def rotate(board, row, col, count):
        """(row, col)을 count번 조작한 결과를 보드에 반영한다."""
        for direction in range(5):
            nr = row + dr[direction]
            nc = col + dc[direction]

            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] = (board[nr][nc] + count) % 4

    # 첫 행의 모든 조작 조합을 시도한다.
    for first_row in product(range(4), repeat=n):
        board = [row[:] for row in clockHands]
        operation_count = sum(first_row)

        # 첫 행 조작을 적용한다.
        for col, count in enumerate(first_row):
            if count:
                rotate(board, 0, col, count)

        # 현재 행을 조작해 바로 위 행을 0으로 확정한다.
        for row in range(1, n):
            for col in range(n):
                count = (-board[row - 1][col]) % 4

                if count:
                    rotate(board, row, col, count)
                    operation_count += count

        # 마지막 행도 모두 0이면 유효한 해다.
        if all(clock == 0 for clock in board[-1]):
            answer = min(answer, operation_count)

    return answer