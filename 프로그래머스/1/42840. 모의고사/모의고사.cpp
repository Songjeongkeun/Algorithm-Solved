#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int x1 = 0, x2 = 0, x3 = 0;
    int y1[5] = {1,2,3,4,5};
    int y2[8] = {2,1,2,3,2,4,2,5};
    int y3[10] = {3,3,1,1,2,2,4,4,5,5};
    for(int i = 0; i < answers.size(); i++){
        if(answers[i] == y1[i % 5]) x1++;
        if(answers[i] == y2[i % 8]) x2++;
        if(answers[i] == y3[i % 10]) x3++;
    }
    int tmp = max(max(x1, x2), x3);
    if(x1 == tmp) answer.push_back(1);
    if(x2 == tmp) answer.push_back(2);
    if(x3 == tmp) answer.push_back(3);
    return answer;
}