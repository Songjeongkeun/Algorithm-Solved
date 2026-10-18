from collections import deque

def solution(priorities, location):
    queue = deque()

    for i, priority in enumerate(priorities):
        queue.append((i, priority))

    answer = 0

    while queue:
        current_index, current_priority = queue.popleft()

        has_higher_priority = False

        for _, priority in queue:
            if priority > current_priority:
                has_higher_priority = True
                break

        if has_higher_priority:
            queue.append((current_index, current_priority))
        else:
            answer += 1

            if current_index == location:
                return answer