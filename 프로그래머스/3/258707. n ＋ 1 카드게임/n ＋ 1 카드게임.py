def solution(coin, cards):
    n = len(cards)
    target = n + 1

    hand = set(cards[:n // 3])
    candidate = set()

    round_count = 1

    def remove_pair_from_same(card_set):
        for card in list(card_set):
            pair = target - card

            if pair in card_set:
                card_set.remove(card)
                card_set.remove(pair)
                return True

        return False

    def remove_pair_from_each(left_set, right_set):
        for card in list(left_set):
            pair = target - card

            if pair in right_set:
                left_set.remove(card)
                right_set.remove(pair)
                return True

        return False

    for i in range(n // 3, n, 2):
        candidate.add(cards[i])
        candidate.add(cards[i + 1])

        if remove_pair_from_same(hand):
            round_count += 1
            continue

        if coin >= 1 and remove_pair_from_each(hand, candidate):
            coin -= 1
            round_count += 1
            continue

        if coin >= 2 and remove_pair_from_same(candidate):
            coin -= 2
            round_count += 1
            continue

        break

    return round_count