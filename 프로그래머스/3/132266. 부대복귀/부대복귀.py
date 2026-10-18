from collections import deque


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]

    # 모든 길은 양방향이다.
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)

    # 각 지역에서 destination까지의 최단시간
    distance = [-1] * (n + 1)
    distance[destination] = 0

    queue = deque([destination])

    # 목적지에서 시작하는 BFS
    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            # 처음 방문한 경로가 최단 경로다.
            if distance[neighbor] != -1:
                continue

            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

    return [distance[source] for source in sources]