def solution(plans):
    def to_minutes(time):
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute

    schedules = [
        (name, to_minutes(start), int(playtime))
        for name, start, playtime in plans
    ]
    schedules.sort(key=lambda schedule: schedule[1])

    completed = []
    paused = []

    for index, (name, start, playtime) in enumerate(schedules):
        # 새 과제를 시작한다.
        paused.append((name, playtime))

        # 마지막 과제라면 다음 시작 시각이 없다.
        if index == len(schedules) - 1:
            continue

        next_start = schedules[index + 1][1]
        available_time = next_start - start

        # 다음 과제가 시작되기 전까지 최근에 멈춘 과제부터 처리한다.
        while paused and available_time > 0:
            current_name, remaining_time = paused.pop()

            if remaining_time <= available_time:
                completed.append(current_name)
                available_time -= remaining_time
            else:
                paused.append((current_name, remaining_time - available_time))
                available_time = 0

    # 더 이상 새 과제가 시작되지 않으므로 스택 순서대로 모두 끝낸다.
    while paused:
        name, _ = paused.pop()
        completed.append(name)

    return completed