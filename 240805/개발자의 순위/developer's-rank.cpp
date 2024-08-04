#include <iostream>
#include <vector>
using namespace std;

int main() {
    int k, n;
    cin >> k >> n;
    
    vector<vector<int>> rank(k, vector<int>(n + 1));
    
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < n; j++) {
            int developer;
            cin >> developer;
            rank[i][developer] = j;  // 각 개발자의 순위를 기록
        }
    }
    
    int count = 0;
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            if (a == b) continue;
            
            bool always_better = true;
            for (int game = 0; game < k; game++) {
                if (rank[game][a] >= rank[game][b]) {
                    always_better = false;
                    break;
                }
            }
            
            if (always_better) count++;
        }
    }
    
    cout << count << endl;
    return 0;
}