def solution(d, budget):
    d.sort()

    answer = 0

    for cost in d:
        if budget < cost:
            break

        budget -= cost
        answer += 1

    return answer