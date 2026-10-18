import heapq


def solution(n, k, enemy):
    invincible_rounds = []

    for round_index, enemy_count in enumerate(enemy):
        # 현재까지는 이 라운드에도 무적권을 쓴다고 가정한다.
        heapq.heappush(invincible_rounds, enemy_count)

        # 무적권 수를 넘으면 가장 작은 공격은 병사로 막는다.
        if len(invincible_rounds) > k:
            n -= heapq.heappop(invincible_rounds)

        if n < 0:
            return round_index

    return len(enemy)