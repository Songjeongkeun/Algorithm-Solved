def solution(cap, n, deliveries, pickups):
    answer = 0

    d = 0  # 아직 처리해야 할 배달량
    p = 0  # 아직 처리해야 할 수거량

    # 가장 먼 집부터 확인
    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        # 현재 위치 i까지 와야 할 일이 남아있다면 왕복 필요
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2

    return answer