#include<vector>
#include<queue>
using namespace std;

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

int BFS(vector<vector<int>> &maps){
    queue<pair<int, int>> q;
    int n = maps.size();
    int m = maps[0].size();
    
    q.push({0,0});
    
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx < 0 || nx >= n || ny < y || ny >= m){
                continue;
            }
            
            if(maps[nx][ny] == 0){
                continue;
            }
            
            if(maps[nx][ny] == 1){
                maps[nx][ny] = maps[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    if (maps[n - 1][m - 1] == 1)
        return -1;
    
    return maps[n-1][m-1];
}


int solution(vector<vector<int> > maps)
{
    int answer = BFS(maps);
    return answer;
}