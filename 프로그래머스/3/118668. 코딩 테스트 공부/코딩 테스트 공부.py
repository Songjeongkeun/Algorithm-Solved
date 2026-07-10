def solution(alp, cop, problems):
    target_alp = max(problem[0] for problem in problems)
    target_cop = max(problem[1] for problem in problems)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    INF = float("inf")
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0

    for current_alp in range(alp, target_alp + 1):
        for current_cop in range(cop, target_cop + 1):
            current_time = dp[current_alp][current_cop]

            if current_time == INF:
                continue

            if current_alp < target_alp:
                dp[current_alp + 1][current_cop] = min(
                    dp[current_alp + 1][current_cop],
                    current_time + 1,
                )

            if current_cop < target_cop:
                dp[current_alp][current_cop + 1] = min(
                    dp[current_alp][current_cop + 1],
                    current_time + 1,
                )

            for req_alp, req_cop, reward_alp, reward_cop, cost in problems:
                if current_alp < req_alp or current_cop < req_cop:
                    continue

                next_alp = min(target_alp, current_alp + reward_alp)
                next_cop = min(target_cop, current_cop + reward_cop)

                dp[next_alp][next_cop] = min(
                    dp[next_alp][next_cop],
                    current_time + cost,
                )

    return dp[target_alp][target_cop]