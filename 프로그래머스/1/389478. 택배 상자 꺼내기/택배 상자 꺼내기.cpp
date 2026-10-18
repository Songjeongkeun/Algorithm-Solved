#include <string>
#include <vector>

using namespace std;


int getCol(int box, int w) {
    int row = (box - 1) / w;
    int idx = (box - 1) % w;

    if (row % 2 == 0) {
        return idx;
    } else {
        return w - 1 - idx;
    }
}

int solution(int n, int w, int num) {
    int answer = 1; // num 자기 자신 포함

    int targetCol = getCol(num, w);

    for (int box = num + 1; box <= n; box++) {
        if (getCol(box, w) == targetCol) {
            answer++;
        }
    }

    return answer;
}