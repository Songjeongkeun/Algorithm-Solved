def solution(n, m, x, y, queries):
    # 최종 위치에 도달할 수 있는 현재 좌표 범위
    top = bottom = x
    left = right = y

    # 마지막 쿼리부터 역방향으로 되돌린다.
    for direction, dx in reversed(queries):
        if direction == 0:
            # 왼쪽 이동의 역연산
            if left != 0:
                left += dx

            right = min(m - 1, right + dx)

        elif direction == 1:
            # 오른쪽 이동의 역연산
            if right != m - 1:
                right -= dx

            left = max(0, left - dx)

        elif direction == 2:
            # 위쪽 이동의 역연산
            if top != 0:
                top += dx

            bottom = min(n - 1, bottom + dx)

        else:
            # 아래쪽 이동의 역연산
            if bottom != n - 1:
                bottom -= dx

            top = max(0, top - dx)

        # 가능한 이전 위치가 없으면 종료한다.
        if top > bottom or left > right:
            return 0

    return (bottom - top + 1) * (right - left + 1)