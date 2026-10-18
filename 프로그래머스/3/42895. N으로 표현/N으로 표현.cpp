#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int N, int number) {
    vector<set<int>> dp(9);

    for (int i = 1; i <= 8; i++) {
        int num = 0;

        // N, NN, NNN 만들기
        for (int j = 0; j < i; j++) {
            num = num * 10 + N;
        }

        dp[i].insert(num);

        // N을 j번 쓴 결과와 i-j번 쓴 결과 조합
        for (int j = 1; j < i; j++) {
            for (int a : dp[j]) {
                for (int b : dp[i - j]) {
                    dp[i].insert(a + b);
                    dp[i].insert(a - b);
                    dp[i].insert(a * b);

                    if (b != 0) {
                        dp[i].insert(a / b);
                    }
                }
            }
        }

        if (dp[i].count(number)) {
            return i;
        }
    }

    return -1;
}