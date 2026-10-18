#include <string>
#include <vector>

using namespace std;

int answer = 0;

int graph[101][101] = {0,};
vector<bool> visited = vector<bool>(101, false);

int dfs(int cur, int n){
    if(visited[cur]) return 0;
    
    int link = 1;
    visited[cur] = true;
    for(int i = 1; i <= n; i++){
        if(graph[cur][i]){
            link += dfs(i, n);
        }
    }
    return link; 
}

int solution(int n, vector<vector<int>> wires) {
    int answer = 999;
    for(int i = 0; i < wires.size(); ++i)
    {
        int x = wires[i][0];
        int y = wires[i][1];
        graph[x][y] = graph[y][x] = 1;
    }
    
    for(int i = 0; i < wires.size(); ++i)
    {
        // 간선을 하나씩 끊어본다.
        int x = wires[i][0];
        int y = wires[i][1];
        graph[x][y] = graph[y][x] = 0;
        
        // 방문 체크 초기화
        fill(visited.begin(),visited.end(),false);
        
        // 간선을 하나씩 끊었을 때, 연결된 송전탑 수를 저장할 vector
        vector<int> linked_node;
        
        // 연결된 송전탑의 수를 dfs를 사용해 계산한다.
        for(int i = 1; i <= n; ++i)
        {
            int link = dfs(i, n);
            if(!link)
                continue;
            
            linked_node.push_back(link);
        }
        
        // 지금까지의 차이값과 현재 차이값 중에 더 작은 쪽을 저장한다.
        int diff =  abs(linked_node[0]-linked_node[1]);
        answer = answer <= diff ? answer : diff;
        
        // 차이가 0일때가 최선의 결과이므로 더 이상 계산하지 않는다.
        if(answer == 0) break;
    
        // 간선을 다시 연결한다.
        graph[x][y] = graph[y][x] = 1;
    }
    return answer;
}