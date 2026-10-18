def solution(A, B):
    A.sort()
    B.sort()

    score = 0
    a_index = 0

    for b_number in B:
        # 현재 B 선수가 가장 작은 미매칭 A 선수를 이길 수 있다.
        if a_index < len(A) and b_number > A[a_index]:
            score += 1
            a_index += 1

    return score