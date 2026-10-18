def solution(a, edges):
    if sum(a) != 0:
        return -1

    n = len(a)
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 원본 입력을 변경하지 않기 위해 복사한다.
    weights = a[:]

    # -2는 아직 방문하지 않은 상태를 의미한다.
    parent = [-2] * n
    parent[0] = -1

    order = []
    stack = [0]

    while stack:
        node = stack.pop()
        order.append(node)

        for next_node in graph[node]:
            if parent[next_node] != -2:
                continue

            parent[next_node] = node
            stack.append(next_node)

    answer = 0

    # 루트는 부모 간선이 없으므로 제외한다.
    for node in reversed(order[1:]):
        answer += abs(weights[node])
        weights[parent[node]] += weights[node]

    return answer