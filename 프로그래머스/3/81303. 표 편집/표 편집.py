def solution(n, k, cmd):
    prev = [i - 1 for i in range(n)]
    nxt = [i + 1 for i in range(n)]
    nxt[n - 1] = -1

    cur = k
    deleted = []

    for command in cmd:
        if command[0] == "U":
            x = int(command[2:])

            for _ in range(x):
                cur = prev[cur]

        elif command[0] == "D":
            x = int(command[2:])

            for _ in range(x):
                cur = nxt[cur]

        elif command[0] == "C":
            deleted.append(cur)

            upper = prev[cur]
            lower = nxt[cur]

            if upper != -1:
                nxt[upper] = lower

            if lower != -1:
                prev[lower] = upper

            cur = lower if lower != -1 else upper

        else:
            restore = deleted.pop()

            upper = prev[restore]
            lower = nxt[restore]

            if upper != -1:
                nxt[upper] = restore

            if lower != -1:
                prev[lower] = restore

    answer = ["O"] * n

    for row in deleted:
        answer[row] = "X"

    return "".join(answer)