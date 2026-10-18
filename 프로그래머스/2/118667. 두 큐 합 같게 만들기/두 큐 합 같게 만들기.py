def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)

    if total % 2 == 1:
        return -1

    target = total // 2
    n = len(queue1)
    combined = queue1 + queue2

    left = 0
    right = n
    current_sum = sum(queue1)

    count = 0
    limit = n * 3

    while count <= limit:
        if current_sum == target:
            return count

        if current_sum < target:
            current_sum += combined[right % (2 * n)]
            right += 1
        else:
            current_sum -= combined[left % (2 * n)]
            left += 1

        count += 1

    return -1