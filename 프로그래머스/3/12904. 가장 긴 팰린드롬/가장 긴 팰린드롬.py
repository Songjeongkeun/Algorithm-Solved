def solution(s):
    length = len(s)
    answer = 1

    for center in range(length):
        left = center
        right = center

        while left >= 0 and right < length and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1

        left = center
        right = center + 1

        while left >= 0 and right < length and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1

    return answer