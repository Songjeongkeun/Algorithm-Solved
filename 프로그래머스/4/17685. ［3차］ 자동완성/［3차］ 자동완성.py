def common_prefix_length(first, second):
    limit = min(len(first), len(second))
    index = 0

    while index < limit and first[index] == second[index]:
        index += 1

    return index


def solution(words):
    words.sort()
    total = 0

    for index, word in enumerate(words):
        longest_common_prefix = 0

        if index > 0:
            longest_common_prefix = max(
                longest_common_prefix,
                common_prefix_length(word, words[index - 1])
            )

        if index + 1 < len(words):
            longest_common_prefix = max(
                longest_common_prefix,
                common_prefix_length(word, words[index + 1])
            )

        # word가 다른 단어의 접두사인 경우에는 단어 전체를 입력해야 한다.
        total += min(len(word), longest_common_prefix + 1)

    return total
