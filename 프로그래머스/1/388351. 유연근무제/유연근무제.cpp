#include <string>
#include <vector>

using namespace std;

int timeToMinute(int n){
    int hour = n / 100;
    int minute = n % 100;
    int total = minute + hour * 60;
    
    return total;
}

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;
    for(int i = 0; i < schedules.size(); i++){
        bool condition = true;
        int a = timeToMinute(schedules[i]) + 10;
        for(int j = 0; j < 7; j++){  
            int today = (startday + j - 1) % 7 + 1;
            int time = timeToMinute(timelogs[i][j]);
            if(today <=5){
                if(time > a){
                    condition = false;
                    break;
                }
            }
        }
        if(condition)
            answer++;
    }
    return answer;
}