def solution(n, bans):
    def to_number(word):
        number = 0

        for char in word:
            value = ord(char) - ord("a") + 1
            number = number * 26 + value

        return number

    def to_word(number):
        result = []

        while number > 0:
            number, remainder = divmod(number - 1, 26)
            result.append(chr(ord("a") + remainder))

        return "".join(reversed(result))

    banned_numbers = sorted(to_number(word) for word in bans)

    target = n

    for banned_number in banned_numbers:
        if banned_number <= target:
            target += 1
        else:
            break

    return to_word(target)