def solution(play_time, adv_time, logs):
    def to_seconds(time):
        hour, minute, second = map(int, time.split(":"))

        return hour * 3600 + minute * 60 + second

    def to_time(seconds):
        hour = seconds // 3600
        minute = (seconds % 3600) // 60
        second = seconds % 60

        return f"{hour:02d}:{minute:02d}:{second:02d}"

    play_seconds = to_seconds(play_time)
    adv_seconds = to_seconds(adv_time)

    # 각 시각에서 발생하는 시청자 수의 변화를 저장한다.
    viewer_changes = [0] * (play_seconds + 1)

    for log in logs:
        start_text, end_text = log.split("-")
        start = to_seconds(start_text)
        end = to_seconds(end_text)

        viewer_changes[start] += 1
        viewer_changes[end] -= 1

    # 첫 번째 누적합: 각 초의 시청자 수를 구한다.
    for second in range(1, play_seconds):
        viewer_changes[second] += viewer_changes[second - 1]

    # 두 번째 누적합: 0초부터 각 시각까지의 누적 시청 시간을 구한다.
    prefix = [0] * (play_seconds + 1)

    for second in range(play_seconds):
        prefix[second + 1] = (
            prefix[second] + viewer_changes[second]
        )

    best_start = 0
    max_watch_time = prefix[adv_seconds]

    # 광고를 시작할 수 있는 모든 시각을 확인한다.
    for start in range(1, play_seconds - adv_seconds + 1):
        end = start + adv_seconds
        watch_time = prefix[end] - prefix[start]

        # 같은 누적 시청 시간이면 더 빠른 기존 시각을 유지한다.
        if watch_time > max_watch_time:
            max_watch_time = watch_time
            best_start = start

    return to_time(best_start)