def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    def count_until(t):
        second_minute = (59 * t) // 3600
        second_hour = (719 * t) // 43200
        triple_overlap = t // 43200

        return second_minute + second_hour - triple_overlap

    answer = count_until(end) - count_until(start)

    # 구간은 시작 시각을 포함한다.
    if start % 3600 == 0:
        answer += 1

    return answer