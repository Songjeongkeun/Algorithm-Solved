def solution(matrix_sizes):
    matrix_count = len(matrix_sizes)

    # dp[start][end]:
    # start번 행렬부터 end번 행렬까지 곱하는 최소 비용
    dp = [
        [0] * matrix_count
        for _ in range(matrix_count)
    ]

    # 짧은 구간부터 최소 비용을 계산한다.
    for length in range(2, matrix_count + 1):
        for start in range(matrix_count - length + 1):
            end = start + length - 1
            dp[start][end] = float("inf")

            # start ~ end 구간을 mid 기준으로 나눈다.
            for mid in range(start, end):
                multiply_cost = (
                    matrix_sizes[start][0]
                    * matrix_sizes[mid][1]
                    * matrix_sizes[end][1]
                )

                cost = (
                    dp[start][mid]
                    + dp[mid + 1][end]
                    + multiply_cost
                )

                dp[start][end] = min(
                    dp[start][end],
                    cost
                )

    return dp[0][matrix_count - 1]