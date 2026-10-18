def solution(key, lock):
    def rotate(matrix):
        return [list(row) for row in zip(*matrix[::-1])]

    def is_unlocked(board):
        for row in range(n, 2 * n):
            for col in range(n, 2 * n):
                if board[row][col] != 1:
                    return False

        return True

    n = len(lock)
    m = len(key)

    # 열쇠가 자물쇠 바깥에 있는 경우까지 처리하기 위한 확장 보드
    board = [[0] * (3 * n) for _ in range(3 * n)]

    # 확장 보드의 중앙에 자물쇠 배치
    for row in range(n):
        for col in range(n):
            board[row + n][col + n] = lock[row][col]

    for _ in range(4):
        # key의 시작 위치를 (0, 0)부터 (2N - 1, 2N - 1)까지 이동한다.
        for start_row in range(2 * n):
            for start_col in range(2 * n):
                # 열쇠를 보드에 더한다.
                for row in range(m):
                    for col in range(m):
                        board[start_row + row][start_col + col] += key[row][col]

                if is_unlocked(board):
                    return True

                # 다음 위치를 검사할 수 있도록 열쇠를 다시 뺀다.
                for row in range(m):
                    for col in range(m):
                        board[start_row + row][start_col + col] -= key[row][col]

        key = rotate(key)

    return False
