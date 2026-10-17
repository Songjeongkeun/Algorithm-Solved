def solution(depth, money, excavate):
    n = len(depth)

    dp = [[0] * (n + 2) for _ in range(n + 2)]
    pick = [[0] * (n + 2) for _ in range(n + 2)]

    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1

            dp[left][right] = float('inf')

            for mid in range(left, right + 1):
                cost = depth[mid - 1] + max(
                    dp[left][mid - 1],
                    dp[mid + 1][right]
                )

                if cost < dp[left][right]:
                    dp[left][right] = cost
                    pick[left][right] = mid

    left, right = 1, n

    while left <= right:
        mid = pick[left][right]
        result = excavate(mid)

        if result == 0:
            return mid
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1