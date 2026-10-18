def solution(sequence):
    current_first = 0
    current_second = 0
    answer = -float("inf")

    for index, value in enumerate(sequence):
        # 전체 수열 기준 [1, -1, 1, -1, ...] 패턴
        first_value = value if index % 2 == 0 else -value
        second_value = -first_value

        # 각 패턴에서 현재 인덱스로 끝나는 최대 연속 부분합
        current_first = max(first_value, current_first + first_value)
        current_second = max(second_value, current_second + second_value)

        answer = max(answer, current_first, current_second)

    return answer