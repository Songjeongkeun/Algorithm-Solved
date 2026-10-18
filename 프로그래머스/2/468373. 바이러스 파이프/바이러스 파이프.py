def solution(n, infection, edges, k):
    # 타입별 인접 리스트
    graph = [[[] for _ in range(n)] for _ in range(3)]

    for x, y, pipe_type in edges:
        x -= 1
        y -= 1
        pipe_type -= 1

        graph[pipe_type][x].append(y)
        graph[pipe_type][y].append(x)

    # 각 타입의 연결 요소를 비트마스크로 저장
    components = [[] for _ in range(3)]

    for pipe_type in range(3):
        visited = [False] * n

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True
            component = 0

            while stack:
                node = stack.pop()
                component |= 1 << node

                for next_node in graph[pipe_type][node]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        stack.append(next_node)

            components[pipe_type].append(component)

    def spread(infected, pipe_type):
        result = infected

        for component in components[pipe_type]:
            # 감염된 노드가 하나라도 있는 연결 요소 전체를 감염시킨다.
            if infected & component:
                result |= component

        return result

    initial_infected = 1 << (infection - 1)
    states = {initial_infected}

    for _ in range(k):
        next_states = set()

        for infected in states:
            for pipe_type in range(3):
                next_states.add(spread(infected, pipe_type))

        states = next_states

    return max(infected.bit_count() for infected in states)