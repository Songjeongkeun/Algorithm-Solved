#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int area = brown + yellow;
    for(int x = 3; x * x <= area; x++){
        if(area % x == 0){
            int y = area / x; 
        
            if((x + y - 2) * 2 == brown){
                answer.push_back(y);
                answer.push_back(x);
            } 
        }
    }
    return answer;
}