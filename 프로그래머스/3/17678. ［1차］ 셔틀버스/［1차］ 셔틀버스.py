def solution(n, t, m, timetable):
    def to_minutes(time_text):
        hour, minute = map(int, time_text.split(":"))
        return hour * 60 + minute

    def to_time(minutes):
        return f"{minutes // 60:02d}:{minutes % 60:02d}"

    crew_times = sorted(to_minutes(time) for time in timetable)

    index = 0
    last_shuttle_time = 9 * 60 + (n - 1) * t

    for shuttle_index in range(n):
        shuttle_time = 9 * 60 + shuttle_index * t
        boarded = 0
        last_boarded_time = -1

        while (
            index < len(crew_times)
            and boarded < m
            and crew_times[index] <= shuttle_time
        ):
            last_boarded_time = crew_times[index]
            index += 1
            boarded += 1

        # 마지막 셔틀의 탑승 결과로 콘의 도착 시각을 결정한다.
        if shuttle_time == last_shuttle_time:
            if boarded < m:
                return to_time(shuttle_time)

            return to_time(last_boarded_time - 1)