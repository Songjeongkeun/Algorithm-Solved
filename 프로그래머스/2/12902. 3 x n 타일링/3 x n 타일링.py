def solution(n):
    MOD = 1_000_000_007

    # 3 × 홀수 크기의 바닥은 채울 수 없다.
    if n % 2 == 1:
        return 0

    # dp[0]과 dp[2]
    dp_zero = 1
    dp_two = 3

    if n == 2:
        return dp_two

    # dp[i] = 4 * dp[i - 2] - dp[i - 4]
    for width in range(4, n + 1, 2):
        current = (
            4 * dp_two - dp_zero
        ) % MOD

        dp_zero, dp_two = dp_two, current

    return dp_two
