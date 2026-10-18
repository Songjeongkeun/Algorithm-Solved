def solution(n, s, a, b, fares):
    INF = float("inf")

    distance = [
        [INF] * (n + 1)
        for _ in range(n + 1)
    ]

    # 자기 자신으로 이동하는 비용은 0이다.
    for point in range(1, n + 1):
        distance[point][point] = 0

    # 택시 경로는 양방향이다.
    for start, end, fare in fares:
        distance[start][end] = fare
        distance[end][start] = fare

    # 모든 지점 쌍의 최단 거리를 계산한다.
    for middle in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                distance[start][end] = min(
                    distance[start][end],
                    distance[start][middle]
                    + distance[middle][end]
                )

    answer = INF

    # 모든 지점을 합승 종료 지점으로 확인한다.
    for split in range(1, n + 1):
        total_fare = (
            distance[s][split]
            + distance[split][a]
            + distance[split][b]
        )

        answer = min(answer, total_fare)

    return answer