def solution(lines):
    intervals = []

    def to_milliseconds(time_text):
        hour, minute, second_text = time_text.split(":")
        second, millisecond = second_text.split(".")

        return (
            (int(hour) * 60 * 60 + int(minute) * 60 + int(second))
            * 1000
            + int(millisecond)
        )

    def duration_to_milliseconds(duration_text):
        number = duration_text[:-1]  # 마지막 's' 제거

        if "." not in number:
            return int(number) * 1000

        second, millisecond = number.split(".")
        millisecond = millisecond.ljust(3, "0")

        return int(second) * 1000 + int(millisecond)

    for line in lines:
        _, time_text, duration_text = line.split()

        end = to_milliseconds(time_text)
        duration = duration_to_milliseconds(duration_text)
        start = end - duration + 1

        intervals.append((start, end))

    max_throughput = 0

    for _, window_start in intervals:
        window_end = window_start + 999
        throughput = 0

        for start, end in intervals:
            if end >= window_start and start <= window_end:
                throughput += 1

        max_throughput = max(max_throughput, throughput)

    return max_throughput