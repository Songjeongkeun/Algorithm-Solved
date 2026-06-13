def solution(cost, hint):
    n = len(cost)
    answer = float("inf")

    # 1번부터 n-1번 스테이지까지의 번들 구매 조합을 모두 확인한다.
    for mask in range(1 << (n - 1)):
        hint_count = [0] * n
        total = 0

        for stage in range(n):
            # 한 스테이지에서 사용할 수 있는 힌트권은 최대 n-1개다.
            used_hint = min(hint_count[stage], n - 1)
            total += cost[stage][used_hint]

            # 마지막 스테이지에서는 힌트 번들을 판매하지 않는다.
            if stage == n - 1:
                continue

            # 현재 스테이지의 힌트 번들을 구매하는 경우다.
            if mask & (1 << stage):
                total += hint[stage][0]

                for ticket in hint[stage][1:]:
                    ticket_index = ticket - 1

                    # n-1개를 초과한 힌트권은 사용할 수 없으므로
                    # 저장할 때부터 최대 n-1개로 제한해도 된다.
                    if hint_count[ticket_index] < n - 1:
                        hint_count[ticket_index] += 1

        answer = min(answer, total)

    return answer