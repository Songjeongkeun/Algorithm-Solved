def solution(numbers):
    costs = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
    ]
    
    INF = float('inf')
    dp = [[INF] * 10 for _ in range(10)]
    dp[4][6] = 0
    
    for num in numbers:
        num = int(num)
        
        next_dp = [[INF] * 10 for _ in range(10)]
        for left in range(10):
            for right in range(10):
                if dp[left][right] == INF:
                    continue
                    
                current = dp[left][right]
                
                if right != num: 
                    next_dp[num][right] = min(next_dp[num][right], current + costs[left][num])
                
                if left != num:
                    next_dp[left][num] = min(next_dp[left][num], current + costs[right][num])
                    
        dp = next_dp
    return min(map(min, dp))