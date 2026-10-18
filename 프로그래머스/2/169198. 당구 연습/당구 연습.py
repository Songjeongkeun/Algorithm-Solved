def solution(m, n, startX, startY, balls):
    answer = []

    for target_x, target_y in balls:
        distances = []

        # 왼쪽 벽 반사
        if not (startY == target_y and startX > target_x):
            distances.append(
                (startX + target_x) ** 2
                + (startY - target_y) ** 2
            )

        # 오른쪽 벽 반사
        if not (startY == target_y and startX < target_x):
            distances.append(
                (2 * m - startX - target_x) ** 2
                + (startY - target_y) ** 2
            )

        # 아래쪽 벽 반사
        if not (startX == target_x and startY > target_y):
            distances.append(
                (startX - target_x) ** 2
                + (startY + target_y) ** 2
            )

        # 위쪽 벽 반사
        if not (startX == target_x and startY < target_y):
            distances.append(
                (startX - target_x) ** 2
                + (2 * n - startY - target_y) ** 2
            )

        answer.append(min(distances))

    return answer