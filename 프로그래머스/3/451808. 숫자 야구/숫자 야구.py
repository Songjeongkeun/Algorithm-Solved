from itertools import permutations


def solution(n, submit):
    def get_result(guess, answer):
        strike = 0
        ball = 0

        for i in range(4):
            if guess[i] == answer[i]:
                strike += 1
            elif guess[i] in answer:
                ball += 1

        return strike, ball

    def parse_result(result):
        strike_text, ball_text = result.split()
        strike = int(strike_text[:-1])
        ball = int(ball_text[:-1])
        return strike, ball

    candidates = [
        "".join(number)
        for number in permutations("123456789", 4)
    ]

    for _ in range(n):
        guess = candidates[0]
        result = parse_result(submit(int(guess)))

        if result == (4, 0):
            return int(guess)

        candidates = [
            candidate
            for candidate in candidates
            if get_result(guess, candidate) == result
        ]

    return int(candidates[0])