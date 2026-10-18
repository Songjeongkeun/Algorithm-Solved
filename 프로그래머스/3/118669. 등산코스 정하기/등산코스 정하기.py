from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    for a, b, weight in paths:
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    summit_set = set(summits)
    infinity = float("inf")

    # intensity[node] = 출입구 중 한 곳에서 node까지의 최소 intensity
    intensity = [infinity] * (n + 1)
    heap = []

    # 모든 출입구를 동시에 시작점으로 사용한다.
    for gate in gates:
        intensity[gate] = 0
        heappush(heap, (0, gate))

    while heap:
        current_intensity, node = heappop(heap)

        # 이미 더 좋은 경로가 처리된 상태라면 건너뛴다.
        if current_intensity > intensity[node]:
            continue

        # 산봉우리는 목적지이므로 다른 지점으로 이동하지 않는다.
        if node in summit_set:
            continue

        for next_node, weight in graph[node]:
            next_intensity = max(current_intensity, weight)

            if next_intensity < intensity[next_node]:
                intensity[next_node] = next_intensity
                heappush(heap, (next_intensity, next_node))

    answer_summit = -1
    answer_intensity = infinity

    for summit in sorted(summits):
        if intensity[summit] < answer_intensity:
            answer_summit = summit
            answer_intensity = intensity[summit]

    return [answer_summit, answer_intensity]