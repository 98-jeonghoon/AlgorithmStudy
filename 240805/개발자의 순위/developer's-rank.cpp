#include <iostream>
#include <algorithm>
using namespace std;

int k, n;
int arr[100][100];
int rank[100][100];

int main() {
    cin >> k >> n;
    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            cin >> arr[i][j];
        }
    }
    
    // 각 경기에서의 순위 계산
    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            rank[i][arr[i][j] - 1] = j;
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