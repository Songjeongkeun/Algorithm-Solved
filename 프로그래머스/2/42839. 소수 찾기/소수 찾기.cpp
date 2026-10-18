#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

set<int> numberSet;

bool isPrime(int num){
    if(num == 0 || num == 1)
        return false;
    for(int i = 2; i * i <= num; i++){
        if(num % i == 0)
            return false;
    }
    return true;
}

void makeCombination(string number, string others){
    if(number != "")
        numberSet.insert(stoi(number));
    
    for (int i = 0; i < others.size(); i++)
        makeCombination(number + others[i], others.substr(0, i) + others.substr(i + 1));
}


int solution(string numbers) {
    int answer = 0;
    makeCombination("", numbers);
    for(int number : numberSet)
        if(isPrime(number))
            answer++;
    return answer;
}