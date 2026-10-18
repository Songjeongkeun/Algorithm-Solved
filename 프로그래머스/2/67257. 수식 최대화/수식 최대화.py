import re
from itertools import permutations


def calculate(left, operator, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    return left * right


def solution(expression):
    # 숫자는 int로, 연산자는 문자열로 저장한다.
    tokens = [
        int(token) if token.isdigit() else token
        for token in re.findall(r"\d+|[+*-]", expression)
    ]

    operators = {token for token in tokens if isinstance(token, str)}
    answer = 0

    # 순열의 앞 원소를 가장 높은 우선순위로 사용한다.
    for priority in permutations(operators):
        current = tokens[:]

        for target_operator in priority:
            reduced = [current[0]]

            # 현재 토큰은 항상 숫자, 연산자, 숫자 순서다.
            for index in range(1, len(current), 2):
                operator = current[index]
                right = current[index + 1]

                if operator == target_operator:
                    reduced[-1] = calculate(
                        reduced[-1],
                        operator,
                        right
                    )
                else:
                    reduced.extend([operator, right])

            current = reduced

        answer = max(answer, abs(current[0]))

    return answer