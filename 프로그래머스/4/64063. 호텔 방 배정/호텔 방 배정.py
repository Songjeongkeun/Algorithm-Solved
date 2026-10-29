def solution(k, room_number):
    # 사용된 방 -> 다음으로 확인할 후보 방
    next_free = {}
    answer = []

    def find(room):
        path = []

        # 딕셔너리에 없는 번호는 아직 비어 있는 방이다.
        while room in next_free:
            path.append(room)
            room = next_free[room]

        # 지나온 방들이 빈 방을 바로 가리키도록 경로 압축한다.
        for occupied_room in path:
            next_free[occupied_room] = room

        return room

    for requested_room in room_number:
        assigned_room = find(requested_room)
        answer.append(assigned_room)

        # 방을 사용 처리하고, 다음 번호를 다음 후보로 연결한다.
        next_free[assigned_room] = assigned_room + 1

    return answer