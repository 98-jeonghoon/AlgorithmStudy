import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[] arr, prefixSum;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new int[n + 1];
        prefixSum = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        prefixSum[0] = arr[0];
        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        int answer = 0;
        for (int i = n; i > 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                if (prefixSum[i] - prefixSum[j] == k) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}