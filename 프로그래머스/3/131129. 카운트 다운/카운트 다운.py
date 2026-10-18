def solution(target):
    throws = [(50, 1)]

    for number in range(1, 21):
        throws.append((number, 1))       # 싱글
        throws.append((number * 2, 0))   # 더블
        throws.append((number * 3, 0))   # 트리플

    infinity = target + 1
    dp = [(infinity, -1) for _ in range(target + 1)]
    dp[0] = (0, 0)

    for score in range(1, target + 1):
        for points, single_or_bull in throws:
            if score < points:
                continue

            previous_darts, previous_singles = dp[score - points]

            if previous_darts == infinity:
                continue

            candidate_darts = previous_darts + 1
            candidate_singles = previous_singles + single_or_bull
            current_darts, current_singles = dp[score]

            if (
                candidate_darts < current_darts
                or (
                    candidate_darts == current_darts
                    and candidate_singles > current_singles
                )
            ):
                dp[score] = (candidate_darts, candidate_singles)

    return list(dp[target])