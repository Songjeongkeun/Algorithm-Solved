def solution(info, edges):
    n = len(info)
    children = [[] for _ in range(n)]

    for parent, child in edges:
        children[parent].append(child)

    answer = 0

    def dfs(sheep, wolf, candidates):
        nonlocal answer

        answer = max(answer, sheep)

        for node in candidates:
            next_sheep = sheep
            next_wolf = wolf

            if info[node] == 0:
                next_sheep += 1
            else:
                next_wolf += 1

            if next_wolf >= next_sheep:
                continue

            next_candidates = candidates[:]
            next_candidates.remove(node)
            next_candidates.extend(children[node])

            dfs(next_sheep, next_wolf, next_candidates)

    dfs(1, 0, children[0])

    return answer