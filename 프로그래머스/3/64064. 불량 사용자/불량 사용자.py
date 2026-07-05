def solution(user_id, banned_id):
    result = set()

    def is_match(user, banned):
        if len(user) != len(banned):
            return False

        for u, b in zip(user, banned):
            if b == "*":
                continue

            if u != b:
                return False

        return True

    def dfs(index, selected):
        if index == len(banned_id):
            result.add(frozenset(selected))
            return

        banned = banned_id[index]

        for user in user_id:
            if user in selected:
                continue

            if not is_match(user, banned):
                continue

            selected.add(user)
            dfs(index + 1, selected)
            selected.remove(user)

    dfs(0, set())

    return len(result)