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

        arr = new long[m];

        long right = 0;
        for (int i = 0; i < m; i++) {
            arr[i] = Long.parseLong(br.readLine());
            right = Math.max(right, arr[i]);
        }

        Arrays.sort(arr);
        long answer = 0;
        long left = 1;
        right = right * n;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            if (check(mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    static boolean check(long mid) {
        long cnt = 0;
        for (int i = 0; i < m; i++) {
            cnt += mid / arr[i];
            if (cnt >= n) {
                return true;
            }
        }
        return cnt >= n;
    }

}