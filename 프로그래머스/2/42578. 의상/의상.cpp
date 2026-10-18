#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, vector<string>> m;
    for(int i = 0; i < clothes.size(); i++){
        if(m.find(clothes[i][1]) == m.end()){
            vector<string> cloth;
            cloth.push_back(clothes[i][0]);
            m.insert(make_pair(clothes[i][1], cloth));
        }
        else {
            m[clothes[i][1]].push_back(clothes[i][0]);
        }
    }
    for(auto it = m.begin(); it != m.end(); it++){
        auto vec = it->second;
        answer *= vec.size()+1;
    }
    answer--;
    return answer;
}