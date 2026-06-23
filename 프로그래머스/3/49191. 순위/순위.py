def solution(n, results):
    win = [
        [False] * (n + 1)
        for _ in range(n + 1)
    ]

    for winner, loser in results:
        win[winner][loser] = True

    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            if not win[start][mid]:
                continue

            for end in range(1, n + 1):
                if win[mid][end]:
                    win[start][end] = True

    answer = 0

    for player in range(1, n + 1):
        known_count = 0

        for other in range(1, n + 1):
            if player == other:
                continue

            if win[player][other] or win[other][player]:
                known_count += 1

        if known_count == n - 1:
            answer += 1

    return answer
