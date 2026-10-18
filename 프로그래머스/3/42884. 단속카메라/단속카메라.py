def solution(routes):
    # 입력 방향과 무관하게 [시작 지점, 끝 지점] 형태로 정리한다.
    routes = [sorted(route) for route in routes]

    # 가장 빨리 끝나는 경로부터 확인한다.
    routes.sort(key=lambda route: route[1])

    camera_count = 0
    camera_position = -float("inf")

    for start, end in routes:
        # 현재 카메라가 이 차량의 경로 안에 없다면 새 카메라가 필요하다.
        if camera_position < start:
            camera_count += 1
            camera_position = end

    return camera_count