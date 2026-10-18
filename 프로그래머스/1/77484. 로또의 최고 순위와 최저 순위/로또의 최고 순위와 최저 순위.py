def solution(lottos, win_nums):
    ranks = [6, 6, 5, 4, 3, 2, 1]

    zero_count = lottos.count(0)
    match_count = 0

    for number in lottos:
        if number in win_nums:
            match_count += 1

    best_rank = ranks[match_count + zero_count]
    worst_rank = ranks[match_count]

    return [best_rank, worst_rank]