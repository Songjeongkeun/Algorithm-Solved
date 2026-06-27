def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1
    start = 1

    for station in stations:
        left = station - w
        right = station + w

        if start < left:
            length = left - start
            answer += (length + coverage - 1) // coverage

        start = right + 1

    if start <= n:
        length = n - start + 1
        answer += (length + coverage - 1) // coverage

    return answer