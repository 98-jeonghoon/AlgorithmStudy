#include <iostream>
#include <vector>
using namespace std;

int k, n;

int main() {
    cin >> k >> n;
    vector<vector<int>> arr(k, vector<int>(n));
    vector<vector<int>> rank(k, vector<int>(n));

    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            cin >> arr[i][j];
            arr[i][j]--; // 0-based 인덱스로 변환
        }
    }
    
    // 각 경기에서의 순위 계산
    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            rank[i][arr[i][j]] = j;
        }
    }
    
    int total_cnt = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(j == i) continue;
            bool always_better = true;
            
            for(int l = 0; l < k; l++){
                if(rank[l][i] >= rank[l][j]){
                    always_better = false;
                    break;
                }
            }
            
            if(always_better) ++total_cnt;
        }   
    }
    
    cout << total_cnt;
    return 0;
}