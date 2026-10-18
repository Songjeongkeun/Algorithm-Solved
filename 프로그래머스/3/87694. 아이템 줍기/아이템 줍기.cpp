#include <string>
#include <vector>
#include <queue>

using namespace std;

int board[101][101] = {0,};
bool visited[101][101] = {false,};

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    // 좌표 2배
    characterX *= 2;
    characterY *= 2;
    itemX *= 2;
    itemY *= 2;
    
    // 1. 직사각형 전체 채우기
    for (auto& r : rectangle) {
        int x1 = r[0] * 2;
        int y1 = r[1] * 2;
        int x2 = r[2] * 2;
        int y2 = r[3] * 2;
        
        for (int x = x1; x <= x2; x++) {
            for (int y = y1; y <= y2; y++) {
                board[x][y] = 1;
            }
        }
    }
    
    // 2. 내부 지우기
    for (auto& r : rectangle) {
        int x1 = r[0] * 2;
        int y1 = r[1] * 2;
        int x2 = r[2] * 2;
        int y2 = r[3] * 2;
        
        for (int x = x1 + 1; x < x2; x++) {
            for (int y = y1 + 1; y < y2; y++) {
                board[x][y] = 0;
            }
        }
    }
    
    // 3. BFS
    queue<pair<pair<int,int>, int>> q;
    q.push({{characterX, characterY}, 0});
    visited[characterX][characterY] = true;
    
    while (!q.empty()) {
        int x = q.front().first.first;
        int y = q.front().first.second;
        int answer = q.front().second;
        q.pop();
        
        if (x == itemX && y == itemY) {
            return answer / 2;
        }
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || ny < 0 || nx > 100 || ny > 100) continue;
            if (visited[nx][ny]) continue;
            if (board[nx][ny] == 0) continue;
            
            visited[nx][ny] = true;
            q.push({{nx, ny}, answer + 1});
        }
    }
    
    return 0;
}