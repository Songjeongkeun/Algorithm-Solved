def solution(record):
    nickname_by_uid = {}
    events = []

    # 첫 번째 순회: 최신 닉네임과 이벤트 순서를 저장한다.
    for log in record:
        parts = log.split()
        command = parts[0]
        uid = parts[1]

        if command == "Enter":
            nickname_by_uid[uid] = parts[2]
            events.append((command, uid))

        elif command == "Leave":
            events.append((command, uid))

        else:
            # Change는 메시지를 남기지 않고 닉네임만 변경한다.
            nickname_by_uid[uid] = parts[2]

    answer = []

    # 두 번째 순회: 최종 닉네임으로 메시지를 만든다.
    for command, uid in events:
        nickname = nickname_by_uid[uid]

        if command == "Enter":
            answer.append(f"{nickname}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname}님이 나갔습니다.")

    return answer