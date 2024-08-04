#include <iostream>
using namespace std;

int k, n;

int main() {
    cin >> k >> n;
    int arr[100][100];
    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            cin >> arr[i][j];
        }
    }
    
    int total_cnt = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(j == i) continue;
            int cnt = 0;
            
            for(int l = 0; l < k; l++){
                if(arr[l][i] > arr[l][j]) ++cnt;
            }
            
            if(cnt == k) ++total_cnt;
        }   
    }
    
    cout << total_cnt;
    return 0;
}