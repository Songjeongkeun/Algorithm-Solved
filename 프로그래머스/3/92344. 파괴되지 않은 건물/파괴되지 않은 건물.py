def solution(board, skill):
    n = len(board)
    m = len(board[0])

    diff = [[0] * (m + 1) for _ in range(n + 1)]

    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree = -degree

        diff[r1][c1] += degree
        diff[r1][c2 + 1] -= degree
        diff[r2 + 1][c1] -= degree
        diff[r2 + 1][c2 + 1] += degree

    for i in range(n):
        for j in range(m):
            diff[i][j + 1] += diff[i][j]

    for j in range(m):
        for i in range(n):
            diff[i + 1][j] += diff[i][j]

    answer = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                answer += 1

    return answer