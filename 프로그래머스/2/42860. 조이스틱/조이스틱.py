def solution(name):
    n = len(name)

    answer = 0

    for char in name:
        up = ord(char) - ord("A")
        down = ord("Z") - ord(char) + 1
        answer += min(up, down)

    move = n - 1

    for i in range(n):
        next_index = i + 1

        while next_index < n and name[next_index] == "A":
            next_index += 1

        move = min(move, 2 * i + n - next_index)
        move = min(move, i + 2 * (n - next_index))

    return answer + move