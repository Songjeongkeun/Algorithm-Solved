def solution(s):
    answer = []

    for string in s:
        stack = []
        count_110 = 0

        # 문자열에서 만들 수 있는 모든 "110"을 제거한다.
        for character in string:
            stack.append(character)

            if (
                len(stack) >= 3
                and stack[-3] == "1"
                and stack[-2] == "1"
                and stack[-1] == "0"
            ):
                del stack[-3:]
                count_110 += 1

        remaining = "".join(stack)

        # 마지막 0 바로 뒤에 제거한 "110"들을 삽입한다.
        # 0이 없으면 rfind가 -1을 반환하므로 삽입 위치는 0이 된다.
        insert_position = remaining.rfind("0") + 1

        converted = (
            remaining[:insert_position]
            + "110" * count_110
            + remaining[insert_position:]
        )

        answer.append(converted)

    return answer