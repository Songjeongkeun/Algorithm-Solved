def solution(gems):
    total_count = len(set(gems))
    gem_count = {}

    left = 0
    answer = [1, len(gems)]
    min_length = len(gems) + 1

    for right in range(len(gems)):
        gem = gems[right]

        if gem in gem_count:
            gem_count[gem] += 1
        else:
            gem_count[gem] = 1

        while len(gem_count) == total_count:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                answer = [left + 1, right + 1]

            left_gem = gems[left]
            gem_count[left_gem] -= 1

            if gem_count[left_gem] == 0:
                del gem_count[left_gem]

            left += 1

    return answer