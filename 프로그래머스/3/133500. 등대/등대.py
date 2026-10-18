def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]

    for lighthouse_a, lighthouse_b in lighthouse:
        graph[lighthouse_a].append(lighthouse_b)
        graph[lighthouse_b].append(lighthouse_a)

    # 1번 등대를 루트로 삼아 부모와 방문 순서를 기록한다.
    parent = [0] * (n + 1)
    parent[1] = -1

    order = []
    stack = [1]

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor == parent[node]:
                continue

            parent[neighbor] = node
            stack.append(neighbor)

    # dp[node][0]: node를 끈 경우
    # dp[node][1]: node를 켠 경우
    dp = [[0, 1] for _ in range(n + 1)]

    # 자식의 값을 먼저 계산하기 위해 방문 순서를 뒤집는다.
    for node in reversed(order):
        for child in graph[node]:
            if parent[child] != node:
                continue

            # 현재 등대를 끄면 자식 등대는 반드시 켜야 한다.
            dp[node][0] += dp[child][1]

            # 현재 등대를 켜면 자식 등대는 켜거나 끌 수 있다.
            dp[node][1] += min(
                dp[child][0],
                dp[child][1]
            )

    return min(dp[1][0], dp[1][1])