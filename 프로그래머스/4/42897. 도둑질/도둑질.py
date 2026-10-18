def solution(money):
    n = len(money)

    # 일자로 놓인 집에서 훔칠 수 있는 최댓값
    def rob(arr):
        prev2 = 0
        prev1 = 0

        for m in arr:
            cur = max(prev1, prev2 + m)
            prev2 = prev1
            prev1 = cur

        return prev1

    # 1. 첫 번째 집 포함 가능, 마지막 집 제외
    case1 = rob(money[:-1])

    # 2. 첫 번째 집 제외, 마지막 집 포함 가능
    case2 = rob(money[1:])

    return max(case1, case2)