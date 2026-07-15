def solution(n, build_frame):
    structures = set()

    def is_valid():
        for x, y, structure_type in structures:
            if structure_type == 0:  # 기둥
                valid_pillar = (
                    y == 0
                    or (x - 1, y, 1) in structures
                    or (x, y, 1) in structures
                    or (x, y - 1, 0) in structures
                )

                if not valid_pillar:
                    return False

            else:  # 보
                valid_beam = (
                    (x, y - 1, 0) in structures
                    or (x + 1, y - 1, 0) in structures
                    or (
                        (x - 1, y, 1) in structures
                        and (x + 1, y, 1) in structures
                    )
                )

                if not valid_beam:
                    return False

        return True

    for x, y, structure_type, command in build_frame:
        structure = (x, y, structure_type)

        if command == 1:  # 설치
            structures.add(structure)

            if not is_valid():
                structures.remove(structure)

        else:  # 삭제
            structures.discard(structure)

            if not is_valid():
                structures.add(structure)

    return [list(structure) for structure in sorted(structures)]