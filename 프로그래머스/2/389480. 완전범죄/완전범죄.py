def solution(info, n, m):
    INF = 10**9

    dp = [INF] * m
    dp[0] = 0

    for a_trace, b_trace in info:
        next_dp = [INF] * m

        for b in range(m):
            if dp[b] == INF:
                continue

            new_a = dp[b] + a_trace
            if new_a < n:
                next_dp[b] = min(next_dp[b], new_a)

            new_b = b + b_trace
            if new_b < m:
                next_dp[new_b] = min(next_dp[new_b], dp[b])

        dp = next_dp

    answer = min(dp)
    return answer if answer != INF else -1