def solution(nodeinfo):
    n = len(nodeinfo)

    # (x 좌표, y 좌표, 노드 번호) 형태로 저장 후 x 기준 정렬
    nodes = sorted(
        (x, y, index + 1)
        for index, (x, y) in enumerate(nodeinfo)
    )

    left = [0] * (n + 1)
    right = [0] * (n + 1)
    stack = []

    # x 오름차순 + y 내림차순 단조 스택으로 카테시안 트리 구성
    for x, y, node_id in nodes:
        last = 0

        # 현재 노드보다 y가 작은 노드는 현재 노드의 왼쪽 서브트리 후보
        while stack and stack[-1][1] < y:
            last = stack.pop()[2]

        # 가장 마지막에 빠진 노드가 현재 노드의 왼쪽 자식
        if last:
            left[node_id] = last

        # 스택 top은 현재 노드의 부모가 되고, 현재 노드는 오른쪽 자식
        if stack:
            parent_id = stack[-1][2]
            right[parent_id] = node_id

        stack.append((x, y, node_id))

    # 스택의 가장 아래 노드는 전체 트리의 루트
    root = stack[0][2]

    # 전위 순회: 루트 -> 왼쪽 -> 오른쪽
    preorder = []
    traversal_stack = [root]

    while traversal_stack:
        node_id = traversal_stack.pop()
        preorder.append(node_id)

        # 스택은 나중에 넣은 노드가 먼저 나오므로 오른쪽을 먼저 넣는다.
        if right[node_id]:
            traversal_stack.append(right[node_id])
        if left[node_id]:
            traversal_stack.append(left[node_id])

    # 후위 순회: 왼쪽 -> 오른쪽 -> 루트
    # 루트 -> 오른쪽 -> 왼쪽 순서로 모은 뒤 뒤집는다.
    reverse_postorder = []
    traversal_stack = [root]

    while traversal_stack:
        node_id = traversal_stack.pop()
        reverse_postorder.append(node_id)

        if left[node_id]:
            traversal_stack.append(left[node_id])
        if right[node_id]:
            traversal_stack.append(right[node_id])

    postorder = reverse_postorder[::-1]

    return [preorder, postorder]