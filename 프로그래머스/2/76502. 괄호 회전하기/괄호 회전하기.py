def solution(s):
    # 올바른 괄호 문자열은 길이가 항상 짝수다.
    if len(s) % 2 == 1:
        return 0

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def is_correct(brackets):
        stack = []

        for character in brackets:
            # 여는 괄호는 스택에 저장한다.
            if character in "([{":
                stack.append(character)
                continue

            # 닫는 괄호의 짝을 검사한다.
            if not stack:
                return False

            if stack[-1] != pairs[character]:
                return False

            stack.pop()

        return not stack

    answer = 0

    for shift in range(len(s)):
        rotated = s[shift:] + s[:shift]

        if is_correct(rotated):
            answer += 1

    return answer