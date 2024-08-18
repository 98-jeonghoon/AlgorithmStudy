import java.io.*;
import java.util.*;

public class Main {
    static int n, m, maxValue;
    static int[] arr;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 최대로 자를 수 있는 값
        maxValue = Integer.MIN_VALUE;

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            maxValue = Math.max(arr[i], maxValue);
        }

        int left = 1, right = maxValue;
        int answer = Integer.MIN_VALUE;
        while (left <= right) {
            int mid = (left + right) / 2;
            int cnt = 0;

            for (int i = 0; i < n; i++) {
                cnt += arr[i] / mid;
            }

            // cnt가 더 많이 나오면
            if (cnt >= m) {
                left = mid + 1;
                answer = Math.max(mid, answer);
            }else
                right = mid - 1;
        }
        System.out.println(answer);
    }


}