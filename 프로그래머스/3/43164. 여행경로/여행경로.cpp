#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[10001] = {0,};
vector<string> answer;
bool isAnswer;

void dfs(string start, int cnt, vector<vector<string>> tickets){
    answer.push_back(start);
    
    if(cnt == tickets.size()){
        isAnswer = true;
    }
    
    for(int i = 0; i < tickets.size(); i++){
        if(visited[i]) continue;
        if(tickets[i][0] == start){
            visited[i] = true;
            dfs(tickets[i][1], cnt+1, tickets);
            if(!isAnswer){
                answer.pop_back();
                visited[i] = false;
            }
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    dfs("ICN", 0, tickets);
    return answer;
}