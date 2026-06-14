from collections import Counter


def solution(points, routes):
    robot_count = len(routes)

    # 모든 로봇은 경로의 첫 번째 포인트에서 시작한다.
    positions = [
        points[route[0] - 1][:]
        for route in routes
    ]

    # 다음으로 방문할 포인트는 경로의 두 번째 원소다.
    next_index = [1] * robot_count
    active = [True] * robot_count

    answer = 0

    while any(active):
        # 현재 시간에 같은 좌표에 있는 로봇 수를 센다.
        position_count = Counter(
            tuple(positions[i])
            for i in range(robot_count)
            if active[i]
        )

        # 로봇이 2대 이상 있는 좌표마다 위험 상황 1회를 더한다.
        answer += sum(
            count >= 2
            for count in position_count.values()
        )

        # 모든 로봇을 동시에 한 칸씩 이동시킨다.
        for i in range(robot_count):
            if not active[i]:
                continue

            # 마지막 포인트에 도착한 로봇은 다음 시간부터 제외한다.
            if next_index[i] == len(routes[i]):
                active[i] = False
                continue

            target_point = routes[i][next_index[i]] - 1
            target_r, target_c = points[target_point]
            r, c = positions[i]

            # r 좌표를 먼저 이동한다.
            if r != target_r:
                r += 1 if r < target_r else -1
            else:
                c += 1 if c < target_c else -1

            positions[i] = [r, c]

            # 목표 포인트에 도착했다면 다음 포인트를 목표로 설정한다.
            if r == target_r and c == target_c:
                next_index[i] += 1

    return answer