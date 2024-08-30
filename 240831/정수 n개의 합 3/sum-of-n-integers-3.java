import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[][] arr, prefixSum;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new int[n + 1][n + 1];
        prefixSum = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = Integer.MIN_VALUE;

        if (k == 1) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    answer = Math.max(arr[i][j], answer);
                }
            }
            System.out.println(answer);
            return;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + arr[i][j];
            }
        }

        for (int i = k; i <= n; i++) {
            for (int j = k; j <= n; j++) {
                int total = prefixSum[i][j] 
                          - prefixSum[i - k][j] 
                          - prefixSum[i][j - k] 
                          + prefixSum[i - k][j - k];
                answer = Math.max(answer, total);
            }
        }

        System.out.println(answer);
    }
}