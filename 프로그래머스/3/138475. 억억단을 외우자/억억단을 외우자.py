from math import isqrt


def solution(e, starts):
    count = [0] * (e + 1)

    for divisor in range(1, isqrt(e) + 1):
        square = divisor * divisor

        # (divisor, divisor)는 한 위치만 차지한다.
        count[square] += 1

        # 서로 다른 인수의 쌍은 순서를 바꾼 두 위치에 등장한다.
        for number in range(square + divisor, e + 1, divisor):
            count[number] += 2

    best = [0] * (e + 1)
    candidate = e

    for number in range(e, min(starts) - 1, -1):
        # 동점이면 더 작은 수인 number를 선택한다.
        if count[number] >= count[candidate]:
            candidate = number

        best[number] = candidate

    return [best[start] for start in starts]