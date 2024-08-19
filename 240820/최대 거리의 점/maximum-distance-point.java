import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static long[] arr;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new long[n];

        long maxValue = 0;

        for(int i = 0; i < n; i++){
            arr[i] = Long.parseLong(br.readLine());
            maxValue = Math.max(maxValue, arr[i]);
        }

        Arrays.sort(arr);

        long left = 1, right = maxValue;
        long answer = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            if (check(mid)) {
                answer = mid;
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        System.out.println(answer);

    }

    static boolean check(long mid) {
        // 물건의 개수는 처음에 1개는 무조건 설치되어 있음
        int cnt = 1;
        long stickPos = arr[0];

        for (int i = 1; i < n; i++) {
            // mid 보다 커지는 부분에 설치함
            if (arr[i] - stickPos >= mid) {
                cnt++;
                stickPos = arr[i];
            }
        }

        return cnt >= m;
    }
}