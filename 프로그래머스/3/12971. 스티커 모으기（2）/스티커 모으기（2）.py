def solution(sticker):
    # 스티커가 한 장이면 해당 스티커를 선택한다.
    if len(sticker) == 1:
        return sticker[0]

    def get_max_sum(values):
        # dp[i - 2], dp[i - 1]
        two_before = 0
        one_before = 0

        for value in values:
            # 현재 스티커를 선택하지 않는 경우와
            # 현재 스티커를 선택하는 경우를 비교한다.
            current = max(
                one_before,
                two_before + value
            )

            two_before, one_before = one_before, current

        return one_before

    # 첫 번째 스티커를 고려하기 위해 마지막 스티커를 제외한다.
    exclude_last = get_max_sum(sticker[:-1])

    # 마지막 스티커를 고려하기 위해 첫 번째 스티커를 제외한다.
    exclude_first = get_max_sum(sticker[1:])

    return max(exclude_last, exclude_first)