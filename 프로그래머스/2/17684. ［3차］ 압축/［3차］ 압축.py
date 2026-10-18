def solution(msg):
    # A부터 Z까지 사전을 초기화한다.
    dictionary = {
        chr(code): code - ord("A") + 1
        for code in range(ord("A"), ord("Z") + 1)
    }

    next_index = 27
    answer = []
    current = ""

    for character in msg:
        candidate = current + character

        # 후보 문자열이 사전에 있으면 더 긴 문자열을 찾는다.
        if candidate in dictionary:
            current = candidate
            continue

        # current가 현재 입력과 일치하는 가장 긴 문자열이다.
        answer.append(dictionary[current])

        # current와 다음 글자를 합친 문자열을 사전에 추가한다.
        dictionary[candidate] = next_index
        next_index += 1

        # 현재 글자부터 다시 탐색을 시작한다.
        current = character

    # 마지막 문자열의 색인 번호를 출력한다.
    answer.append(dictionary[current])

    return answer
