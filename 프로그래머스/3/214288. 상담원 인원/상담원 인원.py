import heapq


def solution(k, n, reqs):
    by_type = [[] for _ in range(k + 1)]

    for start, duration, consult_type in reqs:
        by_type[consult_type].append((start, duration))

    wait = [[0] * (n + 1) for _ in range(k + 1)]

    for consult_type in range(1, k + 1):
        requests = by_type[consult_type]

        for mentor_count in range(1, n + 1):
            heap = [0] * mentor_count
            heapq.heapify(heap)

            total_wait = 0

            for start, duration in requests:
                end_time = heapq.heappop(heap)

                if end_time <= start:
                    heapq.heappush(heap, start + duration)
                else:
                    total_wait += end_time - start
                    heapq.heappush(heap, end_time + duration)

            wait[consult_type][mentor_count] = total_wait

    answer = float("inf")

    def dfs(consult_type, remain, total):
        nonlocal answer

        if total >= answer:
            return

        if consult_type == k:
            answer = min(answer, total + wait[consult_type][remain])
            return

        # 남은 유형마다 최소 1명씩은 배정해야 한다.
        max_count = remain - (k - consult_type)

        for mentor_count in range(1, max_count + 1):
            dfs(
                consult_type + 1,
                remain - mentor_count,
                total + wait[consult_type][mentor_count],
            )

    dfs(1, n, 0)

    return answer