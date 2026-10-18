#include <string>
#include <vector>

using namespace std;

int solution(vector<int> players, int m, int k) {
    int answer = 0;
    int current = 0;
    vector<int> expire(24 + k + 1, 0);
    for(int i = 0; i < 24; i++){
        current -= expire[i];
        
        int need = players[i] / m;
        if(need > current){
            int add = need - current;
            answer += add;
            current += add;
            
            expire[i + k] += add;
        }
        
    }
    
   
    return answer;
}