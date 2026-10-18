#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int> v1, pair<int, int> v2){
    if(v1.first == v2.first) return v1.second < v2.second;
    else return v1.first > v2.first;
}

bool cmp1(pair<string,int> v1, pair<string,int> v2){
    return v1.second > v2.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, vector<pair<int, int>>> m1;
    unordered_map<string, int> m2;
    for(int i = 0; i < genres.size(); i++){
        m1[genres[i]].push_back({plays[i], i});
        m2[genres[i]] += plays[i];
    }
    for(auto &x : m1){
        sort(x.second.begin(), x.second.end(), cmp);
    }
    vector<pair<string,int>> v(m2.begin(), m2.end());
    sort(v.begin(), v.end(), cmp1);
    for(auto x : v){
        for(int j = 0; j < m1[x.first].size(); j++){
            answer.push_back(m1[x.first][j].second);
            if(j) break;
        }
    }
    return answer;
}