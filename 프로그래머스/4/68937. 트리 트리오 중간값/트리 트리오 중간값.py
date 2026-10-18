from collections import deque


def solution(n, edges):
    graph = [[] for _ in range(n)]

    for left, right in edges:
        left -= 1
        right -= 1
        graph[left].append(right)
        graph[right].append(left)

    def bfs(start):
        distance = [-1] * n
        distance[start] = 0
        queue = deque([start])

        farthest_node = start
        max_distance = 0
        farthest_count = 1

        while queue:
            node = queue.popleft()

            for next_node in graph[node]:
                if distance[next_node] != -1:
                    continue

                distance[next_node] = distance[node] + 1
                queue.append(next_node)

                if distance[next_node] > max_distance:
                    max_distance = distance[next_node]
                    farthest_node = next_node
                    farthest_count = 1
                elif distance[next_node] == max_distance:
                    farthest_count += 1

        return farthest_node, max_distance, farthest_count

    # 임의의 정점에서 가장 먼 정점은 지름의 한 끝이다.
    diameter_end, _, _ = bfs(0)

    # 지름의 한 끝에서 지름 길이와 최장 거리 정점 개수를 구한다.
    other_end, diameter, farthest_count = bfs(diameter_end)

    if farthest_count >= 2:
        return diameter

    # 반대쪽 끝에서도 최장 거리 정점이 여러 개인지 확인한다.
    _, _, farthest_count = bfs(other_end)

    if farthest_count >= 2:
        return diameter

    return diameter - 1