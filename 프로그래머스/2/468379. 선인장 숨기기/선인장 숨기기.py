from collections import deque


def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    rain_time = [INF] * (m * n)

    for time, (row, col) in enumerate(drops, 1):
        rain_time[row * n + col] = time

    row_window_count = n - w + 1
    row_min = [0] * (m * row_window_count)

    for row in range(m):
        dq = deque()
        row_start = row * n
        output_start = row * row_window_count

        for col in range(n):
            current = row_start + col

            while dq and rain_time[dq[-1]] >= rain_time[current]:
                dq.pop()

            dq.append(current)

            if dq[0] <= row_start + col - w:
                dq.popleft()

            if col >= w - 1:
                output_col = col - w + 1
                row_min[output_start + output_col] = rain_time[dq[0]]

    best = -1
    answer = [0, 0]

    for col in range(row_window_count):
        dq = deque()

        for row in range(m):
            current = row * row_window_count + col

            while dq and row_min[dq[-1]] >= row_min[current]:
                dq.pop()

            dq.append(current)

            if dq[0] <= (row - h) * row_window_count + col:
                dq.popleft()

            if row >= h - 1:
                top_row = row - h + 1
                value = row_min[dq[0]]

                if value > best:
                    best = value
                    answer = [top_row, col]

    return answer