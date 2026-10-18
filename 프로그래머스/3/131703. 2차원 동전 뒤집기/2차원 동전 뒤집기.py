def solution(beginning, target):
    row_count = len(beginning)
    column_count = len(beginning[0])
    INF = float("inf")

    difference = [
        [
            beginning[row][column] ^ target[row][column]
            for column in range(column_count)
        ]
        for row in range(row_count)
    ]

    def count_flips(first_row_flip):
        row_flip = [0] * row_count
        col_flip = [0] * column_count

        # 첫 번째 행을 뒤집는지 여부를 가정한다.
        row_flip[0] = first_row_flip

        # 첫 번째 행 조건으로 모든 열의 뒤집기 여부를 정한다.
        for column in range(column_count):
            col_flip[column] = (
                difference[0][column]
                ^ row_flip[0]
            )

        # 첫 번째 열 조건으로 나머지 행의 뒤집기 여부를 정한다.
        for row in range(1, row_count):
            row_flip[row] = (
                difference[row][0]
                ^ col_flip[0]
            )

        # 모든 칸이 목표 상태가 되는지 검증한다.
        for row in range(row_count):
            for column in range(column_count):
                if (
                    row_flip[row] ^ col_flip[column]
                    != difference[row][column]
                ):
                    return INF

        return sum(row_flip) + sum(col_flip)

    answer = min(count_flips(0), count_flips(1))

    return -1 if answer == INF else answer