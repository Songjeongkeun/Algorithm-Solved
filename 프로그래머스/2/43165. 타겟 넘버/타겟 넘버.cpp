#include <string>
#include <vector>

using namespace std;

void get_target_number(vector<int> numbers, int target, int sum, int index, int& answer){
    if(index == numbers.size()){
        if(sum == target)
            answer++;
    return;
    }
    get_target_number(numbers, target, sum + numbers[index], index+1, answer);
    get_target_number(numbers, target, sum - numbers[index], index+1, answer);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    get_target_number(numbers, target, 0, 0, answer);
    return answer;
}