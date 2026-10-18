def solution(board):
    o_count = sum(row.count("O") for row in board)
    x_count = sum(row.count("X") for row in board)

    # O가 선공이므로 O와 X의 개수는 같거나 O가 하나 더 많아야 한다.
    if o_count < x_count or o_count > x_count + 1:
        return 0

    win_lines = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    ]

    def has_won(mark):
        for line in win_lines:
            if all(board[r][c] == mark for r, c in line):
                return True
        return False

    o_won = has_won("O")
    x_won = has_won("X")

    # 승리한 순간 게임이 끝나므로 둘 다 승리할 수 없다.
    if o_won and x_won:
        return 0

    # O가 이겼다면 O가 마지막 수를 둔 상태여야 한다.
    if o_won and o_count != x_count + 1:
        return 0

    # X가 이겼다면 X가 마지막 수를 둔 상태여야 한다.
    if x_won and o_count != x_count:
        return 0

    return 1