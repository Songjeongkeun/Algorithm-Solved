def solution(visible, hidden, k):
    n = len(visible)
    m = len(visible[0])

    # 더 작은 축을 비트마스크로 탐색하기 위해 필요한 경우 전치한다.
    if n <= m:
        v = visible
        h = hidden
        rows, cols = n, m
    else:
        v = [list(row) for row in zip(*visible)]
        h = [list(row) for row in zip(*hidden)]
        rows, cols = m, n

    need_exclude = (n % 2 == 0 and m % 2 == 0)
    answer = -10**30

    for mask in range(1 << rows):
        row_cost = -k * mask.bit_count()

        col_zero = [0] * cols
        col_one = [0] * cols
        col_best = [0] * cols

        for col in range(cols):
            score_zero = 0
            score_one = -k

            for row in range(rows):
                row_flipped = (mask >> row) & 1

                if row_flipped == 0:
                    score_zero += v[row][col]
                    score_one += h[row][col]
                else:
                    score_zero += h[row][col]
                    score_one += v[row][col]

            col_zero[col] = score_zero
            col_one[col] = score_one
            col_best[col] = max(score_zero, score_one)

        total = row_cost + sum(col_best)

        if not need_exclude:
            answer = max(answer, total)
            continue

        # n과 m이 모두 짝수라면 0-index 기준 홀수 색 칸 하나를 제외한다.
        for row in range(rows):
            row_flipped = (mask >> row) & 1

            for col in range(cols):
                if (row + col) % 2 == 0:
                    continue

                if row_flipped == 0:
                    value_when_col_zero = v[row][col]
                    value_when_col_one = h[row][col]
                else:
                    value_when_col_zero = h[row][col]
                    value_when_col_one = v[row][col]

                best_without_cell = max(
                    col_zero[col] - value_when_col_zero,
                    col_one[col] - value_when_col_one,
                )

                candidate = total - col_best[col] + best_without_cell
                answer = max(answer, candidate)

    return answer