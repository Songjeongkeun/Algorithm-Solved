def solution(nodes, edges):
    node_count = len(nodes)

    # 실제 노드 번호를 0부터 시작하는 인덱스로 변환한다.
    index = {
        node: i
        for i, node in enumerate(nodes)
    }

    parent = list(range(node_count))
    union_size = [1] * node_count
    degree = [0] * node_count

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return

        if union_size[root_a] < union_size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        union_size[root_a] += union_size[root_b]

    # 각 노드의 차수를 계산하고 같은 트리의 노드를 합친다.
    for a, b in edges:
        a_index = index[a]
        b_index = index[b]

        degree[a_index] += 1
        degree[b_index] += 1

        union(a_index, b_index)

    tree_size = {}
    same_parity_count = {}

    for i, node in enumerate(nodes):
        root = find(i)

        tree_size[root] = tree_size.get(root, 0) + 1
        same_parity_count.setdefault(root, 0)

        # 노드 번호와 차수의 홀짝이 같은지 확인한다.
        if node % 2 == degree[i] % 2:
            same_parity_count[root] += 1

    odd_even_tree_count = 0
    reverse_tree_count = 0

    for root, size in tree_size.items():
        same_count = same_parity_count[root]
        different_count = size - same_count

        # 번호와 차수의 홀짝이 같은 노드가 유일한 경우
        if same_count == 1:
            odd_even_tree_count += 1

        # 번호와 차수의 홀짝이 다른 노드가 유일한 경우
        if different_count == 1:
            reverse_tree_count += 1

    return [odd_even_tree_count, reverse_tree_count]