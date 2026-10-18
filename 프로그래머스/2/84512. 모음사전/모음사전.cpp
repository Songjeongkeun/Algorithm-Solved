#include <string>
#include <vector>

using namespace std;

string arr = "AEIOU";
int answer = 0;
int cnt = 0;
bool found = false;

void dfs(string cur, string word){
    if(found) return; 
    
    if(cur == word){
        answer = cnt;
        return;
    }
    
    if(cur.length() == 5) return;
    
    for(int i = 0; i < 5; i++){
        cnt++;
        dfs(cur+arr[i], word);
    }
}

int solution(string word) {
    dfs("", word);
    return answer;
}