#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> q, vector<int> ans) {
    int answer = 0;
    for(int a = 1;a <= n; a++){
        for(int b = a + 1; b <= n; b++){
            for(int c = b + 1; c <= n; c++){
                for(int d = c + 1; d <= n; d++){
                    for(int e = d + 1; e <= n; e++){
                        vector<int> arr = {a, b, c, d, e};
                        bool condition = true;
                        for(int i = 0; i < q.size(); i++){
                            int count = 0;
                            for(int x : arr)
                                for(int y : q[i])
                                    if(x == y) count++;
                            if(count != ans[i]){
                                condition = false;
                                break;
                            }
                        }
                        if(condition) answer++;
                    }    
                }
            }
        }
    }
    return answer;
}