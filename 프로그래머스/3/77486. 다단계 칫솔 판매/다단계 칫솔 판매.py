def solution(enroll, referral, seller, amount):
    name_to_index = {
        name: index
        for index, name in enumerate(enroll)
    }

    parent = [
        -1 if referrer == "-" else name_to_index[referrer]
        for referrer in referral
    ]

    earnings = [0] * len(enroll)

    for seller_name, sold_count in zip(seller, amount):
        current = name_to_index[seller_name]
        profit = sold_count * 100

        while current != -1 and profit > 0:
            commission = profit // 10
            earnings[current] += profit - commission

            current = parent[current]
            profit = commission

    return earnings