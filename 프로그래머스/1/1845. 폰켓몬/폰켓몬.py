def solution(nums):
    num_s = set(nums)
    cnt = len(nums)
    cnt1 = cnt // 2
    return min(cnt1, len(num_s))