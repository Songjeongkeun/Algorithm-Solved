#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max_x = 0, max_y = 0;
    for(int i = 0; i < sizes.size(); i++){
        if(sizes[i][0] < sizes[i][1]){
            int tmp = sizes[i][1];
            sizes[i][1] = sizes[i][0];
            sizes[i][0] = tmp;
        }
            if(max_x < sizes[i][0])
                max_x = sizes[i][0];
            if(max_y < sizes[i][1])
                max_y = sizes[i][1];
    }

    answer = max_x * max_y;
    return answer;
}