def solution(message, spoiler_ranges):
    n = len(message)

    words = []
    i = 0
    while i < n:
        if message[i] == " ":
            i += 1
            continue

        start = i
        while i < n and message[i] != " ":
            i += 1
        end = i - 1
        words.append((start, end, message[start:i]))

    m = len(spoiler_ranges)
    reveal_at = [[] for _ in range(m)]

    normal_words = set()

    r = 0

    for start, end, word in words:
        while r < m and spoiler_ranges[r][1] < start:
            r += 1

        temp = r
        last_overlap = -1

        while temp < m and spoiler_ranges[temp][0] <= end:
            s, e = spoiler_ranges[temp]

            if not (e < start or end < s):
                last_overlap = temp

            temp += 1

        if last_overlap == -1:
            normal_words.add(word)
        else:
            reveal_at[last_overlap].append((start, word))

    important_count = 0

    revealed_spoiler_words = set()

    for k in range(m):
        reveal_at[k].sort()

        for _, word in reveal_at[k]:
            if word not in normal_words and word not in revealed_spoiler_words:
                important_count += 1

            revealed_spoiler_words.add(word)

    return important_count