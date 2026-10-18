from heapq import heappop, heappush


def solution(city, road):
    INF = 10**18
    road_count = len(road)

    # (x1, y1, x2, y2, limit) 형태로 도로를 저장한다.
    roads = [tuple(info) for info in road]
    road_points = [[] for _ in range(road_count)]
    camera_limit = {}

    def is_horizontal(current_road):
        return current_road[1] == current_road[3]

    def contains(current_road, x, y):
        x1, y1, x2, y2, _ = current_road
        return x1 <= x <= x2 and y1 <= y <= y2

    def add_point(road_index, point):
        road_points[road_index].append(point)

    # 도로의 끝점과 중앙 카메라 위치를 추가한다.
    for index, (x1, y1, x2, y2, limit) in enumerate(roads):
        add_point(index, (x1, y1))
        add_point(index, (x2, y2))

        camera = ((x1 + x2) // 2, (y1 + y2) // 2)
        add_point(index, camera)
        camera_limit[camera] = min(camera_limit.get(camera, INF), limit)

    # 도시가 포함된 모든 도로에 도시 위치를 분할 지점으로 추가한다.
    for x, y in city:
        for index, current_road in enumerate(roads):
            if contains(current_road, x, y):
                add_point(index, (x, y))

    # 모든 도로 쌍의 교차점 또는 접점을 찾는다.
    for first in range(road_count):
        x1, y1, x2, y2, _ = roads[first]
        first_is_horizontal = is_horizontal(roads[first])

        for second in range(first + 1, road_count):
            a1, b1, a2, b2, _ = roads[second]
            second_is_horizontal = is_horizontal(roads[second])
            point = None

            if first_is_horizontal != second_is_horizontal:
                horizontal = roads[first] if first_is_horizontal else roads[second]
                vertical = roads[second] if first_is_horizontal else roads[first]

                hx1, hy, hx2, _, _ = horizontal
                vx, vy1, _, vy2, _ = vertical

                if hx1 <= vx <= hx2 and vy1 <= hy <= vy2:
                    point = (vx, hy)

            elif first_is_horizontal and y1 == b1:
                left = max(x1, a1)
                right = min(x2, a2)
                if left == right:
                    point = (left, y1)

            elif not first_is_horizontal and x1 == a1:
                bottom = max(y1, b1)
                top = min(y2, b2)
                if bottom == top:
                    point = (x1, bottom)

            if point is not None:
                add_point(first, point)
                add_point(second, point)

    # 동일 좌표를 하나의 그래프 정점으로 합친다.
    point_to_index = {}

    def get_index(point):
        if point not in point_to_index:
            point_to_index[point] = len(point_to_index)
        return point_to_index[point]

    # 먼저 모든 중요 지점에 그래프 번호를 부여한다.
    for points in road_points:
        for point in points:
            get_index(point)

    graph = [[] for _ in range(len(point_to_index))]

    # 각 도로의 이웃한 중요 지점을 연결한다.
    for index, points in enumerate(road_points):
        current_road = roads[index]

        if is_horizontal(current_road):
            ordered_points = sorted(set(points), key=lambda point: point[0])
        else:
            ordered_points = sorted(set(points), key=lambda point: point[1])

        for left, right in zip(ordered_points, ordered_points[1:]):
            # 카메라 정점을 지나기 위해 지켜야 하는 가장 낮은 제한 속도
            limit = min(
                camera_limit.get(left, INF),
                camera_limit.get(right, INF),
            )

            left_index = get_index(left)
            right_index = get_index(right)
            graph[left_index].append((right_index, limit))
            graph[right_index].append((left_index, limit))

    start = get_index(tuple(city[0]))
    best_speed = [-1] * len(graph)
    best_speed[start] = INF
    heap = [(-INF, start)]

    # 제한 속도가 큰 경로부터 확정하는 Widest Path 탐색
    while heap:
        negative_speed, current = heappop(heap)
        current_speed = -negative_speed

        if current_speed < best_speed[current]:
            continue

        for next_node, limit in graph[current]:
            next_speed = min(current_speed, limit)

            if next_speed > best_speed[next_node]:
                best_speed[next_node] = next_speed
                heappush(heap, (-next_speed, next_node))

    answer = []
    for x, y in city[1:]:
        speed = best_speed[get_index((x, y))]
        answer.append(0 if speed == INF else speed)

    return answer