def solution(n, cores):
    core_count = len(cores)

    # 시작 시각에 앞 번호 코어부터 하나씩 작업을 받는다.
    if n <= core_count:
        return n

    def assigned_work_count(time):
        return core_count + sum(time // core for core in cores)

    left = 0
    right = max(cores) * (n - core_count)

    # n번째 작업이 배정되는 최소 시각을 찾는다.
    while left < right:
        mid = (left + right) // 2

        if assigned_work_count(mid) >= n:
            right = mid
        else:
            left = mid + 1

    time = left
    assigned_before = assigned_work_count(time - 1)
    remaining = n - assigned_before

    # 같은 시각에 비는 코어는 번호순으로 다음 작업을 받는다.
    for index, core in enumerate(cores, start=1):
        if time % core == 0:
            remaining -= 1

            if remaining == 0:
                return index