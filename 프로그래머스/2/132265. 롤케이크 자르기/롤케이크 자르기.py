from collections import Counter


def solution(topping):
    # 처음에는 모든 토핑이 오른쪽 조각에 있다.
    right_count = Counter(topping)
    left_toppings = set()

    answer = 0

    # 마지막 토핑을 왼쪽으로 옮기면 오른쪽 조각이 비므로 제외한다.
    for index in range(len(topping) - 1):
        topping_type = topping[index]

        # 현재 토핑을 오른쪽에서 왼쪽으로 옮긴다.
        left_toppings.add(topping_type)
        right_count[topping_type] -= 1

        # 오른쪽에 해당 토핑이 더 이상 없으면 종류에서도 제거한다.
        if right_count[topping_type] == 0:
            del right_count[topping_type]

        # 양쪽 토핑 종류 수가 같으면 공평하게 나눈 경우다.
        if len(left_toppings) == len(right_count):
            answer += 1

    return answer