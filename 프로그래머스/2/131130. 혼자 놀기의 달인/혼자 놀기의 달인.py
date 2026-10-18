def solution(cards):
    box_count = len(cards)
    visited = [False] * box_count
    group_sizes = []

    # 방문하지 않은 상자에서 새로운 그룹을 찾는다.
    for start in range(box_count):
        if visited[start]:
            continue

        current = start
        group_size = 0

        # 카드 번호가 가리키는 다음 상자를 따라간다.
        while not visited[current]:
            visited[current] = True
            group_size += 1
            current = cards[current] - 1

        group_sizes.append(group_size)

    group_sizes.sort(reverse=True)

    # 전체 상자가 하나의 그룹이면 두 번째 그룹을 만들 수 없다.
    if len(group_sizes) < 2:
        return 0

    return group_sizes[0] * group_sizes[1]