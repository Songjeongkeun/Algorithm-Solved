from collections import deque

def solution(places):
    answer = []

    def check(place):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue

                visited = [[False] * 5 for _ in range(5)]
                q = deque()
                q.append((i, j, 0))
                visited[i][j] = True

                while q:
                    x, y, dist = q.popleft()

                    if dist == 2:
                        continue

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue

                        if visited[nx][ny]:
                            continue

                        if place[nx][ny] == 'X':
                            continue

                        if place[nx][ny] == 'P':
                            return 0

                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))

        return 1

    for place in places:
        answer.append(check(place))

    return answer