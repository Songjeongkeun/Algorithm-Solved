#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long GCD(long long a, long long b){
    if(!b)
        return a;
    return GCD(b, a % b);
}

int solution(vector<vector<int>> signals) {
    long long curLen, newLen, temp, t;
    vector<long long> len, times;
    for(int i = 0; i < signals.size(); i++){
        len.push_back((long long)signals[i][0] + signals[i][1] + signals[i][2]);
    }
    curLen = len[0];
    for(int i = signals[0][0]; i < signals[0][0] + signals[0][1]; i++){
        times.push_back(i);
    }
    for(int i = 1; i < signals.size(); i++){
        newLen = (curLen * len[i]) / GCD(curLen, len[i]);
        
        vector<long long> nextT;
        for(int j = 0; j < times.size(); j++){
            t = times[j];
            while(t < newLen){
                temp = t % len[i];
                
                if((temp >= signals[i][0]) && (temp < (signals[i][0] + signals[i][1])))
                    nextT.push_back(t);
                
                t += curLen;
            }
        }
        if(nextT.empty())
            return -1;
        
        curLen = newLen;
        times = nextT;
    }
    sort(times.begin(), times.end());
    return (int)times[0] + 1;
}